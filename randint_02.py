import random
start = input("请输入开始值")
end = input("请输入开始值")
start = int(start)
end = int(end)
num  = random.randint(start,end)
count = 0    #计算猜几次数字,若写在回圈内则每次次数都会重复1=0+1
while True:
	count = count+1  #快写法:count += 1
	count = int(count)
	n = input("猜一个数字: ")
	n = int(n)
	if n == num:
		print("恭喜猜对")
		print("你总共猜",count,"次")
		break
	elif n > num: 
		print("比",n,"小")
	elif n < num:
		print("比",n,"大")
	elif n < 0 and n > 100:
		print("范围在0~100哦")
	print("这是你的猜",count,"次")




	

	