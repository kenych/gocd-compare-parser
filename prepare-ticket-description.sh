#!/bin/bash

commits_file=$1
output_file=$2

rm -f $output_file
output=""
NEWLINE=$'\n'

while read commit; do
    IFS=';' read -ra commitArr <<< "$commit"
    if [ ! -z "${commitArr[0]}" -a "${commitArr[0]}" != " " ]
    then
        output="${output} story: ${commitArr[0]} commit: ${commitArr[1]}${NEWLINE}"
    else
        output="${output} commit: ${commitArr[1]}${NEWLINE}"
    fi
done < $commits_file
echo "${output}" > $output_file
