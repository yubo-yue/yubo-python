#!/usr/bin/python3.4

import time

currentTime = time.time()

totalSeconds = int(currentTime)

currentSeconds = totalSeconds % 60

totalMinutes = totalSeconds // 60

currentMinutes = totalMinutes % 60

totalHours = totalMinutes // 60

currentHour = totalHours % 24


print("Current time is", currentHour, ":", currentMinutes, ":", currentSeconds)
