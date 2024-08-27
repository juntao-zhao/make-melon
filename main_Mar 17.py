"""

-*- coding: utf-8 -*-

@Author  : ZHAO Juntao
@Time    : 3/18/2021 1:04 AM

"""
import os
import sys
import time
import random
import numpy as np
from cv2 import cv2
from engine import Engine
from console import *
import csv


def clean(filenames):
    if not isinstance(filenames, list):
        filenames = [filenames]
    for filename in filenames:
        if os.path.exists(filename):
            os.remove(filename)


def agent(**kwargs):
    # TODO: implement the agent function here
    # action_num = kwargs["action_num"]
    # action = random.randint(0, action_num-1)
    action = kwargs["action"] - 1  # Juntao
    return action


def main(epoch=10, verbose=1):
    # engine init
    engine = Engine()
    time.sleep(2)

    '''action from 1 to 16 iteratively'''
    # add for loop here
    for k in range(11, 12):
        ACTION = k + 1

        '''train iteratively'''
        for i in range(epoch):

            is_error = False

            print(BLUE + '[INFO] start {} / {} epoch.'.format(i+1, epoch) + RESET)

            engine.reset_state()

            file_name = "data/a_" + str(ACTION) + "_epoch_" + str(i + 1) + ".csv"
            with open(file_name, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                '''column name'''
                writer.writerow(["score", "frame"])

            '''wait for start'''
            timeout_cnt = 0
            while not engine.match_log('GameStart'):
                time.sleep(1)
                timeout_cnt += 1
                if timeout_cnt > 10:
                    print(RED + '[ERROR] engine cannot detect the game start signal.' + RESET)
                    is_error = True
                    break
            if not is_error: print(GREEN + '[INFO] engine detect the game start signal.' + RESET)

            '''train within an epoch'''
            while not is_error:
                is_error, is_gameover, img = engine.wait_stable(thresh=0.001, timeout=10)
                if is_error:
                    print(RED + '[ERROR] engine crashed, then reset...' + RESET)
                    break
                state = engine.get_info()

                score = state['score']
                frame = state['frame']

                # Juntao
                print("score = {}, frame = {}".format(score, frame))
                with open(file_name, 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([score, frame])

                if is_gameover:
                    print(YELLOW + '[INFO] game over: score = {} in frame {}'.format(score, frame) + RESET)
                    break

                '''the agent make decision to choose one action each step'''
                # action_num = 16
                action = agent(action=ACTION, score=score, frame=frame, flag=is_gameover, image=img)  # action_num=action_num

                if verbose:
                    print(CYAN + '[INFO] Score = {} at Frame {}, take action at {}.'.format(score, frame, action) + RESET)

                engine.pick_action(action)

            if is_error:
                i -= 1


if __name__ == '__main__':
    main(epoch=10, verbose=0)
    clean(['_cap_tmp.png', '_tmp_t1.png', '_tmp_t2.png', 'diff_img.png'])

