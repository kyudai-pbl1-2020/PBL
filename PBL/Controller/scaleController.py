import subprocess
import time
import serial
# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
   port='/dev/ttyUSB0',
   baudrate=9600,
   timeout=1,
   parity=serial.PARITY_EVEN,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.SEVENBITS
)
print(ser.isOpen())
ser.write(b'C\r')
time.sleep(0.1)
ser.write(b'C\r')
time.sleep(0.1)
ser.write(b'C\r')
time.sleep(0.1)
ser.write(b'SIR\r')
time.sleep(0.1)
ser.write(b'SIR\r')
time.sleep(0.1)
ser.write(b'SIR\r')

def escaping(c):
    if c != '\r' and (ord(c)<0x20 or ord(c)> 0x7e):
        return ''
    return c
    
def dataprocess(esc):
    escaped_split = esc.split('\r')
    for line in escaped_split[:-1]:
        if line[0:2] != 'ST':
            continue
        try:
            weight = float(line[3:12])
        except:
            continue
        print('{:.2f}'.format(weight),flush=True)
            
            
    return escaped_split[-1]
            
scale = b''
escaped = ''
# Reading the data from the serial port. This will be running in an infinite loop.
while True :
    if(ser.in_waiting != 0):
        data = ser.read(ser.in_waiting)
        scale += data
    if len(scale) > 0:
        escaped += ''.join(list(map(escaping,scale.decode())))
        escaped = dataprocess(escaped)
        scale = b''
