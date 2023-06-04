# vim: ft=python ts=4 sw=4 tw=999 expandtab
# ----------------------------------------------------------------------------
# File : lib__csv.py
# Description : 
# Author : yc0325lee
# Created : 2021-07-31 19:24:58 by lee2103
# Modified : 2021-07-31 19:24:58 by lee2103
# ----------------------------------------------------------------------------
import csv

filename = "train_neuralnet_train_loss.csv"
print("[info] writing {} ...".format(filename))
with open(filename, "w", newline="") as csvfile:
    csvWriter = csv.writer(csvfile)
    for i, val in enumerate(train_loss_list):
        csvWriter.writerow([i, val])

filename = "train_neuralnet_train_loss.csv"
print("[info] reading {} ...".format(filename))
with open(filename, "r", newline="") as csvfile:
    csvReader = csv.reader(csvfile)
    for row in csvReader:
        print("row=", row)
