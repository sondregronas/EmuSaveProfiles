# EmuSaveProfiles
Quick and dirty tool to manage mulitple users for savefiles for emulators.
Written in Python 2.7.13
<br>
#### Usage:
- Add all absolute filepaths to 'gamesaves' folders on multiple lines in savepaths.cfg, comment with # or space.<br>
- Create a shortcut of the script, and change the target properties to: ```"MyDirectory\EmuSaveProfiles.py" usernamehere```. If no user is - specified, 'default' will be used.<br>
- On the first run of the script, the current user will claim every folder in savepaths.cfg.<br>
- When running the script with a different user, all folders will be renamed to <name>.<name_of_owner>, and a new folder will be made with a new .emusaves identifying file.<br>
- Best enjoyed when run along with a gamelauncher like BigBox using a .bat file, can be run from the Nvidia Gamestream:<br>
```
BigBoxLauncher_MyUser
@echo off
start "" "EmuSaveProfile_MyUser.lnk"
start "" "BigBox.exe"
```
<br>
The script works by adding an identifier file to these folders, and renaming them when another user is in use. So if you have user1 and user2, the folders would be: Saves, containing an empty user1.emusaves file, and Saves.user2, containing an empty user2.emusaves file. Simple!
