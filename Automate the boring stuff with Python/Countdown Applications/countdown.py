import time, subprocess

print('Enter number of seconds when timer should fire')
timeLeft = int(input())

while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft -= 1

subprocess.Popen(['open', 'alarm.wav'])
