import re
import time
import random
import numpy as np
from cv2 import cv2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from diffimg import diff


class Engine:
    def __init__(self, window_size=(500, 925), action_num=16):
        self.capabilities = DesiredCapabilities.CHROME
        self.capabilities['goog:loggingPrefs'] = { 'browser':'ALL' }

        # self.driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        self.driver = webdriver.Chrome("chromedriver")  # Juntao
        self.driver.set_window_rect(x=10, y=35)
        self.driver.set_window_size(*window_size)
        self.driver.get('http://localhost:5688/')
        time.sleep(3)

        self.playground = self.driver.find_element_by_id('GameCanvas')
        self.actions = [int((i+1)*self.playground.size['width']/(action_num+1)) for i in range(action_num)]
        self.action_num = action_num

        self.env_params = {}
        self.env_params['score'] = 0
        self.env_params['frame'] = 0

        self.agent_func = lambda: random.randint(0, len(self.actions)-1)

    def reset_state(self):
        self.driver.refresh()

        self.playground = self.driver.find_element_by_id('GameCanvas')
        self.actions = [int((i+1)*self.playground.size['width']/(self.action_num+1)) for i in range(self.action_num)]

        self.env_params = {}
        self.env_params['score'] = 0
        self.env_params['frame'] = 0

    def capture(self, filename='tmp.png'):
        self.playground.screenshot(filename)

    def capture_fetch(self):
        self.capture('_cap_tmp.png')
        return cv2.imread('_cap_tmp.png')

    def parse_log(self):
        # retval indicates whether the game is over or not
        log = self.driver.get_log('browser')
        if len(log) != 0:
            log_msg = re.findall('"([^"]*)"', log[-1]['message'])
            if len(log_msg) == 0: return True, False
            if log_msg[0] == 'GameOver':
                if len(log) > 1:
                    log_msg = re.findall(r'\d+', log[-2]['message'])
                    if len(log_msg) == 0: return True, True
                    self.env_params['score'] = int(log_msg[-1])
                return False, True
            log_msg = re.findall(r'\d+', log[-1]['message'])
            if len(log_msg) == 0: return True, False
            self.env_params['score'] = int(log_msg[-1])
        return False, False

    def match_log(self, keyword):
        # retval indicates whether the keyword exists or not (full match)
        log = self.driver.get_log('browser')
        if len(log) != 0:
            log_msg = re.findall('"([^"]*)"', log[-1]['message'])
            if len(log_msg) > 0:
                if log_msg[0] == keyword:
                    return True
        return False

    def pick_action(self, action_pos, reset=False):
        assert 0 <= action_pos < len(self.actions)
        if reset:
            self.env_params['frame'] = 0
        self.env_params['frame'] += 1

        _action = webdriver.common.action_chains.ActionChains(self.driver)
        _action.move_to_element_with_offset(self.playground, self.actions[action_pos],
            self.playground.size['height']/2).click().perform()

    def wait_stable(self, thresh=0.001, nextime=0.3, timeout=10):
        pixel_diff = 1
        timeout_cnt = 0
        while pixel_diff > thresh:
            self.capture('_tmp_t1.png')
            time.sleep(nextime)
            self.capture('_tmp_t2.png')
            pixel_diff = diff('_tmp_t1.png', '_tmp_t2.png')
            timeout_cnt += 1
            if timeout_cnt > timeout:
                break
        img = self.capture_fetch()
        is_error, is_gameover = self.parse_log()
        return is_error, is_gameover, img

    def get_info(self):
        return self.env_params

    def hook_agent(self, agent_func):
        self.agent_func = agent_func

