#JSON Parser .py main file
#Uses json module of Python

__author__  = "Serbay Ozkan"
__version__ = "1.0.0"
__email__   = "serbay.ozkan@hotmail.com"
__status__  = "Development"

#Import Python Library Modules
import json
import os
import serial

#Global Class Objects
from tkinter            import Tk

#Global Functions
from tkinter.filedialog import askopenfilename

#Parses Serial Port Data Bit Info comes from user configuration file
def parseSerialDataBit(dataBit):
    from AMRProcess import AMRParams

    if dataBit == 7:
            AMRParams.dataBit = serial.SEVENBITS

    elif dataBit == 8:
            AMRParams.dataBit = serial.EIGHTBITS
    
    else:
            AMRParams.dataBit = serial.EIGHTBITS

#Parses Serial Port Stop Bit Info comes from user configuration file
def parseSerialStopBit(stopBit):
    from AMRProcess import AMRParams

    if stopBit == 1:
        AMRParams.stopBit = serial.STOPBITS_ONE
    elif stopBit == 2:
        AMRParams.stopBit = serial.STOPBITS_TWO
    else:
        AMRParams.stopBit = serial.STOPBITS_ONE

#Parses Serial Port Parity Info comes from user configuration file
def parseSerialParity(parity):
    from AMRProcess import AMRParams

    if parity == "NONE":
        AMRParams.parity = serial.PARITY_NONE
    elif parity == "EVEN":
        AMRParams.parity = serial.PARITY_EVEN
    elif parity == "ODD":
        AMRParams.parity = serial.PARITY_ODD
    else:
        AMRParams.parity = serial.PARITY_NONE

#Parses AMRParams.json file and binds to AMR class objects
def parseAMRParamsFromJSONFile():
    from AMRProcess import AMRParams
    print("USER_MESSAGE: Please Select AMR Config File(AMRParams.json)")
    Tk().withdraw()
    jsonFileName = askopenfilename() # Shows an "Open" dialog box and return the path to the selected file

    with open(jsonFileName) as jsonData:
        amrParamsJSON = json.load(jsonData)

    AMRParams.comPortName = amrParamsJSON["COMPortName"]
    AMRParams.baudrateInStart = int(amrParamsJSON["BaudrateInStart"])
    AMRParams.baudrateInRuntime = int(amrParamsJSON["BaudrateInRuntime"])
    parity = amrParamsJSON["Parity"]
    dataBit = int(amrParamsJSON["DataBit"])
    stopBit = int(amrParamsJSON["StopBit"])
    AMRParams.brand = amrParamsJSON["MeterBrandName"]
    AMRParams.serialNo = amrParamsJSON["MeterSerialNumbers"]
    AMRParams.enable = amrParamsJSON["CommunicationEnable"]

    parseSerialDataBit(dataBit)
    parseSerialParity(parity)
    parseSerialStopBit(stopBit)

