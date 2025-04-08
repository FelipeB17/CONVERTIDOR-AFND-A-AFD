from cx_Freeze import setup, Executable

setup(
    name="ConvertidorAFNDaAFD",
    version="1.0",
    executables=[Executable("ConvertidorAFNDaAFD .py")]
)