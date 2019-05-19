#Serial Communication .py file includes all serial port init, read and partial send
__author__  = "Serbay Ozkan"
__version__ = "1.0.0"
__email__   = "serbay.ozkan@hotmail.com"
__status__  = "Development"

#Import Python Library Modules
import sys
import serial
import io
import threading
import time

#Global Functions
from AMRProcess import amrSerialListCheckProcess
from AMRProcess import createStartMessageResponse
from AMRProcess import checkAMRQueryType
from AMRProcess import createReadoutMessage
from SystemFunc import waitUntilEnterPressed

#Global Class Objects
from AMRProcess import AMRParams

#Constant Definitions
DEBUG_SERIAL_COM = 1
INVALID_DEVICE_NUMBER = -1

#Inits serial com port with user configured params.
def serialInit():
        global serialPort 
        try:
                serialPort = serial.Serial(AMRParams.comPortName, 
                                          AMRParams.baudrateInStart, 
                                          timeout = 0,
                                          bytesize = AMRParams.dataBit,
                                          parity = AMRParams.parity,
                                          stopbits = AMRParams.stopBit)
                
                print(serialPort.name)
        except:
                print("ERROR_COMM: Please check Com Port!")
                waitUntilEnterPressed()

#Decodes string to UTF-8 Format
def decodeStr(inputStr):
    return inputStr.decode('utf-8')

#Encodes string to Bytes format for serial comm. application
def encodeStr(inputStr):
    return str.encode(inputStr)

#Periodic Read Event Threads
def readFromSerialPort ():
    while True:
        
        readBuffer = serialPort.readline()
        
        if decodeStr(readBuffer) != '':
                #print(decodeStr(readBuffer))
                state = checkAMRQueryType(decodeStr(readBuffer))

                if state == 0:
                        opSuccess = amrSerialListCheckProcess(decodeStr(readBuffer))
                        if opSuccess:
                                writeToSerialPort(createStartMessageResponse(AMRParams.requestedSerialNo))
                                time.sleep(0.01)
                elif state == 1:
                        if AMRParams.deviceNumber != INVALID_DEVICE_NUMBER:
                                if AMRParams.enable[AMRParams.deviceNumber]:
                                        serialPort.baudrate = AMRParams.baudrateInRuntime
                                        time.sleep(0.500)
                                        writeToSerialPort(createReadoutMessage(AMRParams.brand[AMRParams.deviceNumber]))
                                        time.sleep(0.1)
                                        serialPort.baudrate = AMRParams.baudrateInStart

                                AMRParams.deviceNumber = INVALID_DEVICE_NUMBER
                else:
                        print("ERROR_COMM: Unexpected State is occured in runtime!")

        time.sleep(0.01)

#Inits Read Event Thread
def readFromSerialPortThreadInit():
    receiveEvent = threading.Thread(target=readFromSerialPort)
    receiveEvent.start()

#Splits bulks string data to n parts defined by size of s and chunksize
def split_chunks(s, chunksize):
    pos = 0
    while(pos != -1):
        new_pos = s.rfind(" ", pos, pos+chunksize)
        if(new_pos == pos):
            new_pos += chunksize # force split in word
        yield s[pos:new_pos]
        pos = new_pos


#Writes data to serial port. 
#Bulk String data manupulation is implemented
def writeToSerialPort(sendStr):
        partialSendSize = 2000

        strLen = len(sendStr)
        if strLen <= partialSendSize:
                serialPort.write(encodeStr(sendStr))
        else:
                myList = list(split_chunks(sendStr, partialSendSize))
                for i in range (0, len(myList)):
                        serialPort.write(encodeStr(myList[i]))
                        time.sleep(0.1)