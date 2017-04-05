#!/bin/bash

commits_file=$1
output_file=$2


rm -f $output_file
output=""

while read commit; do
    IFS=';' read -ra commitArr <<< "$commit"
    if [ ! -z "${commitArr[0]}" -a "${commitArr[0]}" != " " ]
    then
        $(grep ${commitArr[0]} <<< "$output" > /dev/null) || $(grep "\-0000" <<< "${commitArr[0]}" > /dev/null)
        if [ "$?" -eq 1 ];
        then
            if [ -z "${output}" ];
            then
                output="$output${commitArr[0]}"
            else
                output="$output,${commitArr[0]}"
            fi
        fi
    fi
done < $commits_file
echo "${output}" > $output_file


