# CupsCapture

## Introduction
This program will help you not to forget to remove cups and glasses from the table. The mug detector was written using a pre-trained model from Pytorch. If there are more than a certain number of glasses, you will receive a notification in Telegram

## Installation
### Prerequisites
- Linux, macOS or Windows
- Python 3.6+

## Install CupCapture

**Clone repo**
```shell
git clone https://github.com/LongaBonga/CupsCapture.git
```

**Install requirements**
```shell
cd CupsCapture
pip install -r requirements.txt
```

## Run program

there are also arguments for starting this project:
- ``` --start_time``` The hour when program will start searching cups
- ``` --finish_time``` The hour when program will finish searching cups
- ``` --video_path``` The path to the video. or digit, if it is web camera
- ``` --time_freq``` The frequency with which the program will search for cups and send notifications if they are found. Default 15 minutes
- ``` --frame_amount``` The number of frames that must be processed at a time to predict the number of cups

**Run example**
```shell 
python3 main.py --start_time=10 --finish_time=23 --video_path=0 --frame_amount=5
```