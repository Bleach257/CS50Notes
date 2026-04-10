import random
num = random.randint(1,10)
guess_num = int(input("猜数字： "))
if guess_num == num:
    print("对")
else:
    if guess_num > num:
        print("大了")
    else:
        print("小了")

guess_num = int(input("cai shu zi"))
if guess_num == num:
    print("dui le")
else:
    if guess_num > num:
       print("da le")
    else:
       print("xiao le")






