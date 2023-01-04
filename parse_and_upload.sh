#!/bin/bash
# export rosbag_path="$(find / -name "spot_ahg_dataset" 2>/dev/null)"
# export rosbag_path=/hdd/luisamao/robodata/spot_ahg_dataset
export rosbag_path=/home/luisamao/PreferenceLearningSocialNav/Against_Traffic_rosbags
export save_path=/home/luisamao/PreferenceLearningSocialNav/Against_Traffic

export num=${1:-10} 

echo 'writing rosbags to rosbags.txt'

# python3 scripts/get_rosbags.py

PYCMD=$(cat <<EOF
import os
rosbag_path = os.environ['rosbag_path']
# rosbag_path = os.environ['save_path']
# iterate over files in
# that directory
num=0
with open('/home/luisamao/PreferenceLearningSocialNav/src/lidar_rosbag_parser/rosbags.txt', 'w') as file:
    for filename in os.listdir(rosbag_path):
        f = os.path.join(rosbag_path, filename)
        # checking if it is a file
        if os.path.isfile(f):
            file.write(filename.replace('.bag',''))
            file.write('\n')
        # num+=1
        # if num==int(os.environ['num']):
        #     break
EOF
)

python3 -c "$PYCMD"

echo 'parsing bags in rosbags.txt'

File="/home/luisamao/PreferenceLearningSocialNav/src/lidar_rosbag_parser/rosbags.txt"
Lines=$(cat $File)
for Line in $Lines
do
    # echo "$Line"
    roslaunch lidar_rosbag_parser parse_rosbag.launch bag:=$Line
done

echo 'done'

# echo 'starting sftp'

# sftp -oPort=22 luisamao@robovision.csres.utexas.edu:/robodata/luisamao <<EOF
# # # rm -r Preference_Learning_Data
# # # put -R /hdd/luisamao/robodata/Preference_Learning_Data 
# rm -r Nav_Large_Crowds_Data
# put -R /hdd/luisamao/robodata/Nav_Large_Crowds_Data
# exit
# EOF

# echo 'done'
