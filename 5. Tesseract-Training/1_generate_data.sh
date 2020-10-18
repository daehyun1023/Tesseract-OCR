#!/bin/bash

source 0_addfont.sh
source 0_config.sh

echo "==== Generating data for lang $LANG ==="
# --fonts_dir fonts/$fontclass
#rm -rf $LANG_TRAIN_DIR/*

# text2image --fonts_dir /usr/share/fonts/batang --list_available_fonts
# fc-list



$TRAIN_BASE_DIR/tesseract/src/training/tesstrain.sh --fonts_dir fonts/$fontclass \
	     --fontlist $flist \
	     --lang $LANG \
	     --linedata_only \
	     --langdata_dir $LANGDATA_DIR \
	     --tessdata_dir $TRAIN_BASE_DIR/tesseract/tessdata \
	     --save_box_tiff \
	     --maxpages $MAX_PAGES \
	     --output_dir $FONT_LANG_TRAIN_DIR
