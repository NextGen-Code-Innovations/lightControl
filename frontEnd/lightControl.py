from os import system as cmd
import time

print("[0] Reboot all network servers")
print("[1] Start server side things")
masterOption = int(input("Enter your option here: "))

if masterOption == 0:
    print("test")
elif masterOption == 1:
    print("null test")
else:
    exit()