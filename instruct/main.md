# Instructions
## _How to build your own Installer_
---
You may ask
    Why should I create my own exe?
  - It allows advanced customization, not avaliable in the normal installer.
---
# How To Build an Exe?
The Choice is yours.
Some Programs that I recommend to Build your file.
 - PyInstaller
 - CXFreeze

Today we will talk about PyInstaller.
```sh
pip install pyinstaller
pyinstaller --onefile --hidden-import=
```
MAKE SURE THIS IS RAN ON A WINDOWS MACHINE. ALSO MAKE SURE YOU ARE IN THE WORKING DIRECTORY OF YOUR PROGRAM (C:/%USER%/DOWNLOADS in most cases)
*Please note that you may need to run py -m pip install pyinstaller in some situations, and if pyinstaller doesn't work, try PyInstaller instead, or try py -m PyInstaller
