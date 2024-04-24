class Phone:
    IMEI = None  # 序列号
    producer = None  # 厂商

    def call_by_4g(self):
        print("4g通话")

class XIAOMI(Phone):
    def call_by_5g(self):
        print("5g通话")

xiaomi = XIAOMI()
xiaomi.call_by_4g()
xiaomi.call_by_5g()
