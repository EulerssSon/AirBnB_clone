#!/usr/bin/env bash
#this script is for fast push to origin adding all files

if [ $# -eq 0 ]; then
	read -p "Enter Your Commit Msg: " msg
else
	msg=$1
fi
git add .
git commit -m "${msg}"
git push
