# PyExeConverterGUI
## Description
_PyExeConverterGUI converts python file (*.py and *.pyw) to exe or msi installer using CX_Freeze._<br />
## Installation
```
pip3 install cx_Freeze
```
And uncomment the commented text at line 32 and 26.
```
check_output("python{} setup.py bdist_msi".format(ver), stderr=STDOUT, shell=True)
check_output("python{} setup.py build".format(ver), stderr=STDOUT, shell=True)
```
## How to use?
First run the program with:`python3 main.py`.<br />
Then browse the python file and select MSI or EXE and click start.<br />
**_Note:This is still in beta and does not support packages!_**
## Credits
Made by [proalexa](https://github.com/proalexa/)<br />
