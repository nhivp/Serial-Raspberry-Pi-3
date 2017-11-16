# Using UART Serial with Raspberry Pi 3

### Default serial is configured for Raspberry Pi 3

* /dev/ttyS0: Serial for Pinout
* /dev/ttyAMA0: Serial for Bluetooth

### Refer to the following step in usage:

1. Connect the UART to pinout on Raspberry Pi 3 (Pin 14, 15) 
2. Open serial *_/dev/ttyS0_* for using

### Some useful command

* dmesg | grep tty
* ls -l /dev/ | grep tty

## Reference

* [Raspberry Pinout](https://pinout.xyz/pinout/uart#)
* [Configuring The GPIO Serial Port On Raspbian Jessie Including Pi 3](https://spellfoundry.com/2016/05/29/configuring-gpio-serial-port-raspbian-jessie-including-pi-3/)