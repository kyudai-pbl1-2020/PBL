import subprocess
import time
import serial


class ScaleController:
    def __init__(self):
        self.port = '/dev/ttyUSB0'
        self.baudrate = 9600
        self.timeout = 1
        self.parity = serial.PARITY_EVEN
        self.stopbits = serial.STOPBITS_ONE
        self.bytesize = serial.SEVENBITS
        
        self.ser = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            timeout=self.timeout,
            parity=self.parity,
            stopbits=self.stopbits,
            bytesize=self.bytesize
        )

    def setup(self):
        #print(self.ser.isOpen())
        self.ser.write(b'C\r')
        time.sleep(0.1)
        self.ser.write(b'C\r')
        time.sleep(0.1)
        self.ser.write(b'C\r')  
        time.sleep(0.1)
        self.ser.write(b'SIR\r')
        time.sleep(0.1)
        self.ser.write(b'SIR\r')
        time.sleep(0.1)
        self.ser.write(b'SIR\r')

    def escaping(self,c):
        if c != '\r' and (ord(c)<0x20 or ord(c)> 0x7e):
            return ''
        return c

    def dataprocess(self,esc):
        weight = None
        escaped_split = esc.split('\r')
        for line in escaped_split[:-1]:
            if line[0:2] != 'ST':
                continue
            try:
                weight = float(line[3:12])
            except:
                continue
            #print('{:.2f}'.format(weight),flush=True)

        return weight


    def getWeight(self):
        self.setup()

        scale = b''
        escaped = ''

        if(self.ser.in_waiting != 0):
            data = self.ser.read(self.ser.in_waiting)
            scale += data
        if len(scale) > 0:
            escaped += ''.join(list(map(self.escaping,scale.decode())))
            escaped = self.dataprocess(escaped)
            #scale = b''

        self.ser.write(b'C\r')
        return escaped


#TESTING
if __name__ == "__main__":
    currentWeight = None
    sc = ScaleController()
    while currentWeight == None:
        currentWeight = sc.getWeight()
    print(currentWeight)
