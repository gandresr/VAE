#!/bin/bash

wget http://www.cs.ubc.ca/labs/imager/tr/2017/DeepVideoDeblurring/DeepVideoDeblurring_Dataset_Original_High_FPS_Videos.zip
unzip *.zip videos_adobe240
python batch_dataset.py
