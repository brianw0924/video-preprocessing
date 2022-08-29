wget www.robots.ox.ac.uk/~vgg/data/voxceleb/data/vox1_test_txt.zip
unzip vox1_test_txt.zip

wget www.robots.ox.ac.uk/~vgg/data/voxceleb/data/vox1_dev_txt.zip
unzip vox1_dev_txt.zip

wget www.robots.ox.ac.uk/~vgg/data/voxceleb/data/vox2_test_txt.zip
unzip vox2_test_txt.zip

wget www.robots.ox.ac.uk/~vgg/data/voxceleb/data/vox2_dev_txt.zip
unzip vox2_dev_txt.zip

python3 -m pip install -U yt-dlp

sudo apt-get install ffmpeg

python txtCount.py
