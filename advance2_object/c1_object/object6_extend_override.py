class Phone:
    IMEI = None  # 序列号
    producer = None  # 厂商

    def call_by_4g(self):
        print("父类4g通话")

class XIAOMI(Phone):
    def call_by_4g(self):
        print("XIAOMI 4g通话")
        super().call_by_4g()

xiaomi = XIAOMI()
xiaomi.call_by_4g()
