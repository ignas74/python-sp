import pyautogui
import time

msg = input("MSG:")
n = input("TIMES:")

print("------------")

count = 5
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

for i in range(0,int(n)):
	pyautogui.typewrite(msg + '\n')