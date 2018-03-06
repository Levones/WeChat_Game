# -*- coding: utf-8 -*-
import math
import re
import random
import sys
import time
from PIL import Image
from six.moves import input

if sys.version_info.major != 3:
    print('请使用Python3')
    exit(1)
try:
    from common import debug, config, screenshot, UnicodeStreamFilter
    from common.auto_adb import auto_adb
except Exception as ex:
    print(ex)
    exit(1)
adb = auto_adb()
DEBUG_SWITCH = False
adb.test_device()


def main():
    print('激活窗口并按 CONTROL + C 组合键退出')
    debug.dump_device_info()
    screenshot.check_screenshot()
    i=0
    press_time = 20
    press_time = int(press_time)
    im = screenshot.pull_screenshot()
    w, h = im.size
    im_pixel = im.load()
    pixel_1 = im_pixel[220, 695]
    pixel_2 = im_pixel[350, 695]
    pixel_3 = im_pixel[470, 695]
    pixel_4 = im_pixel[595, 695]
    pixel_5 = im_pixel[730, 695]
    pixel_6 = im_pixel[858, 695]
    pixel_7 = im_pixel[220, 835]
    pixel_8 = im_pixel[350, 835]
    pixel_9 = im_pixel[470, 835]
    pixel_10 = im_pixel[595, 835]
    pixel_11 = im_pixel[730, 835]
    pixel_12 = im_pixel[858, 835]
    pixel_13 = im_pixel[220, 975]
    pixel_14 = im_pixel[350, 975]
    pixel_15 = im_pixel[470, 975]
    pixel_16 = im_pixel[595, 975]
    pixel_17 = im_pixel[730, 975]
    pixel_18 = im_pixel[858, 975]
    pixel_19 = im_pixel[220, 1110]
    pixel_20 = im_pixel[350, 1110]
    pixel_21 = im_pixel[470, 1110]
    pixel_22 = im_pixel[595, 1110]
    pixel_23 = im_pixel[730, 1110]
    pixel_24 = im_pixel[858, 1110]
    pixel_25 = im_pixel[220, 1250]
    pixel_26 = im_pixel[350, 1250]
    pixel_27 = im_pixel[470, 1250]
    pixel_28 = im_pixel[595, 1250]
    pixel_29 = im_pixel[730, 1250]
    pixel_30 = im_pixel[858, 1250]
    pixel_31 = im_pixel[220, 1390]
    pixel_32 = im_pixel[350, 1390]
    pixel_33 = im_pixel[470, 1390]
    pixel_34 = im_pixel[595, 1390]
    pixel_35 = im_pixel[730, 1390]
    pixel_36 = im_pixel[858, 1390]
    while True:
        if (250<pixel_1[0]<256 and 250<pixel_1[1]<256 and 250<pixel_1[2]<256):
            cmd = 'shell input tap 220 695'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_2[0]<256 and 250<pixel_2[1]<256 and 250<pixel_2[2]<256):
            cmd = 'shell input tap 350 695'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_3[0]<256 and 250<pixel_3[1]<256 and 250<pixel_3[2]<256):
            cmd = 'shell input tap 470 695'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_4[0]<256 and 250<pixel_4[1]<256 and 250<pixel_4[2]<256):
            cmd = 'shell input tap 595 695'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_5[0]<256 and 250<pixel_5[1]<256 and 250<pixel_5[2]<256):
            cmd = 'shell input tap 730 695'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_6[0]<256 and 250<pixel_6[1]<256 and 250<pixel_6[2]<256):
            cmd = 'shell input tap 858 695'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_7[0]<256 and 250<pixel_7[1]<256 and 250<pixel_7[2]<256):
            cmd = 'shell input tap 220 835'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_8[0]<256 and 250<pixel_8[1]<256 and 250<pixel_8[2]<256):
            cmd = 'shell input tap 350 835'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_9[0]<256 and 250<pixel_9[1]<256 and 250<pixel_9[2]<256):
            cmd = 'shell input tap 470 835'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_10[0]<256 and 250<pixel_10[1]<256 and 250<pixel_10[2]<256):
            cmd = 'shell input tap 595 835'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_11[0]<256 and 250<pixel_11[1]<256 and 250<pixel_11[2]<256):
            cmd = 'shell input tap 730 835'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_12[0]<256 and 250<pixel_12[1]<256 and 250<pixel_12[2]<256):
            cmd = 'shell input tap 858 835'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_13[0]<256 and 250<pixel_13[1]<256 and 250<pixel_13[2]<256):
            cmd = 'shell input tap 220 975'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_14[0]<256 and 250<pixel_14[1]<256 and 250<pixel_14[2]<256):
            cmd = 'shell input tap 350 975'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_15[0]<256 and 250<pixel_15[1]<256 and 250<pixel_15[2]<256):
            cmd = 'shell input tap 470 975'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_16[0]<256 and 250<pixel_16[1]<256 and 250<pixel_16[2]<256):
            cmd = 'shell input tap 595 975'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_17[0]<256 and 250<pixel_17[1]<256 and 250<pixel_17[2]<256):
            cmd = 'shell input tap 730 975'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_18[0]<256 and 250<pixel_18[1]<256 and 250<pixel_18[2]<256):
            cmd = 'shell input tap 858 975'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_19[0]<256 and 250<pixel_19[1]<256 and 250<pixel_19[2]<256):
            cmd = 'shell input tap 220 1110'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_20[0]<256 and 250<pixel_20[1]<256 and 250<pixel_20[2]<256):
            cmd = 'shell input tap 350 1110'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_21[0]<256 and 250<pixel_21[1]<256 and 250<pixel_21[2]<256):
            cmd = 'shell input tap 470 1110'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_22[0]<256 and 250<pixel_22[1]<256 and 250<pixel_22[2]<256):
            cmd = 'shell input tap 595 1110'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_23[0]<256 and 250<pixel_23[1]<256 and 250<pixel_23[2]<256):
            cmd = 'shell input tap 730 1110'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_24[0]<256 and 250<pixel_24[1]<256 and 250<pixel_24[2]<256):
            cmd = 'shell input tap 858 1110'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_25[0]<256 and 250<pixel_25[1]<256 and 250<pixel_25[2]<256):
            cmd = 'shell input tap 220 1250'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_26[0]<256 and 250<pixel_26[1]<256 and 250<pixel_26[2]<256):
            cmd = 'shell input tap 350 1250'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_27[0]<256 and 250<pixel_27[1]<256 and 250<pixel_27[2]<256):
            cmd = 'shell input tap 470 1250'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_28[0]<256 and 250<pixel_28[1]<256 and 250<pixel_28[2]<256):
            cmd = 'shell input tap 595 1250'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_29[0]<256 and 250<pixel_29[1]<256 and 250<pixel_29[2]<256):
            cmd = 'shell input tap 730 1250'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_30[0]<256 and 250<pixel_30[1]<256 and 250<pixel_30[2]<256):
            cmd = 'shell input tap 858 1250'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_31[0]<256 and 250<pixel_31[1]<256 and 250<pixel_31[2]<256):
            cmd = 'shell input tap 220 1390'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_32[0]<256 and 250<pixel_32[1]<256 and 250<pixel_32[2]<256):
            cmd = 'shell input tap 350 1390'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_33[0]<256 and 250<pixel_33[1]<256 and 250<pixel_33[2]<256):
            cmd = 'shell input tap 470 1390'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_34[0]<256 and 250<pixel_34[1]<256 and 250<pixel_34[2]<256):
            cmd = 'shell input tap 595 1390'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_35[0]<256 and 250<pixel_35[1]<256 and 250<pixel_35[2]<256):
            cmd = 'shell input tap 730 1390'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)
        if (250<pixel_36[0]<256 and 250<pixel_36[1]<256 and 250<pixel_36[2]<256):
            cmd = 'shell input tap 858 1390'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.01)

        if DEBUG_SWITCH:
            debug.save_debug_screenshot(ts, im, piece_x,
                                        piece_y, board_x, board_y)
            debug.backup_screenshot(ts)
        im.close()
        i += 1


def yes_or_no():
    while True:
        yes_or_no = str(input('确定开始？[y/n]:'))
        if yes_or_no == 'y':
            break
        else:
            print('请重新输入')

if __name__ == '__main__':
    try:
        yes_or_no()
        main()
    except KeyboardInterrupt:
        adb.run('kill-server')
        exit(0)
