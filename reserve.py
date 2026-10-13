# 法定存款准备金计算器
# 货币银行学
def required_reserve(deposit, rate):
    res = deposit * rate
    return round(res,2)

if __name__ == "__main__":
    print("====法定存款准备金计算器====")
    D = float(input("存款总额："))
    r = float(input("法定存款准备金率（小数，如10%填0.1）："))
    result = required_reserve(D, r)
    print(f"\n法定存款准备金 = {result}")
