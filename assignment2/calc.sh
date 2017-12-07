#!/bin/bash

declare cmd=$@
declare -i value=0


if [ "$1" == "S" ]
then
	for item in ${cmd[*]:1}
	do
		value+=item
	done
elif [ "$1" == "P" ]
then
	value+=$2
	for item in ${cmd[*]:2}
	do
		value=value*item
	done
elif [ "$1" == "M" ]
then
	for item in ${cmd[*]:1}
	do
		if (($item >= $value))
		then
			value=item
		fi
	done
elif [ "$1" == "m" ]
then
	value=$2
	for item in ${cmd[*]:2}
	do
		if (($item <= $value))
		then
			value=item
		fi
	done
fi
echo $value
