# 二项分布计算


# 这是一个阶乘方法
def factorial(num):
    if num >= 0:
        if num == 0 or num == 1:
            return 1
        return num * factorial(num - 1)
    else:
        print("你输入的参数不合法")


# print(factorial(4))

# def get_time(time):

# 计算二项分布概率的方法
# time--进行试验的次数
# probability--试验成功的概率
# 计算公式: C(n, m) = n! / m! * (n - m)!
def bernoulli(time, probability):
    dic = {}
    for i in range(0, time + 1):
        dic["C({}, {})".format(time, i)] = \
            (factorial(time) / (factorial(i) * factorial(time - i))
             * (probability ** i) * ((1 - probability) ** (time - i)))
    return dic  # 以字典的形势返回
