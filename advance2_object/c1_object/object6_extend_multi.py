"""
多继承
"""
class NFCReader:
    def nfc_read(self):
        print("NFC读取功能")
    def nfc_write(self):
        print("NFC写入功能")

class RemoteControl:
    def control(self):
        print("红外遥控")

class Phone:
    IMEI = None  # 序列号
    producer = None  # 厂商

    def call_by_4g(self):
        print("4g通话")

class XIAOMI(Phone, NFCReader, RemoteControl):
    pass

xiaomi = XIAOMI()
xiaomi.call_by_4g()
xiaomi.nfc_write()
xiaomi.control()