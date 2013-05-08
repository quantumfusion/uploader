#!/bin/bash
for num in {1..28}; do
	howmany=$( ssh -o ConnectTimeout=10 cs186-fd$1@hive$num.cs.berkeley.edu who | wc -l )
	echo "hive$num.cs.berkeley.edu: $howmany other user(s)"
done
