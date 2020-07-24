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

    def process(self,data):
        data = data.decode()
        data = data.split(',')[1]
        data = data.replace("+", "")
        data = data.strip("0")
        return data


    def getWeight(self):
        self.setup()
        scale = b''

        if(self.ser.in_waiting != 0):
            data = self.ser.read(self.ser.in_waiting)
            scale += data

        self.ser.write(b'C\r')
        weight = self.process(scale)
        return weight


#TESTING
if __name__ == "__main__":
    currentWeight = None
    sc = ScaleController()
    currentWeight = sc.getWeight()
    print(currentWeight)
