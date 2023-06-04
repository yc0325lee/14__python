#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=999 expandtab
# ----------------------------------------------------------------------------
# - file : interest.py
# - author : yc0325lee
# - created : 2023-01-25 19:30:00 by yc032
# - modified : 2023-01-25 19:30:00 by yc032
# - description : 
# ----------------------------------------------------------------------------
import os, os.path, sys
import random
import pickle
import numpy as np
np.random.seed(42)
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

rate = 0.003
initial = 10000000.0
total = initial
n_months = 1200 # 10-years

interests = list()
totals = list()
for month in range(n_months):
    principal = total
    interest = principal * rate
    total = principal + interest
    print('month[{:3d}]: principal= {:.3f}, interest= {:.3f}, total= {:.3f} ({:.2f}%)'.format(
        month, principal, interest, total, total/initial*100.0))
    interests.append(interest)
    totals.append(total)

months = list(range(n_months))

fig = plt.figure(figsize=(8.0, 12.0)) # default: [6.4, 4.8]
                                     # plt.rcParams["figure.figsize"]
plt.plot(months, interests)
plt.plot(months, totals)
plt.title('interests and totals')
plt.xlabel('month')
plt.ylabel('won')
plt.grid(linestyle='--')
plt.tight_layout() # adjust the padding between and around subplots
index = 0
filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
print('[info] saving image to {} ...'.format(filename))
plt.savefig(filename, bbox_inches="tight")
#plt.show()
plt.close()

# month[  1]: principal= 10000000.000, interest= 30000.000, total= 10030000.000 (100.30%)
# month[  2]: principal= 10030000.000, interest= 30090.000, total= 10060090.000 (100.60%)
# month[  3]: principal= 10060090.000, interest= 30180.270, total= 10090270.270 (100.90%)
# month[  4]: principal= 10090270.270, interest= 30270.811, total= 10120541.081 (101.21%)
# month[  5]: principal= 10120541.081, interest= 30361.623, total= 10150902.704 (101.51%)
# month[  6]: principal= 10150902.704, interest= 30452.708, total= 10181355.412 (101.81%)
# month[  7]: principal= 10181355.412, interest= 30544.066, total= 10211899.478 (102.12%)
# month[  8]: principal= 10211899.478, interest= 30635.698, total= 10242535.177 (102.43%)
# month[  9]: principal= 10242535.177, interest= 30727.606, total= 10273262.782 (102.73%)
# month[ 10]: principal= 10273262.782, interest= 30819.788, total= 10304082.571 (103.04%)
# month[ 11]: principal= 10304082.571, interest= 30912.248, total= 10334994.818 (103.35%)
# month[ 12]: principal= 10334994.818, interest= 31004.984, total= 10365999.803 (103.66%)
# month[ 13]: principal= 10365999.803, interest= 31097.999, total= 10397097.802 (103.97%)
# month[ 14]: principal= 10397097.802, interest= 31191.293, total= 10428289.096 (104.28%)
# month[ 15]: principal= 10428289.096, interest= 31284.867, total= 10459573.963 (104.60%)
# month[ 16]: principal= 10459573.963, interest= 31378.722, total= 10490952.685 (104.91%)
# month[ 17]: principal= 10490952.685, interest= 31472.858, total= 10522425.543 (105.22%)
# month[ 18]: principal= 10522425.543, interest= 31567.277, total= 10553992.820 (105.54%)
# month[ 19]: principal= 10553992.820, interest= 31661.978, total= 10585654.798 (105.86%)
# month[ 20]: principal= 10585654.798, interest= 31756.964, total= 10617411.762 (106.17%)
# month[ 21]: principal= 10617411.762, interest= 31852.235, total= 10649263.998 (106.49%)
# month[ 22]: principal= 10649263.998, interest= 31947.792, total= 10681211.790 (106.81%)
# month[ 23]: principal= 10681211.790, interest= 32043.635, total= 10713255.425 (107.13%)
# month[ 24]: principal= 10713255.425, interest= 32139.766, total= 10745395.191 (107.45%)
# month[ 25]: principal= 10745395.191, interest= 32236.186, total= 10777631.377 (107.78%)
# month[ 26]: principal= 10777631.377, interest= 32332.894, total= 10809964.271 (108.10%)
# month[ 27]: principal= 10809964.271, interest= 32429.893, total= 10842394.164 (108.42%)
# month[ 28]: principal= 10842394.164, interest= 32527.182, total= 10874921.346 (108.75%)
# month[ 29]: principal= 10874921.346, interest= 32624.764, total= 10907546.110 (109.08%)
# month[ 30]: principal= 10907546.110, interest= 32722.638, total= 10940268.749 (109.40%)
# month[ 31]: principal= 10940268.749, interest= 32820.806, total= 10973089.555 (109.73%)
# month[ 32]: principal= 10973089.555, interest= 32919.269, total= 11006008.824 (110.06%)
# month[ 33]: principal= 11006008.824, interest= 33018.026, total= 11039026.850 (110.39%)
# month[ 34]: principal= 11039026.850, interest= 33117.081, total= 11072143.931 (110.72%)
# month[ 35]: principal= 11072143.931, interest= 33216.432, total= 11105360.362 (111.05%)
# month[ 36]: principal= 11105360.362, interest= 33316.081, total= 11138676.444 (111.39%)
# month[ 37]: principal= 11138676.444, interest= 33416.029, total= 11172092.473 (111.72%)
# month[ 38]: principal= 11172092.473, interest= 33516.277, total= 11205608.750 (112.06%)
# month[ 39]: principal= 11205608.750, interest= 33616.826, total= 11239225.577 (112.39%)
# month[ 40]: principal= 11239225.577, interest= 33717.677, total= 11272943.253 (112.73%)
# month[ 41]: principal= 11272943.253, interest= 33818.830, total= 11306762.083 (113.07%)
# month[ 42]: principal= 11306762.083, interest= 33920.286, total= 11340682.369 (113.41%)
# month[ 43]: principal= 11340682.369, interest= 34022.047, total= 11374704.416 (113.75%)
# month[ 44]: principal= 11374704.416, interest= 34124.113, total= 11408828.530 (114.09%)
# month[ 45]: principal= 11408828.530, interest= 34226.486, total= 11443055.015 (114.43%)
# month[ 46]: principal= 11443055.015, interest= 34329.165, total= 11477384.180 (114.77%)
# month[ 47]: principal= 11477384.180, interest= 34432.153, total= 11511816.333 (115.12%)
# month[ 48]: principal= 11511816.333, interest= 34535.449, total= 11546351.782 (115.46%)
# month[ 49]: principal= 11546351.782, interest= 34639.055, total= 11580990.837 (115.81%)
# month[ 50]: principal= 11580990.837, interest= 34742.973, total= 11615733.810 (116.16%)
# month[ 51]: principal= 11615733.810, interest= 34847.201, total= 11650581.011 (116.51%)
# month[ 52]: principal= 11650581.011, interest= 34951.743, total= 11685532.754 (116.86%)
# month[ 53]: principal= 11685532.754, interest= 35056.598, total= 11720589.352 (117.21%)
# month[ 54]: principal= 11720589.352, interest= 35161.768, total= 11755751.120 (117.56%)
# month[ 55]: principal= 11755751.120, interest= 35267.253, total= 11791018.374 (117.91%)
# month[ 56]: principal= 11791018.374, interest= 35373.055, total= 11826391.429 (118.26%)
# month[ 57]: principal= 11826391.429, interest= 35479.174, total= 11861870.603 (118.62%)
# month[ 58]: principal= 11861870.603, interest= 35585.612, total= 11897456.215 (118.97%)
# month[ 59]: principal= 11897456.215, interest= 35692.369, total= 11933148.584 (119.33%)
# month[ 60]: principal= 11933148.584, interest= 35799.446, total= 11968948.029 (119.69%)
# month[ 61]: principal= 11968948.029, interest= 35906.844, total= 12004854.873 (120.05%)
# month[ 62]: principal= 12004854.873, interest= 36014.565, total= 12040869.438 (120.41%)
# month[ 63]: principal= 12040869.438, interest= 36122.608, total= 12076992.046 (120.77%)
# month[ 64]: principal= 12076992.046, interest= 36230.976, total= 12113223.023 (121.13%)
# month[ 65]: principal= 12113223.023, interest= 36339.669, total= 12149562.692 (121.50%)
# month[ 66]: principal= 12149562.692, interest= 36448.688, total= 12186011.380 (121.86%)
# month[ 67]: principal= 12186011.380, interest= 36558.034, total= 12222569.414 (122.23%)
# month[ 68]: principal= 12222569.414, interest= 36667.708, total= 12259237.122 (122.59%)
# month[ 69]: principal= 12259237.122, interest= 36777.711, total= 12296014.833 (122.96%)
# month[ 70]: principal= 12296014.833, interest= 36888.045, total= 12332902.878 (123.33%)
# month[ 71]: principal= 12332902.878, interest= 36998.709, total= 12369901.587 (123.70%)
# month[ 72]: principal= 12369901.587, interest= 37109.705, total= 12407011.291 (124.07%)
# month[ 73]: principal= 12407011.291, interest= 37221.034, total= 12444232.325 (124.44%)
# month[ 74]: principal= 12444232.325, interest= 37332.697, total= 12481565.022 (124.82%)
# month[ 75]: principal= 12481565.022, interest= 37444.695, total= 12519009.717 (125.19%)
# month[ 76]: principal= 12519009.717, interest= 37557.029, total= 12556566.746 (125.57%)
# month[ 77]: principal= 12556566.746, interest= 37669.700, total= 12594236.447 (125.94%)
# month[ 78]: principal= 12594236.447, interest= 37782.709, total= 12632019.156 (126.32%)
# month[ 79]: principal= 12632019.156, interest= 37896.057, total= 12669915.213 (126.70%)
# month[ 80]: principal= 12669915.213, interest= 38009.746, total= 12707924.959 (127.08%)
# month[ 81]: principal= 12707924.959, interest= 38123.775, total= 12746048.734 (127.46%)
# month[ 82]: principal= 12746048.734, interest= 38238.146, total= 12784286.880 (127.84%)
# month[ 83]: principal= 12784286.880, interest= 38352.861, total= 12822639.741 (128.23%)
# month[ 84]: principal= 12822639.741, interest= 38467.919, total= 12861107.660 (128.61%)
# month[ 85]: principal= 12861107.660, interest= 38583.323, total= 12899690.983 (129.00%)
# month[ 86]: principal= 12899690.983, interest= 38699.073, total= 12938390.056 (129.38%)
# month[ 87]: principal= 12938390.056, interest= 38815.170, total= 12977205.226 (129.77%)
# month[ 88]: principal= 12977205.226, interest= 38931.616, total= 13016136.842 (130.16%)
# month[ 89]: principal= 13016136.842, interest= 39048.411, total= 13055185.252 (130.55%)
# month[ 90]: principal= 13055185.252, interest= 39165.556, total= 13094350.808 (130.94%)
# month[ 91]: principal= 13094350.808, interest= 39283.052, total= 13133633.861 (131.34%)
# month[ 92]: principal= 13133633.861, interest= 39400.902, total= 13173034.762 (131.73%)
# month[ 93]: principal= 13173034.762, interest= 39519.104, total= 13212553.866 (132.13%)
# month[ 94]: principal= 13212553.866, interest= 39637.662, total= 13252191.528 (132.52%)
# month[ 95]: principal= 13252191.528, interest= 39756.575, total= 13291948.103 (132.92%)
# month[ 96]: principal= 13291948.103, interest= 39875.844, total= 13331823.947 (133.32%)
# month[ 97]: principal= 13331823.947, interest= 39995.472, total= 13371819.419 (133.72%)
# month[ 98]: principal= 13371819.419, interest= 40115.458, total= 13411934.877 (134.12%)
# month[ 99]: principal= 13411934.877, interest= 40235.805, total= 13452170.682 (134.52%)
# month[100]: principal= 13452170.682, interest= 40356.512, total= 13492527.194 (134.93%)
# month[101]: principal= 13492527.194, interest= 40477.582, total= 13533004.775 (135.33%)
# month[102]: principal= 13533004.775, interest= 40599.014, total= 13573603.790 (135.74%)
# month[103]: principal= 13573603.790, interest= 40720.811, total= 13614324.601 (136.14%)
# month[104]: principal= 13614324.601, interest= 40842.974, total= 13655167.575 (136.55%)
# month[105]: principal= 13655167.575, interest= 40965.503, total= 13696133.077 (136.96%)
# month[106]: principal= 13696133.077, interest= 41088.399, total= 13737221.477 (137.37%)
# month[107]: principal= 13737221.477, interest= 41211.664, total= 13778433.141 (137.78%)
# month[108]: principal= 13778433.141, interest= 41335.299, total= 13819768.441 (138.20%)
# month[109]: principal= 13819768.441, interest= 41459.305, total= 13861227.746 (138.61%)
# month[110]: principal= 13861227.746, interest= 41583.683, total= 13902811.429 (139.03%)
# month[111]: principal= 13902811.429, interest= 41708.434, total= 13944519.863 (139.45%)
# month[112]: principal= 13944519.863, interest= 41833.560, total= 13986353.423 (139.86%)
# month[113]: principal= 13986353.423, interest= 41959.060, total= 14028312.483 (140.28%)
# month[114]: principal= 14028312.483, interest= 42084.937, total= 14070397.421 (140.70%)
# month[115]: principal= 14070397.421, interest= 42211.192, total= 14112608.613 (141.13%)
# month[116]: principal= 14112608.613, interest= 42337.826, total= 14154946.439 (141.55%)
# month[117]: principal= 14154946.439, interest= 42464.839, total= 14197411.278 (141.97%)
# month[118]: principal= 14197411.278, interest= 42592.234, total= 14240003.512 (142.40%)
# month[119]: principal= 14240003.512, interest= 42720.011, total= 14282723.522 (142.83%)
# month[120]: principal= 14282723.522, interest= 42848.171, total= 14325571.693 (143.26%)
