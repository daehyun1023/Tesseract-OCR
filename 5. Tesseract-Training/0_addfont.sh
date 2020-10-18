#!bin/bash


################################## Before run this script################################################
# make directory tesstraining

################################## After run this script, 0_config.sh, 0_setup.sh########################
# make directory train, (kortrain) in train, (batang dotum gothic myeongjo) in kortrain
# (batang dotum gothic myeongjo) in output


# fonts directory move

BASE_DIR=${PWD}



# batang dotum gothic myeongjo font-classification list
declare -a fontslist
fontslist=(batang dotum gothic myeongjo total)
fontclass=$fontslist[5]
cd fonts/$fontclass

#font list generate by Array
declare -a flist

# flist initialize
unset flist

# print name of flist, number of flist
for f in *; do
	flist[${#flist[@]}+1]=${f%.*};
	echo ${#flist[@]} $flist[${#flist[@]}];
done

cd $BASE_DIR

# Set variable list generate by Array
#MAX_PAGES_LIST=(10 20 30)
#ITERATION_LIST=(400 800 1200 1600)

