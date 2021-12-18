import random
num  = random.randint(1,100)
count = 0
while True:
	count = count+1  #快写法:count += 1
	count = int(count)
	n = input("猜一个数字(范围0~100): ")
	n = int(n)
	if n == num:
		print("恭喜猜对")
		break
	elif n > num: 
		print("比",n,"小")
	elif n < num:
		print("比",n,"大")
	elif n < 0 and n > 100:
		print("范围在0~100哦")
	print("这是你的猜",count,"次")

	