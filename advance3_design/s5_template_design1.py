"""
需求：有多个类，完成不同的任务
要求统计他们各自完成任务的时间
"""
import time

from abc import ABC, abstractmethod


class AbsTractTask(ABC):
    @abstractmethod
    def job(self):
        """
        计算统计时间
        :return:
        """

    def call_time(self):
        start_time = time.time()
        self.job()
        print("执行任务耗时{}".format(time.time() - start_time))


class Task1(AbsTractTask):
    def job(self):
        time.sleep(1)


class Task2(AbsTractTask):
    def job(self):
        time.sleep(1.2)


if __name__ == '__main__':
    Task1().call_time()
    Task2().call_time()
