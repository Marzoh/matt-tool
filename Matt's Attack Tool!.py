#!/usr/bin/env python

import time
import random
import re
import os
import webbrowser
import sys

os.system("color a")
print("                                        =====================================")
print("                                                   Please Login!")
print("                                        =====================================")
usr = input("                                        Username: ")
pw = input("                                        Password: ")
os.system("cls")
print("                                        =====================================")
print("                                                  Welcome, " + usr + "!")
print("                                        =====================================")
time.sleep(1)
os.system("cls")
print("                                        =====================================")
print("                                         Loading. [====                ] 26%")
print("                                        =====================================")
time.sleep(1)
os.system("cls")
print("                                        =====================================")
print("                                         Loading.. [=======            ] 43%")
print("                                        =====================================")
time.sleep(1)
os.system("cls")
print("                                        =====================================")
print("                                        Loading... [==========         ] 52%")
print("                                        =====================================")
time.sleep(1)
os.system("cls")
print("                                        =====================================")
print("                                          Loading. [==============     ] 77%")
print("                                        =====================================")
time.sleep(1)
os.system("cls")
print("                                        =====================================")
print("                                         Loading.. [====================] 100%")
print("                                        =====================================")
time.sleep(0.5)
os.system("cls")
print("                                        =====================================")
print("                                        MATT'S ATTACK TOOL! PICK YOUR CHOICE!")
print("                                        =====================================")
print("                                        [1] = DDos Attack")
print("                                        [2] = Bruteforce Attack")
print("")
choice = input("                                        Enter a number: ")
if choice == "1":
	os.system("cls")
	os.system("py ddos.py")
	close()
else:
	print("")

if choice == "2":
	os.system("cls")
	os.system("py brute.py")
	close()
else:
	print("")