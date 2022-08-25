import os
import glob
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-target_txtCount", type=int, default=500)
args = parser.parse_args()

txt = "txt"

'''
Count how many txt file for each id
'''
ids = []
for _id in tqdm(sorted(os.listdir(txt))):
        txtCount = 0
        for yt_key in os.listdir(os.path.join(txt, _id)):
                txtCount+= len(os.listdir(os.path.join(txt, _id, yt_key)))
        ids.append({"_id":_id, "txtCount": txtCount})

'''
Sort ids by txt count in descending order and save to 'txtCount.txt'
'''
ids.sort(key=lambda x: x["txtCount"], reverse=True)
with open("txtCount.txt", 'w') as f:
        f.write("id,txtCount\n")
        for item in ids:
                f.write(f"{item['_id']},{item['txtCount']}\n")

'''
Select ids that has >=txtCount txts and save the video ids to 'video_ids_txtCount{args.target_txtCount}.txt'
'''
with open(f"video_ids_txtCount{args.target_txtCount}.txt", 'w') as f:
        f.write("video_id\n")
        for item in tqdm(ids):
                if item['txtCount'] < args.target_txtCount: continue
                for video_id in os.listdir(os.path.join(txt, item['_id'])):
                        f.write(f"{video_id}\n")