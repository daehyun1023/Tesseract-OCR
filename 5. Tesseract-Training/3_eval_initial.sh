#!/bin/bash

source 0_config.sh

# $TRAINED_DATA_DIR/$LANG.traineddata 
# $TRAINED_DATA_DIR/$fontclass/${recent_font}_new.traineddata 

lstmeval --model $LANG_TRAIN_DIR/$fontclass/$font/$LANG.lstm \
	--traineddata $TRAINED_DATA_DIR/$LANG.traineddata \
	--eval_listfile $LANG_TRAIN_DIR/$fontclass/$font/$LANG.training_files.txt

