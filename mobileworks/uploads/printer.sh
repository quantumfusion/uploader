#! /usr/bin/bash
# ===================
# File: printer.sh
# Author: Matthew Chang
# Version: 0.2
# Date: 11/14/2012
# ===================
# Script takes two arguments and automates the process
# of printing multiple copies of a file.
#
# Note: Make sure this is an executable file!!!
#
# Use example: ./printer.sh nyan.pdf 32
#       Will print 32 copies of nyan.pdf
# ===================
# Changelog:
# 2/2013
#       Added print statement to return current progress

for ((i=1; i<=$2; i++))
do
    lp -c -d phaser $1
    printf "Printed %d/%d\n" "$i" "$2"
    sleep $[ ( $RANDOM % 30 ) + 1 ]
done    
