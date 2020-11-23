# 做了改进：使用随机数作为目标结果
# 引入一个模块 random
import random
# 调用random模块的方法获取一个1~10的随机数
secret = random.randint(1, 10)
print("====== 猜数字小游戏 ======")
temp = input("请输入一个数字：")
i = int(temp)
if i == secret:
    print("猜对了")
chance = 3
while i != secret and chance > 1:
    chance = chance - 1
    if i < secret:
        # 注意，此处不能直接把字符串和整型做拼接，否则会报错，要先使用str函数把整型转换为字符串类型
        temp = input("小了小了，您还有" + str(chance) + "次机会，请重新输入一个数字：")
    else:
        temp = input("大了大了，您还有" + str(chance) + "次机会，请重新输入一个数字：")
    i = int(temp)
    if i == secret:
        print("猜对了")
print("游戏结束")
