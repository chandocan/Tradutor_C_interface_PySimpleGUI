from sys import platform
from cx_Freeze import  setup, Executable
# se tiver rodando no windows tem que colocar essa condição 
base = None
if platform == 'win32':
    base = 'Win32Gui'


setup(
    nome = 'tradutor_inglês_espanhol_russo_chines_hindi',
    version = '0.1',
    description='Tradutor feito por Sr. Jose Alfedo de ADS ano 2021',
    options={
        'build_exe': {
           'includes':['tkinter', 'ttkbootstrap']
        }
    },
    executables = [
         Executable('Tradutor.py', base=base)
    ],
)
