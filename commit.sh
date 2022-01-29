#!/usr/bin/bash
date=2
while [ $date -le 30 ]
do
	powershell set-date -date $date-12-2020
	for i in {0..100}
	do
		echo hello >>  f.txt
		git commit f.txt -m "any comment"
	((date=date+1))
done
