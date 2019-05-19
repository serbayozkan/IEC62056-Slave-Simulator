#System Funcs .py file includes basic and general function prototypes
__author__  = "Serbay Ozkan"
__version__ = "1.0.0"
__email__   = "serbay.ozkan@hotmail.com"
__status__  = "Development"

#Import Python Library Modules
import sys
import os

# Restarts the current program
def restartProgram():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# Waits until character is pressed
def waitUntilEnterPressed():
    input("Press Enter to exit...")
    sys.exit(1)