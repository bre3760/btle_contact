import time
from bluepy.btle import Scanner, DefaultDelegate

#Erase content of previus log file
open('log.txt', 'w').close()

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print ("Discovered device", dev.addr)
        elif isNewData:
            print ("Received new data from", dev.addr)

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(5.0)

def getdistance(rssi):

    txpower = -59   #one meter away RSSI
    #txpower = 8.5
    if rssi == 0:
        return -1
    else:
        ratio = rssi*1.0 / txpower
        if ratio < 1:
            return ratio ** 10
        else:
            return 0.89976 * ratio**7.7095 + 0.111


def log_file(address, rssi, distance):
    logfile = open("log.txt","a")
    logfile.write(f"Device: {address} - RSSI: {rssi} - Distance: {distance}\n")
    logfile.close()

for dev in devices:
    print ("Device %s (%s), RSSI=%d dBm, distance=%.2f meter" % (dev.addr, dev.addrType, dev.rssi, getdistance(dev.rssi)))
    #for (adtype, desc, value) in dev.getScanData():
       # print( "  %s = %s" % (desc, value))
    log_file(dev.addr, dev.rssi, getdistance(dev.rssi))
    print(" ")
