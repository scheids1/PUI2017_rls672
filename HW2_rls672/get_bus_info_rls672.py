from __future__ import print_function 

import os
import json
import sys

try: 
    import urllib2 as urllib
except ImportError: 
    import urllib.request as urllib


if not len(sys.argv) == 4: 
    print('''Invalid number of arguments. Script takes arguments as: python get_bus_info.py <MTA_KEY> <BUS_LINE> <FILENAME.csv>''') 
    sys.exit()

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
for i in range(len(realtimebuses)):
    longitude = str(realtimebuses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    latitude = str(realtimebuses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    if not (realtimebuses[i]['MonitoredVehicleJourney']['OnwardCalls']):
        stopname = 'N/A'
        status = 'N/A'  
    else:
        stopname = str(realtimebuses[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])
        status = str(realtimebuses[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])
    print(latitude + ',' + longitude + ',' + stopname + ',' + status)
    fout.write('{},{},{},{}\n'.format(latitude, longitude, stopname, status))
