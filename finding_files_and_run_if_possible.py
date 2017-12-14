# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 16:37:47 2017

@author: vchandraprakash
Modified by SarathBapu
"""

import os
import re
import platform
from _ast import excepthandler

def find_file(root_folder, rex):
    result = {}     # Results dictionary 
    i = 0           #Count for Dictionary
    for root,dirs,files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            if result:
                a = os.path.join(root,f)
                print ("Found at this location ", a) 
                
                print("Do you want to open [ y ]") 
                c = input()
                if c.lower() == 'y' :
                    os.startfile(a)
                print('Çontinue Search [ y ]' )
                cont = input()
                if cont.lower() != 'y' :
                    return 


def find_file_in_all_drives(file_name):
    #create a regular expression for the file
    rex = re.compile(file_name)
    # Check if the OS is windows 
    if platform.system() == 'Windows' :
        try :
            import win32api
            #print('win32api')
            for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
                find_file( drive, rex )
        except  ModuleNotFoundError :
            print('win32api module is not found. So just searching for the C: ')
            find_file('C:\\', rex)
    else :
        find_file('\\', rex)

file_name_with_extension = input("Enter the file name with the extension\n")
find_file_in_all_drives( file_name_with_extension )

print("The End")

#############################################################################################
# Output:
#   Enter the file name with the extension
#   eclipse.exe
#   Found at this location  C:\$RECYCLE.BIN\S-1-5-21-1991516528-409794927-3010460085-75116\$RSUYR21\C\eclipse\eclipse-SDK-4.6.2-win32-x86_64\eclipse\eclipse.exe
#   Found at this location  C:\eclipse\eclipse-SDK-4.6.2-win32-x86_64\eclipse\eclipse.exe
#   The End
##########################################################################################