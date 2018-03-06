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
    pixel_1 = im_pixel[240, 715]
    pixel_2 = im_pixel[440, 715]
    pixel_3 = im_pixel[640, 715]
    pixel_4 = im_pixel[835, 715]
    pixel_5 = im_pixel[240, 925]
    pixel_6 = im_pixel[440, 925]
    pixel_7 = im_pixel[640, 925]
    pixel_8 = im_pixel[835, 925]
    pixel_9 = im_pixel[240, 1135]
    pixel_10= im_pixel[440, 1135]
    pixel_11= im_pixel[640, 1135]
    pixel_12= im_pixel[835, 1135]
    pixel_13= im_pixel[240, 1340]
    pixel_14= im_pixel[440, 1340]
    pixel_15= im_pixel[640, 1340]
    pixel_16= im_pixel[835, 1340]
    while True:
        if (250<pixel_1[0]<256 and 250<pixel_1[1]<256 and 250<pixel_1[2]<256):
            cmd = 'shell input tap 240 715'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.05)
        if (250<pixel_2[0]<256 and 250<pixel_2[1]<256 and 250<pixel_2[2]<256):
            cmd = 'shell input tap 440 715'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.05)
        if (250<pixel_3[0]<256 and 250<pixel_3[1]<256 and 250<pixel_3[2]<256):
            cmd = 'shell input tap 640 715'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.05)
        if (250<pixel_4[0]<256 and 250<pixel_4[1]<256 and 250<pixel_4[2]<256):
            cmd = 'shell input tap 835 715'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.05)
        if (250<pixel_5[0]<256 and 250<pixel_5[1]<256 and 250<pixel_5[2]<256):
            cmd = 'shell input tap 240 925'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.05)
        if (250<pixel_6[0]<256 and 250<pixel_6[1]<256 and 250<pixel_6[2]<256):
            cmd = 'shell input tap 440 925'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.05)
        if (250<pixel_7[0]<256 and 250<pixel_7[1]<256 and 250<pixel_7[2]<256):
            cmd = 'shell input tap 640 925'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.05)
        if (250<pixel_8[0]<256 and 250<pixel_8[1]<256 and 250<pixel_8[2]<256):
            cmd = 'shell input tap 835 925'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.05)
        if (250<pixel_9[0]<256 and 250<pixel_9[1]<256 and 250<pixel_9[2]<256):
            cmd = 'shell input tap 240 1135'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.05)
        if (250<pixel_10[0]<256 and 250<pixel_10[1]<256 and 250<pixel_10[2]<256):
            cmd = 'shell input tap 440 1135'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.05)
        if (250<pixel_11[0]<256 and 250<pixel_11[1]<256 and 250<pixel_11[2]<256):
            cmd = 'shell input tap 640 1135'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.05)
        if (250<pixel_12[0]<256 and 250<pixel_12[1]<256 and 250<pixel_12[2]<256):
            cmd = 'shell input tap 835 1135'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.05)
        if (250<pixel_13[0]<256 and 250<pixel_13[1]<256 and 250<pixel_13[2]<256):
            cmd = 'shell input tap 240 1340'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.05)
        if (250<pixel_14[0]<256 and 250<pixel_14[1]<256 and 250<pixel_14[2]<256):
            cmd = 'shell input tap 440 1340'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.05)
        if (250<pixel_15[0]<256 and 250<pixel_15[1]<256 and 250<pixel_15[2]<256):
            cmd = 'shell input tap 640 1340'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.05)
        if (250<pixel_16[0]<256 and 250<pixel_16[1]<256 and 250<pixel_16[2]<256):
            cmd = 'shell input tap 835 1340'
            print(cmd)
            adb.run(cmd)
            time.sleep(0.05)

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
