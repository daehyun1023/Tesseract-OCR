#!/bin/bash

source 0_config.sh

#if [ ! -d $OUTPUT_DIR ]; then
#        mkdir $OUTPUT_DIR
#else
#        rm -rf $OUTPUT_DIR/*
#fi

lstmtraining \
        --debug_interval $DEBUG \
        --continue_from $FONT_LANG_TRAIN_DIR/$LANG.lstm \
	--old_traineddata $TRAINED_DATA_DIR/${LANG}.traineddata \
        --traineddata $FONT_LANG_TRAIN_DIR/$LANG/$LANG.traineddata \
	--train_listfile $FONT_LANG_TRAIN_DIR/$LANG.training_files.txt \
        --model_output $FONT_OUTPUT_DIR/$fontclass \
        --max_iterations $ITERATION
#$LANG.training_files.txt
#	--old_traineddata $TRAINED_DATA_DIR/$LANG.traineddata \
#	--old_traineddata $FONT_TRAINED_DATA_DIR/${recent_font}_new.traineddata \
#       --train_listfile $LANGDATA_DIR/$LANG/$LANG.training_text \
