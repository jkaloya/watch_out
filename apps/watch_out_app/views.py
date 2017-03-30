from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import JsonResponse
import math
import requests
import datetime
import bcrypt
from django.contrib import messages
import json
from . import models
from .models import Users, Alerts #already imported models, no need to type models.Alerts

# Create your views here.





def index(request):
	return render(request, 'watch_out_app/index.html')

def login(request):

	return render(request, 'watch_out_app/login.html')

def register(request):

	return render(request, 'watch_out_app/register.html')

def op(request):

	return render(request, 'watch_out_app/op.html')

def alert(request):

	return render(request, 'watch_out_app/alert.html')


def addalert(request):
	print ("inside addalert")
	if "user_id" not in request.session:
		print ("user not logged in")
		return redirect('/login')
	else:
		print ("user logged in")
		return render(request, 'watch_out_app/addalert.html')

def display(request):

	return render(request, 'watch_out_app/display.html')


def retreivealert(lat, lng, desired_dist):
	# we need all the data
	alerts = Alerts.objects.all()
	data = [] # output list containig all the alerts, needs to be converted to json
	# then iterate through it
	lat1 = float(lat)
	lng1 = float(lng)
	for x in alerts:
		alert = x.__dict__ # this will give us the object as dictionary
		# now we extract lat long
		if alert['lati']:
			#print alert['lati']
			#print type(alert['lati'])
			lat2 = float(alert['lati']) # 1st unicode to str, then to float
			lng2 = float(alert['longi'])
			# now the formula
			dist = math.acos(math.sin(math.radians(lat1))*math.sin(math.radians(lat2)) + math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.cos(math.radians(lng1)-math.radians(lng2))) * 3,959
			if dist < 100*desired_dist:
				data.append({u'type' : alert['crime'], u'address' : alert['address'], u'date' : alert['date'].date().strftime("%m-%d-%y %H:%M %p"), u'lat':alert['lati'], u'lon' : alert['longi'], u'link' : alert['description']})

	return data

def formprocess(request):

	print('im in the formprocess')
	data = request.POST
	radius = data['radius']
	lat = data['lat']
	lng = data['lng']
	address = data['address']
	payload = {'lat': lat, 'lon': lng, 'radius': radius, 'key': 'privatekeyforspotcrimepublicusers-commercialuse-877.410.1607'}
	r = requests.get('https://api.spotcrime.com/crimes.json', params=payload)
	#print r
	data = retreivealert(lat, lng, radius) #calling it from here

	#print data
	#we need to convert it to json and add it to the request
	#json.dump(data)
	spot_crime_data = r.json()
	#print spot_crime_data
	final = {u'crimes' : { u'spotcrime' : spot_crime_data['crimes'], u'user': data}}
	#print type(final)
	#final.update(data)


	#final_dat = json.dumps(final, ensure_ascii=True)
	print ('im about to return stuff')

	return JsonResponse(final) # this should do fine

# incomplete method

def addalertprocess(request):
	if request.POST:
		#inputs = request.POST
		#print inputs
		print("add alert process data")
		print(request.POST)
		lat = request.POST.get('lat')
		lng = request.POST.get('lng')
		thisuser = models.Users.objects.get(id = request.session['user_id'])
		alert= models.Alerts.objects.create(address = request.POST.get('address'), lati=lat, longi=lng, date= request.POST.get('date'), crime= request.POST.get('type'), radius=5, description=request.POST.get('description'), poster=thisuser)
		print("this is alert:", alert)
		alerts = Alerts.objects.filter(lati=lat)
		print alerts.values()
	return redirect('/crimes')



#LOGIN REGS
def loginprocess(request):
	post = request.POST
	print post

	email=request.POST.get('email')
	print "email", email
	password=request.POST.get('password')

	#check if existing user or input error
	existuser = models.Users.objects.loginvalid(request,email, password)
	if existuser == True:
		print "user exist"
		user_id = models.Users.objects.get(email = email).id
		request.session['user_id'] = user_id
		context = {
			'username' : email,
			'status' : "logged in"
		}
		return redirect('/')
	##DISPLAY MSGED TO SHOW ERROR
	for ind in range (0, len(existuser)):
		messages.error(request, existuser[ind])
	return redirect('/registration')

def registerprocess(request):
	#GET USER INPUT

	name=request.POST.get('name')
	email = request.POST.get('email')
	password=request.POST.get('password')
	repassword=request.POST.get('re_password')
	newuser = models.Users.objects.registervalid(name, email, password, repassword)
	print newuser
	if not newuser:
		hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
		newuser = models.Users.objects.create(name=name, email=email, hashed_pw=hashed)
		user_id = models.Users.objects.get(email = email).id
		request.session['user_id'] = user_id
		return redirect('/')
	if newuser[0] == "User already exist! Please login instead!":
		print("go to login page")
		return redirect('/login')

	for ind in range (0, len(newuser)):
		messages.error(request, newuser[ind])
	return redirect('/registration')


def loggingout(request):
	request.session.pop('user_id')
	return redirect('/')
