#  APACHE 2.0 licence.
#
#  Utility to comment out those naughty unused variables and imports
#  and then run your golong project.
#
#  Use this script for any small quick golang experiement, it's
#  obviously not production quality stuff :-D
#
#  But it will save you a lot of time and typing!
#
#  How to use:
#
#  Put this script in your (exported) script directory, and chmod u+x
#  it. 
#
#  Now, anywhere you have gopher code, do: CompileGolang.bash <your file>
#
#  This works on the entire tree you have in there.
# 
#  Written by: https://github.com/GabrielaBarbara/ 

#! /bin/bash

workfile=$1
go run $workfile 2>gorun_error_report.txt
tab=`echo -e "\t"`
recompile=0
offset=0
file=gorun_error_report.txt
while IFS=: read -r theFile line problem what wot
do
		if [ "$offset" = 0 ]; then
				lastFile=$theFile
		else
				if [ "$lastFile" != "$theFile" ]; then
						offset=0
				fi
		fi
		if [ "$problem" == " imported and not used" ]; then
				replace="// UNUSED IMPORT $what $wot"
				sed -i "$line"s:.*:"$replace": $theFile
				recompile=1
		fi
		check_problem=`echo $problem | cut -d' ' -f2-`
		if [ "$check_problem" == "declared and not used" ]; then
				unusedVar=`echo $problem | cut -d " " -f1`
				offset=$(($offset+1))
				line=$(($line+$offset))
				sed -i "$line"'i\'"$tab"'_ = '"$unusedVar"' // UNUSED VARIABLE\' $theFile
				recompile=1
		fi
done <"$file"
cat gorun_error_report.txt
rm gorun_error_report.txt
if [ $recompile -eq 1 ]; then
		echo "Unused code detected and temporarily fixed."
 		gorun.bash $workfile
fi
