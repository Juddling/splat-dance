import usb.core
import usb.util
import sys

# find our device
dev = usb.core.find(idVendor=0x0E8F, idProduct=0x0035)

# was it found?
if dev is None:
    raise ValueError('Device not found')

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# Let's fuzz around!

# Lets start by Reading 1 byte from the Device using different Requests
# bRequest is a byte so there are 255 different values
for bRequest in range(255):
    try:
        ret = dev.ctrl_transfer(0xC0, bRequest, 0, 0, 1)
        print "bRequest ", bRequest
        print ret
    except:
        # failed to get data for this request
        pass
