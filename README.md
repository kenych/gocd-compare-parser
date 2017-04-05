GOCD has really nice feature of [displaying a difference between two given artifacts](https://docs.gocd.io/current/advanced_usage/compare_pipelines.html).
By the time of writing this scripts gocd 16.3.0 didn't have an API, check it still may not have;)

So what script does if effectively parsing the HTML page and creating the output file with story number and commit description to be used
further in the CD pipeline.

Output looks something like that:

CRP-1450;CRP-1450 lower jacoco coverate so we can build temporarily
CRP-0000;CRP-0000 No story - add missing test for creating risk profile
CPMEMBER-2690;CPMEMBER-2690 [M1] [FE] [BE] Fix handling of evidence linked to a case file
CPMEMBER-2690;CPMEMBER-2690 [M1] [FE] [BE] Fix handling of evidence linked to a case file
;CRP-1452 : Corrected url
;CRP-1452 : Changed way updateUrl is used
CRP-1452;CRP-1452 Correcting host and port env variable name.
CRP-1453;CRP-1453 Added account security coreplatform client config to increase timeout

 
 