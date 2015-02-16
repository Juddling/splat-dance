import sys
import usb.core
import usb.util
# decimal vendor and product values
dev = usb.core.find(idVendor=0x0E8F, idProduct=0x0035)
# or, uncomment the next line to search instead by the hexidecimal equivalent
# dev = usb.core.find(idVendor=0x45e, idProduct=0x77d)
# first endpoint
interface = 0
endpoint = dev[0][(0, 0)][0]
# if the OS kernel already claimed the device, which is most likely true
# thanks to http://stackoverflow.com/questions/8218683/pyusb-cannot-set-configuration
if dev.is_kernel_driver_active(interface) is True:
  # tell the kernel to detach
  dev.detach_kernel_driver(interface)
  # claim the device
  usb.util.claim_interface(dev, interface)


def left_pressed(data):
  return data & 128 == 128


def up_pressed(data):
  return data & 64 == 64


def right_pressed(data):
  return data & 16 == 16


def down_pressed(data):
  return data & 32 == 32

collected = 0
attempts = 250
while collected < attempts :
    try:
        data = dev.read(endpoint.bEndpointAddress,endpoint.wMaxPacketSize)
        collected += 1
        if left_pressed(data[5]):
          print "left pressed"
        if up_pressed(data[5]):
          print "up pressed"

        print data
    except usb.core.USBError as e:
        data = None
        if e.args == ('Operation timed out',):
            continue
# release the device
usb.util.release_interface(dev, interface)
# reattach the device to the OS kernel
dev.attach_kernel_driver(interface)
