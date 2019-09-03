from cx_Freeze import setup, Executable
import os

#well see if this thing works, or if I have to import something
#In the future I should change this to say - #Your tcl file location here
os.environ['TCL_LIBRARY'] = r"C:\Users\hcrai\AppData\Local\Continuum\anaconda3\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\hcrai\AppData\Local\Continuum\anaconda3\tcl\tk8.6"


#adding base Win32GUI should make it so that the
setup(name = "Distributed GUI", version = "0.1",
    description = "Executable GUI attempt",
    executables = [Executable("execPrac.py", base = "Win32GUI")])

#Then we do python setup.py build
#into the console, but only if we are in the same directory
#otherwise we will have to enter the entire path for it to build
