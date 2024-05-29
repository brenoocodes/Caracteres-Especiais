import sys
import os
from cx_Freeze import setup, Executable



base = None
if sys.platform == 'win32':
    base = 'Win32GUI'


config = Executable(
    script='main.py',
    base=base

)

setup(
    name='Retira caracteres especiais',
    version='1.0',
    description='Programa pede uma pasta de arquivos, onde ele irá varrer todos os arquivos e tirar os caracteres especiais, além disso você vai escolher uma pasta destino que será enviado os arquivos sem caracteres especiais, mantendo a pasta origem sem nenhuma modificação',
    author='Breno Codes',
    options = {'build_exe':{'include_msvcr':True}},
    executables=[config]

)