GOCD has really nice feature of [displaying a difference between two given artifacts](https://docs.gocd.io/current/advanced_usage/compare_pipelines.html).
By the time of writing this scripts gocd 16.3.0 didn't have an API, check it still may not have;)

So what script does is parsing the HTML page and creating the output file with story number and commit description to be used
further in the CD pipeline. Then we remove duplicate commits and create two separate file, one as list of stories retrieved from commits second is description.

Output of python looks something like that:

```
CRP-1450;CRP-1450 lower jacoco coverate so we can build temporarily
CRP-0000;CRP-0000 No story - add missing test for creating risk profile
CPMEMBER-2690;CPMEMBER-2690 [M1] [FE] [BE] Fix handling of evidence linked to a case file
CPMEMBER-2690;CPMEMBER-2690 [M1] [FE] [BE] Fix handling of evidence linked to a case file
;CRP-1452 : Corrected url
;CRP-1452 : Changed way updateUrl is used
CRP-1452;CRP-1452 Correcting host and port env variable name.
CRP-1453;CRP-1453 Added account security coreplatform client config to increase timeout
```

Run application:
```
python GoHTMLParserRunner.py gooutput.html commits.txt
```
Run test:
```
python -m unittest GoHTMLParserTest
```

Run application:
```
python GoHTMLParserRunner.py gooutput.html commits.txt
```
Run test:
```
python -m unittest GoHTMLParserTest
```
 
Example of usage: 
Given HTML file gooutput.html, running run.sh will generate unique_commits.txt with all duplicates removed, stories.txt:
```
 CPMEMBER-2690,CRP-1450,CRP-1452,CRP-1453
```
 and description.txt:
```
 commit: CRP-1452 : Changed way updateUrl is used
 commit: CRP-1452 : Corrected url
 story: CPMEMBER-2690 commit: CPMEMBER-2690 [M1] [FE] [BE] Fix handling of evidence linked to a case file
 story: CRP-0000 commit: CRP-0000 No story - add missing test for creating risk profile
 story: CRP-1450 commit: CRP-1450 lower jacoco coverate so we can build temporarily
 story: CRP-1452 commit: CRP-1452 Correcting host and port env variable name.
 story: CRP-1453 commit: CRP-1453 Added account security coreplatform client config to increase timeout
```
