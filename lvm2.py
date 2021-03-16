import os

print("-----------------------------------------------------\n")

print("\tLVM AUTOMATION USING PYHTON SCRIPT\n")
print("-----------------------------------------------------\n")

def createpv():
    pvname = input("Enter device name to create PV:\t")
    os.system("pvcreate "+pvname)

def createvg():
    vgname = input("Enter VG name to create:")
    nd = int(input("Enter how many devices you want to add (number):"))
    devices = ""
    for i in range(nd):
        pv = input("Enter a name pf PV{0}:".format(i+1))
        devices = devices+" "+pv
    print(devices)
    os.system("vgcreate {0} {1}".format(vgname,devices))
    
    
def createlv():
    lvsize = int(input("Enter size of LV to create:"))
    lvname = input("Enter name for LV:")
    vgname = input("Enter VG name:")
    lvpath = "/dev/%s/%s"%(vgname,lvname) 
    os.system("lvcreate --size {0} --name {1} {2}".format(lvsize,lvname,vgname))       
    os.system("mkfs.ext4 {0}".format(lvpath))

def extendlv():
    increase_size = int(input("Enter size to increase size of LV (in GB): "))
    lvpath = input("Enter path of LV partition:")
    os.system("lvextend --size {0} {1}".format(increase_size,lvpath))
    os.system("resize2fs {0}".format(lvpath))
    os.system("df -hT")
    
def reducelv():
    unmountlv()
    lvpath = input("Enter path of LV partition:")
    lvsize = input("Enter size to reduce size of LV (in GB):")
    os.system("e2fsck -f {0}".format(lvpath))
    os.system("resize2fs {0} {1}".format(lvpath,lvsize))
    os.system("lvreduce --size {0} {1}".format(lvsize,lvpath))
    os.system("df -hT")

def displaypv():
    print('''
    1. LIST OF ALL PV
    2. DISPLAY SPECIFIC PV
    \n''')

    choice = int(input("ENTER YOUR CHOICE:"))
    if choice==1:
        os.system("pvdisplay")
    else:
        pvd = input("Enter PV name to display:")
        os.system("pvdisplay {0}".format(pvd))
        
def displayvg():
    print('''
    1. LIST OF ALL VG
    2. DISPLAY SPECIFIC VG
    \n''')

    choice = int(input("ENTER YOUR CHOICE:"))
    if choice==1:
        os.system("vgdisplay")
    else:
        vgd = input("Enter VG name to display:")
        os.system("vgdisplay {0}".format(vgd))

def displaylv():
    print('''
    1. LIST OF ALL LV
    2. DISPLAY SPECIFIC LV
    \n''')

    choice = int(input("ENTER YOUR CHOICE:"))
    if choice==1:
        os.system("lvdisplay")
    else:
        lvd = input("Enter VG name to display:")
        os.system("lvdisplay {0}".format(lvd))

def mountlv():
    mount_point = input("Enter path of directory to mount LV:")
    lvpath = input("Enter path of LV partition:")
    os.system("mount {0} {1}".format(lvpath,mount_point))
    os.system("df -hT")

def unmountlv():
    mount_point = input("Enter mount point to unmount: ")
    os.system("umount {0}".format(mount_point))
    os.system("df -hT")


while True:

    print('''
    =================================
    1. CREATE A PHYSICAL VOLUME (PV)
    2. DISPLAY PHYSICAL VOLUME (PV)
    3. CREATE A VOLUME GROUP (VG)
    4. DISPLAY VOLUME GROUP (VG)
    5. CREATE A LOGICAL VOLUME (LV)
    6. DISPLAY LOGICAL VOLUME (LV)
    7. MOUNT LOGICAL VOLUME (LV)
    8. UNMOUNT LOGICAL VOLUME (LV)
    9. EXTEND LOGICAL VOLUME
    10. REDUCE LOGICAL VOLUME
    11. QUIT
    ==================================
    ''')

    action = int(input("Enter choice to perform action:"))

    if action==1:
        createpv()
    
    elif action==2:
        displaypv()

    elif action==3:
        createvg()

    elif action==4:
        displayvg()

    elif action==5:
        createlv()

    elif action==6:
        displaylv()

    elif action==7:
        mountlv()

    elif action==8:
        unmountlv()

    elif action==9:
        extendlv()

    elif action==10:
        reducelv()

    elif action==11:
        exit()

    else:
        print("\n!! Invalid Action !!")
        
