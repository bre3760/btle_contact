import sys
import struct
import bluetooth._bluetooth as bluez

from scapy.all import *
from scapy.utils import *


OCF_LE_CTL=0x08
OCF_LE_SET_SCAN_ENABLE=0x000C


# set bluetooth device
dev_id = bluez.hci_get_route('28:39:26:5F:EE:C4')
try:
    sock = bluez.hci_open_dev(dev_id)
except:
    print ("Error accessing bluetooth")
    exit(1)

# send commands to open socket as SCAN_ENABLE
cmd_pkt = struct.pack("<BB", 0x01, 0x00)
bluez.hci_send_cmd(sock, OCF_LE_CTL, OCF_LE_SET_SCAN_ENABLE, cmd_pkt)

# scan for beacons
try:
    while True:

        # filter only for HCI_EVENT_PKT
        flt = bluez.hci_filter_new()
        bluez.hci_filter_all_events(flt)
        bluez.hci_filter_set_ptype(flt, bluez.HCI_EVENT_PKT)
        sock.setsockopt(bluez.SOL_HCI, bluez.HCI_FILTER, flt)

        # Listen forever for frames
        while True:
            packet = sock.recv(255)

            # this is how one would have to go... parsing a field at a time
            # ptype, event, plen = struct.unpack("BBB", packet[:3])

            # .... or outsource the parsing
            pckt = HCI_LE_Meta_Advertising_Report(packet[5:])
            pckt.show()

            # ... Or search a library that implements it all

except KeyboardInterrupt:
    pass
