import random
num = random.randint(1,100)
print("cai shu zi")
count = 0

flag = True
while flag:
    num_1 = int(input("请输入一个数字："))
    count += 1

    if num_1 == num:

        print("猜对了")
        flag = False
    else:
        if num_1 > num:
            print("大了")

        else:
            print("小了")

print(f"猜了{count}次")
