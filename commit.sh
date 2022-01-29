#!/usr/bin/bash
date=2
while [ $date -le 30 ]
do
	powershell set-date -date $date-01-2022
	for i in {0..10}
	do
		echo hello >>  config.py
		git commit config.py -m "any commenear"
	done
	((date=date+1))
done
