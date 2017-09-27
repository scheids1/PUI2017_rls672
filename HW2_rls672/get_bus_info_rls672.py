from __future__ import print_function 

import os
import json
import sys

try: 
    import urllib2 as urllib
except ImportError: 
    import urllib.request as urllib

key = sys.argv[1]
route = sys.argv[2]

fout = open(sys.argv[3], "w")

fout.write("Latitude,Longitude,Stop Name,Stop Status\n")

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + \
key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + route

response = urllib.urlopen(url)
data = response.read()
data = json.loads(data)

realtimebuses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'] 

print('Bus Line : ', route)
print('Number of Active Buses : ', len(realtimebuses))
print('Latitude','Longitude','Stop Name','Stop Status')
for bus in range(len(realtimebuses)):
    longitude = str(realtimebuses[bus]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    latitude = str(realtimebuses[bus]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    stopname = str(realtimebuses[bus]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])
    status = str(realtimebuses[bus]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])
    if not stopname: 
        stopname = 'N/A'
    if not status: 
        status = 'N/A'
    print(latitude + ',' + longitude + ',' + stopname + ',' + status)
    fout.write('{},{},{},{}\n'.format(latitude, longitude, stopname, status))
