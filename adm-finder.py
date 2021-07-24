# Author:    Hades.y2k
# Contrubutions: AnonyminHack5
# Version:   1.0
# Date:      11/05/2015
# License:   <OpenSource GPL>

import sys
import httplib
import socket

class bcolors: # This class will be use to make fonts with colors
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

# Real Fun Start Here!
class adminfinder():
    print ""
    print bcolors.HEADER + "\t###################################################################" + bcolors.ENDC
    print bcolors.HEADER + "\t#    ######   ######   #### ####   #####    #######               #" + bcolors.ENDC
    print bcolors.HEADER + "\t#     #####   #####    #### ####   #####    #####                 #" + bcolors.ENDC
    print bcolors.HEADER + "\t#      ####   ####     #### ####   #####   #####                  #" + bcolors.ENDC
    print bcolors.HEADER + "\t#       #########      #### ####   ##########                     #" + bcolors.ENDC
    print bcolors.HEADER + "\t#         #####        #### ####   #########                      #" + bcolors.ENDC
    print bcolors.HEADER + "\t#          ###         #### ####   ##########                     #" + bcolors.ENDC
    print bcolors.HEADER + "\t#          ###         #### ####   #####   #####   ADMIN FINDER   #" + bcolors.ENDC
    print bcolors.HEADER + "\t#          ###         #### ####   #####    #####   by Hades.y2k  #" + bcolors.ENDC
    print bcolors.HEADER + "\t#          ###         #### ####   #####    ######    version 1.0 #" + bcolors.ENDC
    print bcolors.HEADER + "\t###################################################################" + bcolors.ENDC
    print ""

    def __init__(self):
        self.admin_locate()

    def admin_locate(self):
        try:
            try:
                site = raw_input(bcolors.BLUE + "Enter the Web Site URL: " + bcolors.ENDC)
                site = site.replace("http://", "")
                print bcolors.YELLOW + "\n\t[*] Checking the website " +  site + bcolors.ENDC
                conn = httplib.HTTPConnection(site)
                conn.connect()  # Connecting the website
                print bcolors.GREEN + "\t[+] Connection Established, It's Online.\n" + bcolors.ENDC
            except (httplib.HTTPResponse, socket.error) as Exit:
                print bcolors.RED + "\t[!] Cannot Connect to the Website, It might be offline or invalid URL.\n" + bcolors.ENDC
                sys.exit()

            print bcolors.YELLOW + "\t[*] Scanning: " + site + bcolors.ENDC + "\n"
            

            # This will Loop through Word List to get Admin Page
            wordfile = open("wordlist.txt", "r")
            wordlist = wordfile.readlines()
            wordfile.close()

            for word in wordlist:
                admin = word.strip("\n")
                admin = "/" + admin
                target = site + admin
                print bcolors.YELLOW + "[*] Checking: " + target + bcolors.ENDC
                connection = httplib.HTTPConnection(site)
                connection.request("GET", admin)
                response = connection.getresponse()


                # Deciding the Response Status and Print out the result!....
                if response.status == 200:
                    print bcolors.GREEN + "\n\n\t+------------------------------------------------------+" + bcolors.ENDC
                    print "%s %s" % (bcolors.GREEN + "\t[!] Admin Page Found >> " + bcolors.ENDC, bcolors.GREEN + target + bcolors.ENDC)
                    print bcolors.GREEN + "\t+------------------------------------------------------+\n" + bcolors.ENDC
                    raw_input(bcolors.YELLOW + "[*] Press enter to continue.\n" + bcolors.ENDC)

                elif response.status == 302:
                    print bcolors.RED + "[!] 302 Object moved temporarily.\n" + bcolors.ENDC

                elif response.status == 404:
                    print bcolors.RED + "[!] 404 Web Page Not Found.\n" + bcolors.ENDC

                elif response.status == 410:
                    print bcolors.RED + "[!] 410 Object removed permanently.\n" + bcolors.ENDC
                
                else:
                    print "%s %s %s %s" % (bcolors.RED + "Unknown Response: " + bcolors.ENDC, bcolors.RED + response.status + bcolors.ENDC, "\n", bcolors.RED + host + bcolors.ENDC)
                connection.close() # After fun jobs, we are closing connection.

        except (httplib.HTTPResponse, socket.error):
            print bcolors.RED + "\n\t[!] Session Cancelled, An Error Occured." + bcolors.ENDC
            print bcolors.RED + "\t[!] Check Your Internet Connection" + bcolors.ENDC
        except (KeyboardInterrupt, SystemExit):
            print bcolors.RED + "\t[!] Session Interrupted and Cancelled." + bcolors.ENDC

if __name__ == "__main__":
    adminfinder()
