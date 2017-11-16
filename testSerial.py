import serial
import struct

def main():
    port = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=3.0)
    port.write(struct.pack('>B', 1))
    print('Send OK')
    port.close()

if __name__ == '__main__':
    main()