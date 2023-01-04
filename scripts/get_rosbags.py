import pandas as pd
import sys
import subprocess
import os
#later if time, make path not hard coded and create directory if it doesn't exist
# subprocess.run(["cd","/hdd/luisamao/robodata/Large_Crowds_Data"])
excel_file = "~/PreferenceLearningSocialNav/SCAND.xlsx"
all_rosbags = pd.read_excel(excel_file, sheet_name=1)
# save_path = os.environ['save_path']
save_path = "/home/luisamao/PreferenceLearningSocialNav/Sidewalk_rosbags"
robot = "Spot"
tag = "Navigating Through Large Crowds" #if None else sys.argv[1]
tag1 = "Passing Conversational Groups"
tag2 = "Against Traffic"
tag3 = "Overtaking"
tag4 = "Sidewalk"
end = len(all_rosbags)
count = 0
for i in range(0,end):
    if (str(all_rosbags["Tags"][i]).find(tag) == -1  and str(all_rosbags["Tags"][i]).find(tag1) == -1 ) and str(all_rosbags["Tags"][i]).find(tag2) == -1 and str(all_rosbags["Tags"][i]).find(tag3) == -1 and str(all_rosbags["Tags"][i]).find(tag4) != -1 and str(all_rosbags["Robot"][i])==robot:
        count+=1
        # print(all_rosbags["Link to rosbag"][i])
        # print(str(all_rosbags["Tags"][i]))
        subprocess.run(["wget", str(all_rosbags["Link to rosbag"][i]), "-P", save_path])
