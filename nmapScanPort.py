#import nmap for scanning 
import nmap 
#import regular expression for the valid ip address 
import re
#import ipaddress to check the validity of the input IP address
import ipaddress
# import print-color module for a better CLI view
from print_color import print

#use the regular expression to extract the number of ports user want to scan 
# specify <lowest> - <highest> port number

port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

#initiate the port numbers

port_min = 0; 
port_max = 65535

def display_header():
    print("**************************************")
    print("*        ____ _                      *")
    print("*       / ___| | __ _ _   _          *")
    print("*      | |   | |/ _` | | | |         *")
    print("*      | |___| | (_| | |_| |         *")
    print("*       \____|_|\__,_|\__, |         *")
    print("*                     |___/          *")
    print("*                                    *")
    print("*            WELCOME TO              *")
    print("*        Port Scanner Program        *", color="blue")
    print("**************************************")
    print("*                                    *")
    print("*     -Only use for right purpose-   *")
    print("*                                    *")
    print("**************************************")
    print("*           Designed by Clay         *")
    print("**************************************")

# Call the function to display the header
display_header()


#take the input ip 
while True: 
    print("\nWhich ip address you want to scan? ")
    ip_address_entered = input("Enter the ip address: ")
# check the validity of the ipaddress 
    try: 
        #check the validity with the ipaddress module
        ip_address_valid = ipaddress.ip_address(ip_address_entered)
        print("VALID ip address", tag ="succes", tag_color="green", color = "white")
        break
    except: 
        print("INVALID ipaddress", tag ="failure", tag_color="red", color = "white")

#take the port range
while True: 
    #Can scan port from 0-65535
    print("Enter the range of ports that you want to scan (<int> - <int>)")
    port_range = input("Enter the range: ")
    #cut off the space between two numbers: 
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid: 
        #find the lowest port 
        port_min = int(port_range_valid.group(1))
        #find the highest port
        port_max = int(port_range_valid.group(2))
        break

nmap = nmap.PortScanner()
#go through all the port in the range 
for port in range (port_min, port_max + 1):
    try: 
        result = nmap.scan(ip_address_entered, str(port))
        # extract port status from the returned object 
        port_status = (result["scan"][ip_address_entered]["tcp"][port]["state"])
        if port_status == "open":
            print(f"Port {port} is {port_status}", color = "green")
        else: 
            print(f"Port {port} is {port_status}", color = "magenta")
    except:    
        print(f"Cannot scan port {port}.", color = "red")
    