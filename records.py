"""

-*- coding: utf-8 -*-

@Author  : ZHAO Juntao
@Time    : 3/22/2021 11:51 AM

"""

import numpy as np
import matplotlib.pyplot as plt

action = range(1, 17)
epoch = range(1, 11)

score = [[0]*10]*16
frame = [[0]*10]*16

score[0] = [416, 485, 300, 416, 482, 468, 320, 254, 414, 447]
frame[0] = [133, 152, 103, 131, 149, 155, 115, 97, 133, 140]

score[1] = [307, 294, 336, 332, 513, 278, 26, 308, 330, 348]
frame[1] = [124, 106, 115, 113, 156, 100, 25, 117, 111, 118]

score[2] = [330, 287, 533, 354, 395, 28, 426, 321, 14, 9]
frame[2] = [114, 97, 165, 119, 131, 17, 132, 114, 19, 18]

score[3] = [8, 28, 15, 15, 23, 11, 322, 28, 356, 8]
frame[3] = [15, 16, 20, 15, 18, 15, 114, 22, 128, 14]

score[4] = [390, 24, 308, 368, 580, 535, 15, 12, 15, 459]
frame[4] = [132, 18, 115, 129, 173, 159, 19, 17, 18, 146]

score[5] = [10, 13, 26, 345, 281, 28, 258, 451, 370, 516]
frame[5] = [16, 18, 20, 123, 126, 144, 99, 149, 140, 160]

score[6] = [14, 394, 168, 422, 371, 461, 431, 367, 325, 517]
frame[6] = [19, 128, 79, 148, 137, 154, 153, 132, 122, 163]

score[7] = [31, 352, 49, 513, 362, 23, 15, 449, 396, 268]
frame[7] = [23, 127, 28, 161, 128, 20, 17, 159, 139, 107]

score[8] = [483, 378, 400, 17, 396, 378, 340, 10, 480, 393]  # epoch 1/7: [ERROR] engine crashed, then reset...
frame[8] = [157, 131, 137, 20, 133, 156, 124, 16, 144, 129]

score[9] = [13, 9, 529, 488, 39, 360, 293, 10, 362, 472]
frame[9] = [15, 15, 158, 162, 18, 124, 112, 15, 125, 150]

score[10] = [472, 432, 381, 385, 321, 538, 394, 377, 20, 27]  # epoch 7 ERROR
frame[10] = [150, 146, 134, 144, 118, 171, 135, 123, 21, 22]

score[11] = [360, 618, 316, 323, 391, 28, 467, 367, 339, 12]
frame[11] = [123, 185, 112, 115, 126, 22, 152, 112, 126, 21]

score[12] = [469, 317, 490, 38, 10, 11, 310, 365, 369, 290]
frame[12] = [139, 110, 155, 27, 17, 16, 109, 128, 128, 111]

score[13] = [320, 28, 359, 261, 309, 407, 12, 223, 25, 335]
frame[13] = [122, 143, 128, 99, 106, 142, 20, 89, 23, 117]

score[14] = [236, 507, 468, 277, 464, 454, 328, 12, 21, 445]
frame[14] = [100, 151, 151, 105, 142, 144, 101, 20, 21, 144]

score[15] = [392, 344, 317, 182, 449, 228, 279, 348, 402, 231]
frame[15] = [136, 117, 111, 73, 138, 90, 99, 121, 128, 95]

score_rnd = [320, 328, 418, 445, 379, 335, 376, 503, 336, 270]
frame_rnd = [120, 119, 149, 143, 129, 125, 134, 171, 120, 117]

'''final scores of action 1-16'''
# for i in range(16):
#     plt.plot(epoch, score[i], "o")
#     plt.plot(epoch, score[i])
#     plt.xlabel('epoch')
#     plt.ylabel('final score')
#     plt.title('final scores for action ' + str(i+1))
#     # for i in range(10):
#     #     plt.text(k_vales[i], accuracies[i], (accuracies[i]))
#     plt.show()

'''final scores of random action'''
plt.plot(epoch, score_rnd, "o")
plt.plot(epoch, score_rnd)
plt.xlabel('epoch')
plt.ylabel('final score')
plt.title('final scores for random action')
plt.show()

'''average final scores'''
# scores = np.zeros(16)
# for i in range(16):
#     scores[i] = np.mean(score[i])
# plt.plot(action, scores, "o")
# plt.plot(action, scores)
# plt.xlabel('action')
# plt.ylabel('final score')
# plt.title('average final scores in 10 epochs')
# plt.show()

'''remove extreme values'''
# scores = np.zeros(16)
# for i in range(16):
#     score[i].remove(min(score[i]))
#     score[i].remove(max(score[i]))
#     print(score[i])
#     scores[i] = np.mean(score[i])
# plt.plot(action, scores, "o")
# plt.plot(action, scores)
# plt.xlabel('action')
# plt.ylabel('final score')
# plt.title('average final scores in 10 epochs (without extreme values)')
# plt.show()
