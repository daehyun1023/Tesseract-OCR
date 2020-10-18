# ===================================
# Set variable options for training
# batang 2, dotum 2, gothic 5, myeongjo 3
LANG=kor
# FONT_LIST=$flist[1]
# RECENT_FONT=$flist[1]
MAX_PAGES=100
ITERATION=2000
DEBUG=-1
#font=$(echo $FONT_LIST | cut -f 1 -d ' ')
#font2=$(echo $FONT_LIST | cut -f 2 -d ' ')
#font3=$(echo $FONT_LIST | cut -f 3 -d ' ')

# font=$(echo $FONT_LIST | tr -d ' ')

#recent_font=$(echo $RECENT_FONT | cut -f 1 -d ' ')
#recent_font2=$(echo $RECENT_FONT | cut -f 2 -d ' ')
#recent_font3=$(echo $RECENT_FONT | cut -f 3 -d ' ')

# recent_font=$(echo $RECENT_FONT | tr -d ' ')


# ===================================

# Root Directory
BASE_DIR=${PWD}

# Training Directory
TRAIN_BASE_DIR=$BASE_DIR/tesstraining
TRAIN_DIR=$TRAIN_BASE_DIR/train

# Language Training Directory
LANG_TRAIN_DIR=$TRAIN_DIR/${LANG}train
FONT_LANG_TRAIN_DIR=$LANG_TRAIN_DIR/$fontclass

# Result Directory
OUTPUT_DIR=$TRAIN_BASE_DIR/output
FONT_OUTPUT_DIR=$OUTPUT_DIR/$fontclass

# Langdata Directory
LANGDATA_DIR=$TRAIN_BASE_DIR/langdata

# Langdata LSTM Directory
LANGDATA_LSTM_DIR=$TRAIN_BASE_DIR/langdata_lstm

# trained data Directory
TRAINED_DATA_DIR=$BASE_DIR/traindata

# font trained data Directory
FONT_TRAINED_DATA_DIR=$TRAINED_DATA_DIR/$fontclass


chmod +x 0_setup.sh 1_generate_data.sh 2_extract_lstm.sh 3_eval_initial.sh 4_generate_traineddata.sh 5_finetune.sh 6_eval_check.sh 7_combine.sh
