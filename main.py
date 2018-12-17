import time, os, shutil, subprocess, ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def backup_procedure():
    print("!! Starting backup procedure !!")
    timestamp = time.strftime('%Y%m%d%H%M',time.localtime())
    try:
        os.mkdir("C:/Program Files/Nuix/WRA Backup %s" %(timestamp))
    except:
        print("ERROR: Could not make backup directory C:/Program Files/Nuix/WRA Backup %s" %(timestamp))
        raise

    os.chdir("C:/Program Files/Nuix/WRA Backup %s" %(timestamp))
    snapshots = input("Backup Snapshots? [N]: ")
    print("Warning: The thumbnails folder can be very large and may take a long time to backup. Thumbnails can be regnerated again if need be.")
    thumbnails = input("Backup Thumbnails? [N]: ")
    mariaDB = input("Backup MariaDB User Database? [N]: ")
    print("User and Group config stores things like user dashboard perspectives and group highlighting options")
    config = input("Backup User and Group configs? [N]: ")

    if (snapshots.lower() == "y") or (snapshots.lower() == "yes"):
        if os.path.exists("../Web Platform/Nuix Config/snapshots"):
            try:
                shutil.copytree("../Web Platform/Nuix Config/snapshots","Nuix Config/snapshots")
            except:
                print('Failed to copy snapshots')
                raise
        else:
            print("WARN: Snapshots directory does not exist")

    #This should get the location of thumbnails from the nuix-restful-service.properties file
    if (thumbnails.lower() == "y") or (thumbnails.lower() == "yes"):
        if os.path.exists("../Web Platform/Nuix IMS/thumbnails"):
            try:
                shutil.copytree("../Web Platform/Nuix IMS/thumbnails", "Nuix IMS/thumbnails")
            except:
                print('Failed to copy thumbnails')
                raise
        else:
            print("WARN: Thumbnails directory does not exist")

    if (mariaDB.lower() == "y") or (mariaDB.lower() == "yes"):
        if os.path.exists("../Web Platform/Nuix UMS/Nuix MariaDB"):
            try:
                shutil.copytree("../Web Platform/Nuix UMS/Nuix MariaDB", "Nuix UMS/Nuix MariaDB")
            except:
                print('Failed to copy Nuix MariaDB')
                raise
        else:
            print("WARN: Nuix MariaDB directory does not exist")

    if (config.lower() == "y") or (config.lower() == "yes"):
        if os.path.exists("../Web Platform/Nuix UMS/config"):
            try:
                shutil.copytree("../Web Platform/Nuix UMS/config", "Nuix UMS/config")
            except:
                print('Failed to copy config directory')
                raise
        else:
            print("WARN: config directory does not exist")

def uninstall():
    print("!! Starting uninstall procedure !!")
    if os.path.isfile("C:/Program Files/Nuix/Web Platform/Nuix MMS/uninstall.exe"):
        print("Uninstalling MMS... Please follow the prompts on screen")
        subprocess.call("C:/Program Files/Nuix/Web Platform/Nuix MMS/uninstall.exe")
    if os.path.isfile("C:/Program Files/Nuix/Web Platform/Nuix Web Review/uninstall.exe"):
        print("Uninstalling Nuix Web Review... Please follow the prompts on screen")
        subprocess.call("C:/Program Files/Nuix/Web Platform/Nuix Web Review/uninstall.exe")
    if os.path.isfile("C:/Program Files/Nuix/Web Platform/Nuix UMS/uninstall.exe"):
        print("Uninstalling Nuix UMS... Please follow the prompts on screen")
        subprocess.call("C:/Program Files/Nuix/Web Platform/Nuix UMS/uninstall.exe")
    if os.path.isfile("C:/Program Files/Nuix/Web Platform/Nuix IMS/uninstall.exe"):
        print("Uninstalling Nuix IMS... Please follow the prompts on screen")
        subprocess.call("C:/Program Files/Nuix/Web Platform/Nuix IMS/uninstall.exe")
    if os.path.isfile("C:/Program Files/Nuix/Web Platform/Nuix Config/uninstall.exe"):
        print("Uninstalling Nuix Config... Please follow the prompts on screen")
        subprocess.call("C:/Program Files/Nuix/Web Platform/Nuix Config/uninstall.exe")

### Main section ###
if is_admin():
    print("Please ensure you have taken a snapshot before uninstalling. This feature can be found in Nuix Config. You will need to restore this snapshot after your fresh install is completed.")
    backup = input("Do you want to backup anything before uninstalling? [Y]: ")

    if (backup.lower() == "y") or (backup.lower() == "yes") or (backup == ""):
        backup_procedure()
        uninstall()
    else:
        print("Proceeding without backing up anything - Please ensure this is correct!")
        proceed = input("Proceed without backing up? [N]")
        if (proceed.lower() == "y") or (proceed.lower() == "yes"):
            uninstall()
        else:
            backup_procedure()
            uninstall()

    cleanup = input("Do you want to wipe the install directory? [N]: ")
    if (cleanup.lower() == "y") or (cleanup.lower() == "yes"):
        try:
            shutil.rmtree("C:/Program Files/Nuix/Web Platform")
        except:
            print("Failed to remove the Web Platform directory..")
            raise
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

print("Done!")
