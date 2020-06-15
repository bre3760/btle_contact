import time
from bluepy.btle import Scanner, DefaultDelegate

# class ScanDelegate(DefaultDelegate):
#     def __init__(self):
#         DefaultDelegate.__init__(self)

#     def handleDiscovery(self, dev, isNewDev, isNewData):
#         if isNewDev:
#             print ("Discovered device", dev.addr)
#         elif isNewData:
#             print ("Received new data from", dev.addr)

# scanner = Scanner().withDelegate(ScanDelegate())
# devices = scanner.scan(5.0)

# def getdistance(rssi):
#     txpower = -59   #one meter away RSSI
#     if rssi == 0:
#         return -1
#     else:
#         ratio = rssi*1.0 / txpower
#         if ratio < 1:
#             return ratio ** 10
#         else:
#             return 0.89976 * ratio**7.7095 + 0.111

# # for dev in devices:
# #     print ("Device %s (%s), RSSI=%d dB, distance=%.2f meter" % (dev.addr, dev.addrType, dev.rssi, getdistance(dev.rssi)))

# for dev in devices:
#     print ("Device %s (%s), RSSI=%d dB, distance=%.2f meter" % (dev.addr, dev.addrType, dev.rssi, getdistance(dev.rssi)))
#     for (adtype, desc, value) in dev.getScanData():
#         print( " %s = %s" % (desc, value))
#     print(" ")

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


def log_file(address):
    logfile = open("log.txt","r+")
    logaddress = logfile.readlines()
    logfile.close()
    found = 0
    for line in logaddress:
        if address == line.rstrip():
            found = 1
    if found == 0:
        logfile = open("log.txt","a")
        logfile.write(f"{address}\n")
        logfile.close()


for dev in devices:
    log_file(dev.addr)
    print ("Device %s (%s), RSSI=%d dB, distance=%.2f meter" % (dev.addr, dev.addrType, dev.rssi, getdistance(dev.rssi)))

    print(" ")
