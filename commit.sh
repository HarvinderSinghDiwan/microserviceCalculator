#!/usr/bin/bash
date=2
while [ $date -le 30 ]
do
	powershell set-date -date $date-1-2021
	for i in {0..2}
	do
		echo hello >>  config.py
		git commit config.py -m "configurations added"
	done
	((date=date+1))
done
