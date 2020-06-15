import time
from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print ("Discovered device", dev.addr)
        elif isNewData:
            print ("Received new data from", dev.addr)

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)

def getdistance(rssi):
    txpower = -59   #one meter away RSSI
    if rssi == 0:
        return -1
    else:
        ratio = rssi*1.0 / txpower
        if ratio < 1:
            return ratio ** 10
        else:
            return 0.89976 * ratio**7.7095 + 0.111


def log(address, rssi, distance):
    logfile = open("log.txt","a")
    logfile.write(f"Device: {address} - RSSI: {rssi} - Distance: {distance} meter")
    logfile.close()


for dev in devices:

    #erase the content of the previous log file
    file = open("log.txt","r+")
    file.truncate(0)
    file.close()
    distance = getdistance(dev.rssi)
	log(dev.addr, dev.rssi, distance)
    print ("Device %s (%s), RSSI=%d dB, distance=%.2f meter" % (dev.addr, dev.addrType, dev.rssi, distance))
    print(" ")	