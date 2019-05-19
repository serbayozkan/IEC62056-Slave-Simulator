#Main .py file includes all initilization and runtime functions of AMR System
__author__  = "Serbay Ozkan"
__version__ = "1.0.0"
__email__   = "serbay.ozkan@hotmail.com"
__status__  = "Development"

#Import Python Library Modules
import os 
import sys

#Global Functions
from JSONParser       import parseAMRParamsFromJSONFile
from SerialComProcess import serialInit
from SerialComProcess import readFromSerialPortThreadInit
from AMRProcess       import amrInit

#Parses AMRParams.json file
parseAMRParamsFromJSONFile()

#Inits all serial comm. layer
serialInit()

#Inits AMR Serial List Check Operation
amrInit()

#Calls periodically read event to handle master requests
readFromSerialPortThreadInit()
