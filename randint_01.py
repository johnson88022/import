import random
num  = random.randint(1,100)
while True:
	n = input("猜一个数字{(范围0~100): ")
	n = int(n)
	if n == num:
		print("恭喜猜对")
		break
	elif n > num: 
		print("太大")
	elif n < num:
		print("太小")
	elif n < 0 and n > 100:
		print("范围在0~100哦")   
