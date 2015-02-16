import sys
import usb.core
import usb.util

dev = usb.core.find(idVendor=0x0E8F, idProduct=0x0035)

interface = 0
endpoint = dev[0][(0, 0)][0]

# if the OS kernel already claimed the device, which is most likely true
# thanks to http://stackoverflow.com/questions/8218683/pyusb-cannot-set-configuration
if dev.is_kernel_driver_active(interface) is True:
    dev.detach_kernel_driver(interface)
    usb.util.claim_interface(dev, interface)


class DanceMat():
    def __init__(self):
        pass

    def update(self):
        self.data = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)

    def right(self):
        return self.data[5] & 128 == 128

    def up(self):
        return self.data[5] & 64 == 64

    def left(self):
        return self.data[5] & 16 == 16

    def down(self):
        return self.data[5] & 32 == 32

    def end(self):
        usb.util.release_interface(dev, interface)
        dev.attach_kernel_driver(interface)
