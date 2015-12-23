from bluetooth.ble import DiscoveryService, BeaconService
from datetime import datetime, date

import os

class Beacon(object):
    def __init__(self, data, address):
        self._uuid = data[0]
        self._major = data[1]
        self._minor = data[2]
        self._power = data[3]
        self._rssi = data[4]
        self._address = address

    def __str__(self):
        return '{0}, RSSI: {1}'.format(self._address, self._rssi)

datadir = '/home/pi/data'
beacon_service = BeaconService()

while True:

    devices = beacon_service.scan(30)
    
    if devices:
        with open('/home/pi/data/data.txt', 'a+') as f:
        
            for address, data in devices.items():
                b = Beacon(data, address)
                print(b)
                dt = datetime.now()
                f.write('{0},{1},{2},{3},{4},{5},{6},{7}\n'.format(b._address, b._rssi, dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second))

    else:
        print('no devices')
