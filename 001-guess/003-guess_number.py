# 做了改进：不用每猜错一次都需要重新运行游戏
print("====== 猜数字小游戏 ======")
temp = input("请输入一个数字：")
i = int(temp)
while i != 9:
    if i < 9:
        temp = input("小了小了，请重新输入一个数字：")
    else:
        temp = input("大了大了，请重新输入一个数字：")
    i = int(temp)
print("猜对了")
print("游戏结束")
