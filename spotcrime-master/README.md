[![NPM version](https://badge.fury.io/js/spotcrime.png)](http://badge.fury.io/js/spotcrime)

## Information

<table>
<tr>
<td>Package</td><td>spotcrime</td>
</tr>
<tr>
<td>Description</td>
<td>API client for crime statistics</td>
</tr>
<tr>
<td>Node Version</td>
<td>>= 0.4</td>
</tr>
</table>

## Usage

```javascript
var spotcrime = require('spotcrime');

// somewhere near phoenix, az
var loc = {
  lat: 33.39657,
  lon: -112.03422
};

var radius = 0.01; // this is miles

spotcrime.getCrimes(loc, radius, function(err, crimes){

});
```

## Example Crimes

```javascript
[ { cdid: 46846473,
    type: 'Assault',
    date: '12/04/13 06:52 PM',
    address: '2200 BLOCK OF E SCHOOL DR',
    link: 'http://spotcrime.com/crime/46846473-bf48f72ccce82295caf2aee6aedca3e1',
    lat: 33.4037116,
    lon: -112.0341417 },
  { cdid: 46845797,
    type: 'Burglary',
    date: '12/03/13 12:00 PM',
    address: '2000 BLOCK OF E ST ANNE AV',
    link: 'http://spotcrime.com/crime/46845797-82cbf298a022813edcee81e0a7ec827b',
    lat: 33.3880011,
    lon: -112.0387037 },
  { cdid: 46846182,
    type: 'Theft',
    date: '12/01/13 08:00 AM',
    address: '2200 BLOCK OF E ALTA VISTA RD',
    link: 'http://spotcrime.com/crime/46846182-818423ce25e8e193cf531e769e0e4c30',
    lat: 33.3892497,
    lon: -112.0344112 },
  { cdid: 46039372,
    type: 'Arrest',
    date: '11/29/13 01:18 AM',
    address: '2000 BLOCK OF E BURGESS LA',
    link: 'http://spotcrime.com/crime/46039372-bb0eb5147f7f6ab63f30ce7298ff2de2',
    lat: 33.3902173,
    lon: -112.0386689 },
  { cdid: 46846219,
    type: 'Assault',
    date: '11/28/13 09:00 AM',
    address: '6000 BLOCK OF S 25TH LA',
    link: 'http://spotcrime.com/crime/46846219-cbe45d070a76520090147ac862b8eae4',
    lat: 33.3933088,
    lon: -112.0272747 },
  { cdid: 46038235,
    type: 'Arrest',
    date: '11/26/13 09:45 PM',
    address: '2100 BLOCK OF E MOBILE LA',
    link: 'http://spotcrime.com/crime/46038235-61f1ce3ad5a5f259b95ca709b7e42700',
    lat: 33.4015345,
    lon: -112.0368315 },
  { cdid: 45526778,
    type: 'Assault',
    date: '11/23/13 12:29 PM',
    address: '2200 BLOCK OF E NANCY LA',
    link: 'http://spotcrime.com/crime/45526778-aacdddd8c5fd83edee8aee7b55ce7cba',
    lat: 33.3907383,
    lon: -112.0343804 },
  { cdid: 45526648,
    type: 'Arrest',
    date: '11/22/13 12:45 AM',
    address: '00 BLOCK OF S 18TH PL',
    link: 'http://spotcrime.com/crime/45526648-8c6523cf0f2ede15fa06ee8ba43ff7a9',
    lat: 33.3996538,
    lon: -112.0425118 },
  { cdid: 45525295,
    type: 'Burglary',
    date: '11/19/13 06:00 PM',
    address: '2000 BLOCK OF E ALTA VISTA RD',
    link: 'http://spotcrime.com/crime/45525295-ac2846846772b7295d08b11c122b764f',
    lat: 33.3894736,
    lon: -112.0386812 },
  { cdid: 45526055,
    type: 'Assault',
    date: '11/17/13 07:00 PM',
    address: '2000 BLOCK OF E SOUTHERN AV',
    link: 'http://spotcrime.com/crime/45526055-2226a1b74f9c35f93eea4f05e8790b8c',
    lat: 33.3928994,
    lon: -112.038771 },
  { cdid: 45526002,
    type: 'Assault',
    date: '11/17/13 01:20 PM',
    address: '1800 BLOCK OF E SUNLAND AV',
    link: 'http://spotcrime.com/crime/45526002-7e8696518721e503edc21b66d681f69a',
    lat: 33.3952706,
    lon: -112.0419982 },
  { cdid: 45399939,
    type: 'Assault',
    date: '11/14/13 06:26 PM',
    address: '1800 BLOCK OF E CHIPMAN RD',
    link: 'http://spotcrime.com/crime/45399939-60fe48fae1b88a8bb13a3f8da1321913',
    lat: 33.4021139,
    lon: -112.0425066 },
  { cdid: 45399867,
    type: 'Theft',
    date: '11/14/13 02:50 AM',
    address: '1800 BLOCK OF E WIER AV',
    link: 'http://spotcrime.com/crime/45399867-16eec0ec24e8826e280f76e3cf3d5960',
    lat: 33.4028975,
    lon: -112.0419515 },
  { cdid: 45399736,
    type: 'Arrest',
    date: '11/13/13 03:48 PM',
    address: '2200 BLOCK OF E ALTA VISTA RD',
    link: 'http://spotcrime.com/crime/45399736-8ad39cd813c9b532c36b067fdc33f389',
    lat: 33.3892497,
    lon: -112.0344112 },
  { cdid: 45399857,
    type: 'Theft',
    date: '11/13/13 09:00 AM',
    address: '2400 BLOCK OF E CHIPMAN RD',
    link: 'http://spotcrime.com/crime/45399857-ebab1be3c66ca74d188fd1a837dc12dc',
    lat: 33.4023596,
    lon: -112.0298543 },
  { cdid: 45399981,
    type: 'Theft',
    date: '11/12/13 10:00 PM',
    address: '2200 BLOCK OF E SOUTHERN AV',
    link: 'http://spotcrime.com/crime/45399981-e45f253643e6738ceb002d476c86bd78',
    lat: 33.393055,
    lon: -112.0343692 },
  { cdid: 45398534,
    type: 'Burglary',
    date: '11/12/13 09:40 PM',
    address: '6000 BLOCK OF S 24TH ST',
    link: 'http://spotcrime.com/crime/45398534-1dd99d3647e293f6e85c3e59e40d1224',
    lat: 33.3931883,
    lon: -112.0300853 },
  { cdid: 45398249,
    type: 'Burglary',
    date: '11/12/13 11:00 AM',
    address: '2500 BLOCK OF E MOBILE LA',
    link: 'http://spotcrime.com/crime/45398249-464b7a13198f081a547b7d3c5df7e3e3',
    lat: 33.4014647,
    lon: -112.0269926 },
  { cdid: 45398125,
    type: 'Burglary',
    date: '11/11/13 05:00 PM',
    address: '2200 BLOCK OF E SUNLAND AV',
    link: 'http://spotcrime.com/crime/45398125-ed1c0ef761d15dc49c5073dcfbde7d65',
    lat: 33.3963898,
    lon: -112.0342238 },
  { cdid: 45397891,
    type: 'Burglary',
    date: '11/10/13 05:00 PM',
    address: '1900 BLOCK OF E ROESER RD',
    link: 'http://spotcrime.com/crime/45397891-d0d1e497c806f4e1141363fa44d2ec33',
    lat: 33.3996718,
    lon: -112.0409278 },
  { cdid: 45397831,
    type: 'Burglary',
    date: '11/10/13 09:00 AM',
    address: '2200 BLOCK OF E ALTA VISTA RD',
    link: 'http://spotcrime.com/crime/45397831-a3069cd4985acc7f10d81e7253717da8',
    lat: 33.3892497,
    lon: -112.0344112 },
  { cdid: 45398680,
    type: 'Assault',
    date: '11/10/13 03:47 AM',
    address: '2200 BLOCK OF E ST CATHERINE AV',
    link: 'http://spotcrime.com/crime/45398680-5042b57e3c8b382023f3b1d8f502f175',
    lat: 33.3885581,
    lon: -112.0344187 },
  { cdid: 45397854,
    type: 'Burglary',
    date: '11/09/13 02:00 AM',
    address: '5700 BLOCK OF S 21ST TE',
    link: 'http://spotcrime.com/crime/45397854-78d4b817012ae47dbd87c52761d7fc24',
    lat: 33.3946717,
    lon: -112.0350565 },
  { cdid: 45286939,
    type: 'Arrest',
    date: '11/05/13 10:58 PM',
    address: '2500 BLOCK OF E MOBILE LA',
    link: 'http://spotcrime.com/crime/45286939-0f5d31616ac37df9341c0a64c2201a0b',
    lat: 33.4014647,
    lon: -112.0269926 },
  { cdid: 45286601,
    type: 'Assault',
    date: '11/04/13 08:27 AM',
    address: '2100 BLOCK OF E CARVER DR',
    link: 'http://spotcrime.com/crime/45286601-6cf7b1a49862dbb04cdf5f1a09a56044',
    lat: 33.4035415,
    lon: -112.0374932 },
  { cdid: 45286385,
    type: 'Arrest',
    date: '11/03/13 12:18 AM',
    address: '1900 BLOCK OF E MOBILE LA',
    link: 'http://spotcrime.com/crime/45286385-93710be743ce7ffbafd083a91eeb59a3',
    lat: 33.4013553,
    lon: -112.0405715 },
  { cdid: 45171443,
    type: 'Arrest',
    date: '11/02/13 12:55 PM',
    address: '2200 BLOCK OF E NANCY LA',
    link: 'http://spotcrime.com/crime/45171443-c035e100285bc17fe5e0db4829037106',
    lat: 33.3907383,
    lon: -112.0343804 },
  { cdid: 45171359,
    type: 'Assault',
    date: '11/02/13 12:38 AM',
    address: '2500 BLOCK OF E ATLANTA AV',
    link: 'http://spotcrime.com/crime/45171359-fe024ee261e9a7ca74d580ade7d75af0',
    lat: 33.400552,
    lon: -112.0270119 },
  { cdid: 45171362,
    type: 'Assault',
    date: '11/02/13 12:20 AM',
    address: '2500 BLOCK OF E MOBILE LA',
    link: 'http://spotcrime.com/crime/45171362-85a51c7741e699a7a75dbea0ab2234e4',
    lat: 33.4014647,
    lon: -112.0269926 },
  { cdid: 45286756,
    type: 'Theft',
    date: '11/01/13 01:00 AM',
    address: '2100 BLOCK OF E HUNTINGTON DR',
    link: 'http://spotcrime.com/crime/45286756-061412908c91bc0eb281c94a2c25849d',
    lat: 33.3935261,
    lon: -112.0361545 },
  { cdid: 45169993,
    type: 'Burglary',
    date: '10/31/13 01:00 PM',
    address: '1100 BLOCK OF E FRAKTUR RD',
    link: 'http://spotcrime.com/crime/45169993-10af575a29849fb468f16ab54c6b1466',
    lat: 33.3957776,
    lon: -112.035973 },
  { cdid: 45286658,
    type: 'Theft',
    date: '10/30/13 06:38 AM',
    address: '2000 BLOCK OF E BURGESS LA',
    link: 'http://spotcrime.com/crime/45286658-e9de501f4c2fe13bbf6bffc1c84fccc6',
    lat: 33.3902173,
    lon: -112.0386689 },
  { cdid: 45170421,
    type: 'Theft',
    date: '10/28/13 12:48 PM',
    address: '2400 BLOCK OF E SOUTHERN AV',
    link: 'http://spotcrime.com/crime/45170421-9025f8a35bc99276306dc893dddae0ce',
    lat: 33.3932169,
    lon: -112.0300395 },
  { cdid: 45169901,
    type: 'Arrest',
    date: '10/27/13 06:29 AM',
    address: '6600 BLOCK OF S 22ND ST',
    link: 'http://spotcrime.com/crime/45169901-7ca79c121712ddf1ecb769379ee8375f',
    lat: 33.3874058,
    lon: -112.0344249 },
  { cdid: 45038273,
    type: 'Burglary',
    date: '10/23/13 04:30 PM',
    address: '5000 BLOCK OF S 24TH ST',
    link: 'http://spotcrime.com/crime/45038273-a640b6bac5b0016d71082887679606a0',
    lat: 33.4014265,
    lon: -112.0299195 },
  { cdid: 45039443,
    type: 'Assault',
    date: '10/23/13 09:00 AM',
    address: '2500 BLOCK OF E MOBILE LA',
    link: 'http://spotcrime.com/crime/45039443-4f2ba90a57a63d75cead4a851b6ed0bf',
    lat: 33.4014647,
    lon: -112.0269926 },
  { cdid: 45038782,
    type: 'Theft',
    date: '10/21/13 03:00 PM',
    address: '2400 BLOCK OF E SOUTHERN AV',
    link: 'http://spotcrime.com/crime/45038782-5db5b9cd7bd5b7417dd1137f845b7204',
    lat: 33.3932169,
    lon: -112.0300395 },
  { cdid: 44894183,
    type: 'Shooting',
    date: '10/18/13 03:39 PM',
    address: '6400 BLOCK OF S 21ST ST',
    link: 'http://spotcrime.com/crime/44894183-5d0b413f7e4c3a28d48610cb028d7d78',
    lat: 33.387732,
    lon: -112.036577 },
  { cdid: 44911288,
    type: 'Assault',
    date: '10/18/13 02:18 PM',
    address: '6400 BLOCK OF S 21ST ST',
    link: 'http://spotcrime.com/crime/44911288-c1efbbd1542fce8a7493223228763555',
    lat: 33.3892406,
    lon: -112.0363713 },
  { cdid: 44911226,
    type: 'Assault',
    date: '10/17/13 09:03 AM',
    address: '4600 BLOCK OF S 21ST ST',
    link: 'http://spotcrime.com/crime/44911226-a5da6b4674cce468c13441e5b5d72ac0',
    lat: 33.4048519,
    lon: -112.0374933 },
  { cdid: 44911141,
    type: 'Assault',
    date: '10/16/13 07:22 PM',
    address: '6400 BLOCK OF S 21ST PL',
    link: 'http://spotcrime.com/crime/44911141-08029f307406e3dad33f2067e09ad97f',
    lat: 33.3892621,
    lon: -112.0355023 },
  { cdid: 45171089,
    type: 'Assault',
    date: '10/16/13 06:00 PM',
    address: '1900 BLOCK OF E HIDALGO AV',
    link: 'http://spotcrime.com/crime/45171089-28227b4f9c26be35690c8dbfef697635',
    lat: 33.3937439,
    lon: -112.0403549 },
  { cdid: 45399029,
    type: 'Theft',
    date: '10/16/13 12:00 PM',
    address: '2300 BLOCK OF E HUNTINGTON DR',
    link: 'http://spotcrime.com/crime/45399029-c3330abb26eae61b51ac7e827197cd3c',
    lat: 33.3934823,
    lon: -112.0324101 },
  { cdid: 44910717,
    type: 'Robbery',
    date: '10/15/13 01:00 PM',
    address: '2200 BLOCK OF E SOUTHERN AV',
    link: 'http://spotcrime.com/crime/44910717-f9f834daa00f8191456c3125296b5112',
    lat: 33.393055,
    lon: -112.0343692 },
  { cdid: 44910713,
    type: 'Assault',
    date: '10/15/13 01:00 PM',
    address: '2300 BLOCK OF E SHERATON LA',
    link: 'http://spotcrime.com/crime/44910713-e41ea41b532986798080e6446812cc90',
    lat: 33.4011662,
    lon: -112.0320788 },
  { cdid: 44909910,
    type: 'Burglary',
    date: '10/14/13 10:25 PM',
    address: '2400 BLOCK OF E SOUTHERN AV',
    link: 'http://spotcrime.com/crime/44909910-0d6137ab2d47cf823ec67430d66d1108',
    lat: 33.3932169,
    lon: -112.0300395 },
  { cdid: 45039181,
    type: 'Robbery',
    date: '10/12/13 04:25 PM',
    address: '2400 BLOCK OF E SOUTHERN AV',
    link: 'http://spotcrime.com/crime/45039181-881d5c4a2b7d3fc1803607ccbcf4be4c',
    lat: 33.3932169,
    lon: -112.0300395 },
  { cdid: 44782000,
    type: 'Assault',
    date: '10/12/13 10:00 AM',
    address: '6400 BLOCK OF S 21ST ST',
    link: 'http://spotcrime.com/crime/44782000-b1495fa097bab2b2b7c06a8daa8f7662',
    lat: 33.3892406,
    lon: -112.0363713 },
  { cdid: 44781985,
    type: 'Theft',
    date: '10/12/13 02:30 AM',
    address: '5100 BLOCK OF S 18TH PL',
    link: 'http://spotcrime.com/crime/44781985-b77fdb76e43f57c8b6923955c1f40a60',
    lat: 33.4001492,
    lon: -112.0425218 },
  { cdid: 44781895,
    type: 'Arrest',
    date: '10/11/13 04:28 PM',
    address: '2000 BLOCK OF E BURGESS LA',
    link: 'http://spotcrime.com/crime/44781895-2a9588f327c3234480e1a276882f3372',
    lat: 33.3902173,
    lon: -112.0386689 } ]
```

## LICENSE

(MIT License)

Copyright (c) 2016 Contra <yo@contra.io>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.