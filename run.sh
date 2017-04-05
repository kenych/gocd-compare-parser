#!/bin/bash

python GoHTMLParserRunner.py gooutput.html commits.txt
sort -u commits.txt > unique_commits.txt
./prepare-ticket-stories.sh unique_commits.txt stories.txt
./prepare-ticket-description.sh unique_commits.txt description.txt

