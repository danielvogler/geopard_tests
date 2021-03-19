"""
Daniel Vogler
geopard test execution
"""

from geopard.geopard import Geopard
from matplotlib import pyplot as plt
import sys
import datetime
from datetime import timedelta

dtw_threshold=0.2

### passed arguments
gold_name = sys.argv[1]
activity_name = sys.argv[2]
benchmark_dtw = float(sys.argv[3])
radius = float(sys.argv[4])
t = datetime.datetime.strptime(sys.argv[5], '%H:%M:%S')
benchmark_time = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
folder_path = "./gpx_files/"

### initialize
gp = Geopard()

"""
Track matching
"""

### dtw matching of example segments/activities
geopard_response = gp.dtw_match(folder_path+gold_name,folder_path+activity_name,radius=radius,dtw_threshold=dtw_threshold)

if not geopard_response.is_success():
    print("\n----- Matching not successful -----")
    print("Error:" , geopard_response.error)
    exit(-1)

final_time = geopard_response.time
final_dtw = geopard_response.dtw
match_flag = geopard_response.match_flag
final_start_point = geopard_response.start_point
final_end_point = geopard_response.end_point

"""
Track plotting
"""

### load gold standard/baseline segment
gold = gp.gpx_loading(folder_path + gold_name)
### interpolate gold data
gold_interpolated = gp.interpolate(gold)

### load activity data to be edited
trkps = gp.gpx_loading(folder_path + activity_name)
### crop activity data to segment length
gpx_cropped = gp.gpx_track_crop(gold, trkps, radius)

### find potential start/end trackpoints - just for plotting
nn_start, nn_start_idx = gp.nearest_neighbours(gpx_cropped,gold[:4,0],radius)
nn_finish, nn_finish_idx = gp.nearest_neighbours(gpx_cropped,gold[:4,-1],radius)

### plot gpx tracks
fig = plt.figure(num=None, figsize=(200, 150), dpi=80, facecolor='w', edgecolor='k')
gp.gpx_plot(fig,nn_start,["NN Start Cropped","X","b"],1200)
gp.gpx_plot(fig,nn_finish,["NN Finish Cropped","P","b"],1200)
gp.gpx_plot(fig,trkps,["Activity",".","k"])
gp.gpx_plot(fig,gpx_cropped,["Activity Cropped","o","k"])
gp.gpx_plot(fig,gold,["Gold","o","r"])

### plot interpolated gpx tracks
fig = plt.figure(num=None, figsize=(200, 150), dpi=80, facecolor='w', edgecolor='k')
gp.gpx_plot(fig,gpx_cropped,["Activity Cropped","o","k"])
gpx_interpolated = gp.interpolate(gpx_cropped)
gp.gpx_plot(fig,gpx_interpolated.T,["Activity Interpolated",".","k"])
gp.gpx_plot(fig,gold,["Gold","o","r"])
gp.gpx_plot(fig,gold_interpolated.T,["Gold Interpolated",".","r"])

"""
Benchmark
"""

f = open('./output/benchmark.txt', 'a')
sys.stdout = f

print('\n\n--- Benchmark ---\n')
print('Benchmark gold:', gold_name)
print('Benchmark activity:', activity_name)

print('\nBenchmark time:', benchmark_time)
print('Computed time: ', final_time)
if final_time == benchmark_time:
    print("Time match:    " , final_time)
else:
    print("Time match:    Failed")

print('\nBenchmark DTW:', benchmark_dtw)
print('Computed DTW: ', final_dtw)
if (abs(benchmark_dtw-final_dtw)/benchmark_dtw) < 0.01:
    print("DTW match:    " , final_dtw)
else:
    print("DTW match:    Failed")


f.close()

exit()
