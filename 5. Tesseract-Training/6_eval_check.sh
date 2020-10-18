#!/bin/bash

source 0_config.sh

lstmeval \
        --model $OUTPUT_DIR/${font}_checkpoint \
        --traineddata $LANG_TRAIN_DIR/$fontclass/$font/$LANG/$LANG.traineddata \
        --eval_listfile $LANG_TRAIN_DIR/$fontclass/$font/$LANG.training_files.txt

