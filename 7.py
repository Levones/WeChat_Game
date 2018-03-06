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
    im = screenshot.pull_screenshot()
    w, h = im.size
    im_pixel = im.load()
    pixel_1 = im_pixel[215, 690]
    pixel_2 = im_pixel[320, 690]
    pixel_3 = im_pixel[430, 690]
    pixel_4 = im_pixel[535, 690]
    pixel_5 = im_pixel[645, 690]
    pixel_6 = im_pixel[755, 690]
    pixel_7 = im_pixel[865, 690]
    pixel_8 = im_pixel[215, 810]
    pixel_9 = im_pixel[320, 810]
    pixel_10 = im_pixel[430, 810]
    pixel_11 = im_pixel[535, 810]
    pixel_12 = im_pixel[645, 810]
    pixel_13 = im_pixel[755, 810]
    pixel_14 = im_pixel[865, 810]
    pixel_15 = im_pixel[215, 930]
    pixel_16 = im_pixel[320, 930]
    pixel_17 = im_pixel[430, 930]
    pixel_18 = im_pixel[535, 930]
    pixel_19 = im_pixel[645, 930]
    pixel_20 = im_pixel[755, 930]
    pixel_21 = im_pixel[865, 930]
    pixel_22 = im_pixel[215, 1050]
    pixel_23 = im_pixel[320, 1050]
    pixel_24= im_pixel[430, 1050]
    pixel_25 = im_pixel[535, 1050]
    pixel_26 = im_pixel[645, 1050]
    pixel_27 = im_pixel[755, 1050]
    pixel_28 = im_pixel[865, 1050]
    pixel_29 = im_pixel[215, 1180]
    pixel_30 = im_pixel[320, 1180]
    pixel_31 = im_pixel[430, 1180]
    pixel_32 = im_pixel[535, 1180]
    pixel_33 = im_pixel[645, 1180]
    pixel_34 = im_pixel[755, 1180]
    pixel_35 = im_pixel[865, 1180]
    pixel_36 = im_pixel[215, 1290]
    pixel_37 = im_pixel[320, 1290]
    pixel_38 = im_pixel[430, 1290]
    pixel_39 = im_pixel[535, 1290]
    pixel_40 = im_pixel[645, 1290]
    pixel_41 = im_pixel[755, 1290]
    pixel_42 = im_pixel[865, 1290]
    pixel_43 = im_pixel[215, 1410]
    pixel_44 = im_pixel[320, 1410]
    pixel_45 = im_pixel[430, 1410]
    pixel_46 = im_pixel[535, 1410]
    pixel_47 = im_pixel[645, 1410]
    pixel_48 = im_pixel[755, 1410]
    pixel_49 = im_pixel[865, 1410]
    
    
    while True:
        if (250<pixel_1[0]<256 and 250<pixel_1[1]<256 and 250<pixel_1[2]<256):
            cmd = 'shell input tap 215 690'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_2[0]<256 and 250<pixel_2[1]<256 and 250<pixel_2[2]<256):
            cmd = 'shell input tap 320 690'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_3[0]<256 and 250<pixel_3[1]<256 and 250<pixel_3[2]<256):
            cmd = 'shell input tap 430 690'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_4[0]<256 and 250<pixel_4[1]<256 and 250<pixel_4[2]<256):
            cmd = 'shell input tap 535 690'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_5[0]<256 and 250<pixel_5[1]<256 and 250<pixel_5[2]<256):
            cmd = 'shell input tap 645 690'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_6[0]<256 and 250<pixel_6[1]<256 and 250<pixel_6[2]<256):
            cmd = 'shell input tap 755 690'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_7[0]<256 and 250<pixel_7[1]<256 and 250<pixel_7[2]<256):
            cmd = 'shell input tap 865 690'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_8[0]<256 and 250<pixel_8[1]<256 and 250<pixel_8[2]<256):
            cmd = 'shell input tap 215 810'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_9[0]<256 and 250<pixel_9[1]<256 and 250<pixel_9[2]<256):
            cmd = 'shell input tap 320 810'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_10[0]<256 and 250<pixel_10[1]<256 and 250<pixel_10[2]<256):
            cmd = 'shell input tap 430 810'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_11[0]<256 and 250<pixel_11[1]<256 and 250<pixel_11[2]<256):
            cmd = 'shell input tap 535 810'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_12[0]<256 and 250<pixel_12[1]<256 and 250<pixel_12[2]<256):
            cmd = 'shell input tap 645 810'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_13[0]<256 and 250<pixel_13[1]<256 and 250<pixel_13[2]<256):
            cmd = 'shell input tap 755 810'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_14[0]<256 and 250<pixel_14[1]<256 and 250<pixel_14[2]<256):
            cmd = 'shell input tap 865 810'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_15[0]<256 and 250<pixel_15[1]<256 and 250<pixel_15[2]<256):
            cmd = 'shell input tap 215 930'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_16[0]<256 and 250<pixel_16[1]<256 and 250<pixel_16[2]<256):
            cmd = 'shell input tap 320 930'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_17[0]<256 and 250<pixel_17[1]<256 and 250<pixel_17[2]<256):
            cmd = 'shell input tap 430 930'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_18[0]<256 and 250<pixel_18[1]<256 and 250<pixel_18[2]<256):
            cmd = 'shell input tap 535 930'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_19[0]<256 and 250<pixel_19[1]<256 and 250<pixel_19[2]<256):
            cmd = 'shell input tap 645 930'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_20[0]<256 and 250<pixel_20[1]<256 and 250<pixel_20[2]<256):
            cmd = 'shell input tap 755 930'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_21[0]<256 and 250<pixel_21[1]<256 and 250<pixel_21[2]<256):
            cmd = 'shell input tap 865 930'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_22[0]<256 and 250<pixel_22[1]<256 and 250<pixel_22[2]<256):
            cmd = 'shell input tap 215 1050'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_23[0]<256 and 250<pixel_23[1]<256 and 250<pixel_23[2]<256):
            cmd = 'shell input tap 320 1050'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_24[0]<256 and 250<pixel_24[1]<256 and 250<pixel_24[2]<256):
            cmd = 'shell input tap 430 1050'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_25[0]<256 and 250<pixel_25[1]<256 and 250<pixel_25[2]<256):
            cmd = 'shell input tap 535 1050'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_26[0]<256 and 250<pixel_26[1]<256 and 250<pixel_26[2]<256):
            cmd = 'shell input tap 645 1050'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_27[0]<256 and 250<pixel_27[1]<256 and 250<pixel_27[2]<256):
            cmd = 'shell input tap 755 1050'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_28[0]<256 and 250<pixel_28[1]<256 and 250<pixel_28[2]<256):
            cmd = 'shell input tap 865 1050'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_29[0]<256 and 250<pixel_29[1]<256 and 250<pixel_29[2]<256):
            cmd = 'shell input tap 215 1180'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_30[0]<256 and 250<pixel_30[1]<256 and 250<pixel_30[2]<256):
            cmd = 'shell input tap 320 1180'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_31[0]<256 and 250<pixel_31[1]<256 and 250<pixel_31[2]<256):
            cmd = 'shell input tap 430 1180'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_32[0]<256 and 250<pixel_32[1]<256 and 250<pixel_32[2]<256):
            cmd = 'shell input tap 535 1180'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_33[0]<256 and 250<pixel_33[1]<256 and 250<pixel_33[2]<256):
            cmd = 'shell input tap 645 1180'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_34[0]<256 and 250<pixel_34[1]<256 and 250<pixel_34[2]<256):
            cmd = 'shell input tap 755 1180'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_35[0]<256 and 250<pixel_35[1]<256 and 250<pixel_35[2]<256):
            cmd = 'shell input tap 865 1180'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_36[0]<256 and 250<pixel_36[1]<256 and 250<pixel_36[2]<256):
            cmd = 'shell input tap 215 1290'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_37[0]<256 and 250<pixel_37[1]<256 and 250<pixel_37[2]<256):
            cmd = 'shell input tap 320 1290'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_38[0]<256 and 250<pixel_38[1]<256 and 250<pixel_38[2]<256):
            cmd = 'shell input tap 430 1290'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_39[0]<256 and 250<pixel_39[1]<256 and 250<pixel_39[2]<256):
            cmd = 'shell input tap 535 1290'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_40[0]<256 and 250<pixel_40[1]<256 and 250<pixel_40[2]<256):
            cmd = 'shell input tap 645 1290'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_41[0]<256 and 250<pixel_41[1]<256 and 250<pixel_41[2]<256):
            cmd = 'shell input tap 755 1290'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_42[0]<256 and 250<pixel_42[1]<256 and 250<pixel_42[2]<256):
            cmd = 'shell input tap 865 1290'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_43[0]<256 and 250<pixel_43[1]<256 and 250<pixel_43[2]<256):
            cmd = 'shell input tap 215 1410'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_44[0]<256 and 250<pixel_44[1]<256 and 250<pixel_44[2]<256):
            cmd = 'shell input tap 320 1410'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_45[0]<256 and 250<pixel_45[1]<256 and 250<pixel_45[2]<256):
            cmd = 'shell input tap 430 1410'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_46[0]<256 and 250<pixel_46[1]<256 and 250<pixel_46[2]<256):
            cmd = 'shell input tap 535 1410'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_47[0]<256 and 250<pixel_47[1]<256 and 250<pixel_47[2]<256):
            cmd = 'shell input tap 645 1410'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_48[0]<256 and 250<pixel_48[1]<256 and 250<pixel_48[2]<256):
            cmd = 'shell input tap 755 1410'
            print(cmd)
            adb.run(cmd)
        if (250<pixel_49[0]<256 and 250<pixel_49[1]<256 and 250<pixel_49[2]<256):
            cmd = 'shell input tap 865 1410'
            print(cmd)
            adb.run(cmd)

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
