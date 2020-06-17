# btle_contact
Experimental bluetooth low energy contact tracing
installation guide:
For the pc
-install bluepy (sudo pip3 install bluepy)

For the raspberry pi

-download gattlib (sudo pip3 install gattlib or download gattlib-0.20150805.tar.gz)

-install dependencies (sudo apt-get install python3-pip python-dev libbluetooth-dev libboost-python-dev libboost-thread-dev gir1.2-glib-2.0 librust-glib-sys-dev)

-decompress gattlib-0.20150805.tar.gz, enter in the folder, and install it 
tar -zxvf gattlib-0.20150805.tar.gz

cd gattlib-0.20150805

sudo pip3 install .

-install bluez[ble] (sudo pip3 install pybluez[ble]

-install human patiance (sudo go get a coffee)
