# vim: ft=python ts=4 sw=4 tw=999 expandtab
# ----------------------------------------------------------------------------
# File : lib__json.py
# Description : 
# Author : yc0325lee
# Created : 2021-07-24 22:55:34 by lee2103
# Modified : 2021-07-24 22:55:34 by lee2103
# ----------------------------------------------------------------------------
import json

# saving structured data with json
data = [1, 'simple', 'list']

with open("data.json", "w") as outFile: # dumping
    json.dump(data, outFile)

with open("data.json", "r") as inFile: # re-loading
    data = json.load(inFile)
