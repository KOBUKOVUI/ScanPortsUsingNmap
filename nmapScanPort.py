import nmap 
import re 

ipAddressPattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
portRangePattern = re.compile("([0-9]+)-([0-9]+)")

portMin = 0
portMax = 65535

print("==============================")
print("Welcome to the port scanner!!!")
print("______________________________")
print("Designed by Clay")
print("==============================")
openPort = []

while True: 
    ipAddressEntered = input("\nEnter the ip address: ")
    if ipAddressPattern.search(ipAddressEntered): 
        print(f"{ipAddressEntered} is valid")
        break 

while True: 
    print("Enter the range of ports you want to scan(between 20-100): ")
    portRange = input("Enter port range(firstPort - lastPort): ")
    portRangeValid = portRangePattern.search(portRange.replace(" ",""))
    if portRangeValid: 
        portMin = int(portRangeValid.group(1))
        portMax = int(portRangeValid.group(2))
        break

nm = nmap.PortScanner()

for port in range(portMin, portMax + 1): 
    try: 
        result = nm.scan(ipAddressEntered, str(port))
        portStatus = (result['scan'][ipAddressEntered]['tcp'][port]['state'])
        if portStatus == 'open':
            print(f"\033[1;32;40m Port: {port} is {portStatus}")
            
        else: 
            print(f"\033[1;31;40mPort: {port} is {portStatus}")
    except: 
        print("Cannot scan port")