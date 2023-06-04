# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# File : lib__threading.py
# Author : yc0325lee
# Created : 2022-03-05 19:59:00 by lee2103
# Modified : 2022-03-05 19:59:00 by lee2103
# Description : 
# ----------------------------------------------------------------------------
import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working: %s" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join() # join으로 스레드가 종료될때까지 기다린다.

print("End")
