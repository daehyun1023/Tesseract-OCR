#!/bin/bash
#source 0_config.sh
# WARNING
# ==================================================================
# Run this script if you get encoding errors during lstmeval.
# This will combine unicharset and create a new .traineddata
# ====================================================================


# WARNING
#====================================================================
# Assign TRAINEDDATA FILE
#combine_tessdata -u $FONT_TRAINED_DATA_DIR/${recent_font}_new.traineddata $LANG_TRAIN_DIR/$fontclass/$font/$LANG.
#======================================================================

echo "==== Unpacking traineddata for kor ===="

combine_tessdata -u $TRAINED_DATA_DIR/kor.traineddata $FONT_LANG_TRAIN_DIR/$LANG.

#unicharset_extractor $FONT_LANG_TRAIN_DIR/kor.Baekmuk_Dotum.exp0.box $FONT_LANG_TRAIN_DIR/kor.BareunDotum.exp0.box $FONT_LANG_TRAIN_DIR/kor.BareunDotumPro.exp0.box $FONT_LANG_TRAIN_DIR/kor.HCR.Dotum.exp0.box $FONT_LANG_TRAIN_DIR/kor.HCR_Dotum_Bold.exp0.box $FONT_LANG_TRAIN_DIR/kor.UnDotum.exp0.box


#wordlist2dawg $LANGDATA_DIR/$LANG/$LANG.wordlist kor.lstm-word-dawg $FONT_LANG_TRAIN_DIR/ kor.lstm-unicharset

#combine_tessdata -o $TRAINED_DATA_DIR/kor.traineddata $FONT_LANG_TRAIN_DIR/kor.lstm-word-dawg

echo "==== Setting new version ===="

VERSION_STR="$LANG version on $(date +%F) from"

sed -e "s/^/$VERSION_STR" $FONT_LANG_TRAIN_DIR/$LANG.version > $FONT_LANG_TRAIN_DIR/$LANG.new.version

echo "==== Merging unicharset ===="

merge_unicharsets $FONT_LANG_TRAIN_DIR/$LANG.lstm-unicharset $FONT_LANG_TRAIN_DIR/$LANG/$LANG.unicharset $FONT_LANG_TRAIN_DIR/$LANG.unicharset

echo "==== New traineddata for training ===="

if [ -d $FONT_LANG_TRAIN_DIR/$LANG ]; then
  mv $FONT_LANG_TRAIN_DIR/$LANG $FONT_LANG_TRAIN_DIR/${LANG}_old
fi

combine_lang_model \
  --input_unicharset $FONT_LANG_TRAIN_DIR/$LANG.unicharset \
  --script_dir $LANGDATA_DIR \
  --words $LANGDATA_DIR/$LANG/$LANG.wordlist \
  --numbers $LANGDATA_DIR/$LANG/$LANG.numbers \
  --puncs $LANGDATA_DIR/$LANG/$LANG.punc \
  --output_dir $FONT_LANG_TRAIN_DIR \
  --lang $LANG \
  --version_str $FONT_LANG_TRAIN_DIR/$LANG.new.version
echo "\nNew $LANG.traineddata created! \n"
