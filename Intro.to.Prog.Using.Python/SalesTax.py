#!/usr/bin/python3.4

purchaseAmount = eval(input("Enter purchase amount:"))

tax = purchaseAmount * 0.06

print("Sales tax is", int(tax * 100) / 100.0)
