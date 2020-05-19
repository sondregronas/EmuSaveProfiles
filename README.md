# EmuSaveProfiles
Quick and dirty tool to manage mulitple users for savefiles for emulators.
Written in Python 2.7.13
<br>
#### Usage:
- Add the save-game folders on separate lines in savepaths.cfg (make comments with either # or space.<br>
- Create a shortcut of the script, right click into properties and change the target properties to: ```"MyDirectory\EmuSaveProfiles.py" usernamehere```. If no user is specified, 'default' will be used.<br>
- On the first run of the script, the current user will claim every folder in savepaths.cfg, by adding a file into each folder with an identifier like 'default.emusaves'.<br>
- When running the script with a different user, all folders will be renamed to <name>.<name_of_owner>, and a new folder will be made with a new .emusaves identifying file. For example 'User1.emusaves'.<br>
- Best enjoyed when run along with a gamelauncher like BigBox using a .bat file that can be run from the Nvidia Gamestream, like BigBox_User.bat:<br>
```
BigBoxLauncher_MyUser
@echo off
start "" "EmuSaveProfile_MyUser.lnk"
start /WAIT "" "BigBox.exe"
exit
```
<br>
Ideally this script would have some backup functionality that could move a copy of every savegame into it's own directory, but as for now it's just a simple way of "swapping memory cards" in use with certain emulators that don't let you store multiple savefiles.
