# Daniel Vogler
# geopard tests

mkdir -p ./output/
rm -f ./output/benchmark.txt

declare -A tests

### set test indices to check
test_idx=(1 2 3 4 5 6 7 8)

### example - one-way skimo
tests[1,name]="tds_sunnestube"
tests[1,dtw]=0.09702
tests[1,radius]=7
tests[1,t]=0:25:22
tests[1,gold_name]="tds_sunnestube_segment.gpx"
tests[1,activity_name]="tds_sunnestube_activity_25_25.gpx"

### example - gpx track jump during activity - tdh2
tests[2,name]="tdh2_gpx_jump"
tests[2,dtw]=0.08136
tests[2,radius]=7
tests[2,t]=0:36:14
tests[2,gold_name]="tdh2.gpx"
tests[2,activity_name]="tdh2_error.gpx"

### example - intersecting tracks - tdu3
tests[3,name]="tdu3_ob8"
tests[3,dtw]=0.01154
tests[3,radius]=7
tests[3,t]=0:26:53
tests[3,gold_name]="tdu3_dv.gpx"
tests[3,activity_name]="tdu3_ls.gpx"

### example - one-way cross-country ski
tests[4,name]="nordicstar_dischmatal"
tests[4,dtw]=0.09671
tests[4,radius]=4
tests[4,t]=0:44:26
tests[4,gold_name]="nordicstar_dischmatal_segment.gpx"
tests[4,activity_name]="nordicstar_dischmatal_activity_44_39.gpx"

### example - green marathon zurich
tests[5,name]="green_marathon_zurich"
tests[5,dtw]=0.12866
tests[5,radius]=15
tests[5,t]=4:15:11
tests[5,gold_name]="green_marathon_segment.gpx"
tests[5,activity_name]="green_marathon_activity_4_15_17.gpx"

### example - two loops
tests[6,name]="nordicstar_weltcup"
tests[6,dtw]=0.06490
tests[6,radius]=34
tests[6,t]=0:25:46
tests[6,gold_name]="nordicstar_weltcup_segment.gpx"
tests[6,activity_name]="nordicstar_weltcup_activity_25_52.gpx"

### example - cropping
tests[7,name]="tdh1"
tests[7,dtw]=0.28447
tests[7,radius]=40
tests[7,t]=0:27:35
tests[7,gold_name]="tdh1_dv.gpx"
tests[7,activity_name]="tdh1_mg.gpx"

### example - no matching start/end points found
tests[8,name]="no_matching_endpoints"
tests[8,dtw]=0.1
tests[8,radius]=15
tests[8,t]=23:59:59
tests[8,gold_name]="tdh1_dv.gpx"
tests[8,activity_name]="tdu2a.gpx"

### loop through test cases
for idx in "${test_idx[@]}"; do

  echo Testing: ${tests[$idx,name]}

  python3 individual_tests.py \
    ${tests[$idx,gold_name]} \
    ${tests[$idx,activity_name]} \
    ${tests[$idx,dtw]} \
    ${tests[$idx,radius]} \
    ${tests[$idx,t]}

done
