# vim: ft=python ts=4 sw=4 tw=999 expandtab
# ----------------------------------------------------------------------------
# File : lib__turtle.py
# Author : yc0325lee
# Created : 2022-03-09 22:50:51 by lee2103
# Modified : 2022-03-09 22:50:51 by lee2103
# Description : 
# ----------------------------------------------------------------------------
import turtle as t
import time

t.home()
t.shape("square")

def go_to_somewhere(count, delay):
    for n in range(0, count):
        t.forward(25)
        time.sleep(delay)
    t.left(90)


for i in range(0, 10):
    go_to_somewhere(8, 0.01)

time.sleep(0.5)
