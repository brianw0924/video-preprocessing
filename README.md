1) Install requirments:
```
pip install -r requirements.txt
```

2) Run script
```
bash script.sh
```

3) Run preprocessing (assuming 8 gpu, and 5 workers per gpu).
```
python crop_vox.py --workers 40 --device_ids 0,1,2,3,4,5,6,7 --format .mp4