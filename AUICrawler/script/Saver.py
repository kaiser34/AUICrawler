# -*- coding:utf-8 -*-

import datetime
import os
import sys
import types
import HtmlMaker


reload(sys)
sys.setdefaultencoding('utf-8')

log_tag = os.path.basename(os.getcwd())


def save_crawler_log(log_path, log):
    log_file = open(log_path + '/CrawlerLog.txt', 'a')
    if type(log) is types.StringType:
        if "Step" in log:
            log_str = log_tag + " : " + str(datetime.datetime.now()) + "  " + log
        else:
            log_str = log_tag + " : " + str(datetime.datetime.now()) + "       - " + log
    else:
        log_str = log_tag + " : " + str(datetime.datetime.now()) + "       - " + str(log)
    print log_str
    log_file.write(log_str + '\n')
    log_file.close()


def save_crawler_log_both(plan_log_path, device_log_path, log):
    save_crawler_log(plan_log_path, log)
    save_crawler_log(device_log_path, log)


def save_crawl_result(plan, app):
    save_crawler_log(plan.logPath, "Step : Save crawl results . ")
    plan.resultHtml = HtmlMaker.mack_crawl_result_html(plan, app)
    result_file = open(plan.logPath + '/Result.html', 'w')
    result_file.write(plan.resultHtml)
    result_file.close()
