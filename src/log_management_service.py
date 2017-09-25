# -*- coding:utf-8 -*-
import os
import time
import datetime
__author__ = 'yangxin'


class LogManagementService(object):
    def __init__(self):
        pass

    @staticmethod
    def manage_log(input_log_file, output_log_file, data):
        # rename the input_log_file to yesterday
        os.rename(input_log_file, output_log_file)
        with open(input_log_file, "w") as input_log_file:
            input_log_file.write(data)
            input_log_file.close()

    def timers(self):
        while True:
            today = datetime.date.today()
            yesterday = today - datetime.timedelta(days=1)
            year_yes = str(yesterday)[0:4]
            month_yes = str(yesterday)[5:7]
            day_yes = str(yesterday)[8:10]
            year_today = str(today)[0:4]
            month_today = str(today)[5:7]
            day_today = str(today)[8:10]
            run_time = datetime.datetime(int(year_today), int(month_today), int(day_today), 0, 2, 59)
            now = datetime.datetime.now()
            if run_time < now < (run_time + datetime.timedelta(seconds=1)):
                print "it's time run"
                time.sleep(5)
                file_name = year_yes + month_yes + day_yes
                LogManagementService.manage_log("today_named log file path",
                                                "log content" + file_name + ".log", file_name)

if __name__ == '__main__':
    log_management_serivice = LogManagementService()
    log_management_serivice.timers()
