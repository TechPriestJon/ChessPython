import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "pyglet"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Chess Game",
        version = "0.1",
        description = "Chess Game!",
        options = {"build_exe": build_exe_options},
        executables = [Executable(targetName="chess-python.exe", base=base, script="__main__.py")])