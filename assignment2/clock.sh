#!/bin/bash

#clock showing time
# either AM/PM clock or regular 24h clock

show(){
	local x=$1
	local y=$2
	local txt=$3
	tput cup $x $y
	echo "$txt"
}

AMPM=false

while [ : ]
do
	clear
	time1="$(date +"%r")"
	time2="$(date +"%T")"
	
	if [ "$AMPM" == true ]
	then 
		show 10 10 "Time is: $time1"
	else
		show 10 10 "Time is: $time2"
	fi
	show 11 10 " press 1 to exit!"
	show 12 10 " press 2 for AM/PM!"
	tput cup 13 10; read -t 2 -p "Choice [1-2] " usrhndl

	case $usrhndl in
		1) echo "Bye."; exit 0;;
		2) AMPM=true
	esac
done



 
