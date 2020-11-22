# 做了改进：可以提示用户输入的数字比目标数字大了还是小了
temp = input("请输入一个数字：")
i = int(temp)
if i == 9:
    print('猜对了')
else:
    if i > 9:
        print("大了大了")
    else:
        print("小了小了")
print("游戏结束")
