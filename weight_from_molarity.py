# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 11:32:04 2023

@author: Kshitij Vashisth
"""
'''
a = input (":")
b = float(a)/50
print(b)
'''
print("A wet lab program by ::KayVeez::\n")

#Calculate required solute from molarity
mol_m = float(input("Please input molar mass of compoound in grams/mol : ")) 
mol = float(input("Please input molarity (in mM) of compound : "))
vol = float(input("Please input volume of solvent in milliliters : "))
weight =  ((mol/1000)*vol*mol_m)/1000
print(weight,"grams")
b = input("Do you want to continue? Y/N : ")

while True:
    if b=="Y":
        mol_m = float(input("Please input molar mass of compoound in grams/mol : ")) 
        mol = float(input("Please input molarity of compound : "))
        vol = float(input("Please input volume of solvent in milliliters : "))
        weight =  (mol*vol*mol_m)/1000
        print(weight,"grams")
    else:
        a = 'Thank You!'
        print(a)
        break
b = input("Press Enter to exit...")
 
