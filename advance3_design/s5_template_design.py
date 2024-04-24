"""
需求：有多个类，完成不同的任务
要求统计他们各自完成任务的时间
"""
import time


class Task1:
    def job(self):
        start = time.time()
        time.sleep(1)
        print("耗时{}秒".format(time.time() - start))


class Task2:
    def job(self):
        start = time.time()
        time.sleep(1.2)
        print("耗时{}秒".format(time.time() - start))

if __name__ == '__main__':
    Task1().job()
    Task2().job()
