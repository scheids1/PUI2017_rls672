from __future__ import print_function
import sys
import json

try: 
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib 

if not len(sys.argv) == 3: 
    print('''Invalid number of arguments''') 
    sys.exit()


key = sys.argv[1]
BUS_LINE = sys.argv[2]

url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' \
    + key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + BUS_LINE

print(url)

response = urllib.urlopen(url)
data = response.read().decode('utf-8')
data = json.loads(data)

realtimebuses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

print('Bus Line : ', BUS_LINE)
print('Number of Active Buses : ', len(realtimebuses))

for bus in range(len(realtimebuses)):
    BUS_LINE = str(realtimebuses[bus]['MonitoredVehicleJourney']['PublishedLineName'])
    longitude = str(realtimebuses[bus]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    latitude = str(realtimebuses[bus]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    print("Bus " + str(bus) + " is at latitude " + latitude + " and longitude " + longitude)
