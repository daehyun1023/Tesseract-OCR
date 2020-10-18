#!/bin/bash

source 0_config.sh

lstmtraining --stop_training \
        --continue_from $FONT_OUTPUT_DIR/${fontclass}_checkpoint \
        --traineddata $FONT_LANG_TRAIN_DIR/$LANG/$LANG.traineddata \
        --model_output $FONT_TRAINED_DATA_DIR/${fontclass}.traineddata
