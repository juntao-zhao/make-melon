"""

-*- coding: utf-8 -*-

@Author  : ZHAO Juntao
@Time    : 3/16/2021 11:04 PM

"""

import os
import sys
import time
import random
import numpy as np
from cv2 import cv2
from engine import Engine
from console import *
import pandas as pd
import csv


def clean(filenames):
    if not isinstance(filenames, list):
        filenames = [filenames]
    for filename in filenames:
        if os.path.exists(filename):
            os.remove(filename)


def agent(**kwargs):
    # TODO: implement the agent function here
    action_num = kwargs["action_num"]
    action = random.randint(0, action_num - 1)
    # action = kwargs["action"] - 1
    return action


def main(epoch=10):
    # engine init
    timeout_cnt = 0
    engine = Engine()
    time.sleep(2)

    '''action from 1 to 16 iteratively'''
    # add for loop here
    for k in range(15):

        '''train iteratively'''
        for i in range(epoch):
            print(BLUE + '[INFO] start {} / {} epoch.'.format(i + 1, epoch) + RESET)

            '''wait for start'''
            while not engine.match_log('GameStart'):
                time.sleep(1)
                timeout_cnt += 1
                if timeout_cnt > 10:
                    print(RED + '[ERROR] engine cannot detect the game start signal.' + RESET)
                    sys.exit(-1)
            print(GREEN + '[INFO] engine detect the game start signal.' + RESET)

            '''train within an epoch'''
            while True:
                is_gameover, img = engine.wait_stable(thresh=0.001, timeout=10)
                state = engine.get_state()

                score = state['score']
                frame = state['frame']

                if is_gameover:
                    print(YELLOW + '[INFO] game over: score = {} in frame {}'.format(score, frame) + RESET)
                    break

                '''the agent make decision to choose one action each step'''
                action_num = 16
                action = agent(action_num=action_num, score=score, frame=frame, flag=is_gameover, image=img)

                engine.pick_action(action)

            engine.reset_state()


if __name__ == '__main__':
    main(epoch=20)
    clean(['_cap_tmp.png', '_tmp_t1.png', '_tmp_t2.png', 'diff_img.png'])


