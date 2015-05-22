#!/usr/bin/python3.4

seconds = eval(input("Enter an integer for seconds:"))

minutes = seconds // 60 # Find minutes in seconds
remainingSeconds = seconds % 60
print(seconds, "seconds is", minutes, "minutes and", remainingSeconds, "seconds")
