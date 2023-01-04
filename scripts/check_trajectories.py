import pickle
import numpy as np
import os
import sys

if len(sys.argv)>1:
    directory = sys.argv[1]
else: directory = "/hdd/luisamao/robodata/Nav_Large_Crowds_Data"
count = 0
total = 0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        # print(f)
        with open(f, "rb") as file:
            a = pickle.load(file)
            for index in range(0, len(a['human_expert_odom'])):
                if (len(a['move_base_path'][index])>0 and len(a['human_expert_odom'][index])>0):
                    x1 = a['human_expert_odom'][index][0][0]-a['move_base_path'][index][0][0]
                    y1 = a['human_expert_odom'][index][0][1]-a['move_base_path'][index][0][1]
                    x2 = a['human_expert_odom'][index][-1][0]-a['move_base_path'][index][-1][0]
                    y2 = a['human_expert_odom'][index][-1][1]-a['move_base_path'][index][-1][1]
                    # if (x1!=0 or x2!=0 or y1!=0 or y2!=0):
                        # print(filename, index, x1, y1, x2, y2)
                    total+=1
                    if (x2!=0 or y2!=0):
                        print(filename, index, x2, y2)
                        count+=1
                    # if (a['move_base_path'][index][-1][0]>400 or a['move_base_path'][index][-1][1]>400):
                    #     print(a['move_base_path'][index][-1][0],a['move_base_path'][index][-1][1])
print(count,"/", total, "mismatched end positions")