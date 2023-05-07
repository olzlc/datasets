import os

path = './images'
file = os.listdir(path)

# only_smoke = 0
# only_fire = 0
# fire_smoke = 0
# in_home = 0
# out_home = 0
# background = 0
# not_0_num = 0
# have_0_num = 0
# for item in file:
#     labels = item.split('-')
#     if labels[1] == '0' and labels[2] == '0':
#         have_0_num += 1
#         continue
#     not_0_num += 1
#
#     if labels[0] == '0':
#         in_home += 1
#     elif labels[0] == '1':
#         out_home += 1
#     else:
#         background += 1
#
#     if labels[1] == '1' and labels[2] == '0':
#         only_smoke += 1
#     elif labels[1] == '0' and labels[2] == '1':
#         only_fire += 1
#     elif labels[1] == '1' and labels[2] == '1':
#         fire_smoke += 1
#
# print("一共多少张烟火图片:" + str(not_0_num))
# print("一共多少张无烟火图片:" + str(have_0_num))
# print("一共多少张室内图片:" + str(in_home))
# print("一共多少张室外图片:" + str(out_home))
# print("一共多少张纯背景图片:" + str(background))
# print("一共多少张纯烟图片:" + str(only_smoke))
# print("一共多少张纯火图片:" + str(only_fire))
# print("一共多少张烟火图片:" + str(fire_smoke))

num = 0
for item in file:
    labels = item.split('-')
    if labels[0] == '2' and labels[1] == '1' and labels[2] == '1':
        num += 1
print(num)
