from bluetooth.ble import DiscoveryService, BeaconService

# service = DiscoveryService()
# devices = service.discover(2)
# print(devices)

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

while True:

    beacon_service = BeaconService()
    devices = beacon_service.scan(10)
    
    if devices:

        for address, data in devices.items():
            b = Beacon(data, address)
            print(b)
 
    else:
        print('no devices')
