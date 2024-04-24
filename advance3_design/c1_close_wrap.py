"""
闭包：解决全局变量可能被修改的风险
"""
account_amount = 0


def atm(num, despoist=True):
    global account_amount
    if despoist:
        account_amount += num
        print(f"存款:+{num}, 账户余额{account_amount}")
    else:
        account_amount -= num
        print(f"存款:+{num}, 账户余额{account_amount}")


atm(300)
atm(300)
atm(100, False)

print("---------")


# 改为闭包代码
def account_create(init_amount=0):
    def atm(num, despoist=True):
        nonlocal init_amount
        if despoist:
            init_amount += num
            print(f"存款:+{num}, 账户余额{init_amount}")
        else:
            init_amount -= num
            print(f"存款:+{num}, 账户余额{init_amount}")

    return atm


atm1 = account_create(100)
atm1(300)
atm1(300)
atm1(100, False)
