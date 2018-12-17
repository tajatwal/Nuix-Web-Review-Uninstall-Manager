# Nuix Web Review Uninstall Manager
A small utility written in Python to assist with backup and uninstall for the Nuix Web Review services. 

This utility will guide the user through the process of uninstalling all of the various services, and requesting confirmation if certain directories should be backed up. This will allow you to backup group configuration, the MariaDB instance, dashboard perspectives, snapshots, etc. 

## Getting started
You can either download the source code directly or find the latest release here:\n
https://github.com/RealLukeManning/Nuix-Web-Review-Uninstall-Manager/releases

Please ensure you have taken a snapshot before running this utility. This feature can be found in Nuix Config. You will need to restore this snapshot after your fresh install is completed. A snapshot maitains all of your configuration settings. 

For the initial release this utility will only work with the default directories being used. All services must be installed under the default directory, and none of the user defined directories must be changed from the default location:\n
C:\\Program Files\\Nuix\Web Platform\\

This application needs to run with Administrator privileges to succcessfully backup all the required directories, and to run the uninstall.exe for all services. Nothing is required from the user to achieve this as the application will prompt the user to allow for elevated privileges. 

A backup directory will be created in the "C:\Program Files\Nuix\Web Platform" directory named "WRA Backup \<Timestamp\>". 

Simply follow the prompts on screen to uninstall all of the services, and decide which directories to backup before uninstalling. 

## Disclaimer
I assume no responsibility or liability for any errors or problems that arise from the use of this script. The information and code contained in this repository is provided on an “as is” basis with no guarantees of completeness, accuracy, usefulness or timeliness. Please ensure this script is tested thoroughly in your environment before ever running on a production machine. 

This is a personal project and has no affiliation with Nuix in any way. It is not an official Nuix utility and is not supported by Nuix directly. 
