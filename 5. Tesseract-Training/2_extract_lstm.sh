#!/bin/bash

source 0_config.sh

# Assign traineddata

# $TRAINED_DATA_DIR/$LANG.traineddata => recent traineddata
# batang 12, dotum 12, gothic 15, myeongjo 10

# if train by font => $FONT_TRAINED_DATA_DIR
# if train by total => $TOTAL_TRAINED_DATA_DIR

combine_tessdata -e $TRAINED_DATA_DIR/kor.traineddata $FONT_LANG_TRAIN_DIR/kor.lstm

#combine_tessdata -e $FONT_TRAINED_DATA_DIR/${recent_font}_new.traineddata $LANG_TRAIN_DIR/$fontclass/$font/$LANG.lstm
