# find the longest train run time
from collections import defaultdict
from datetime import datetime, timedelta
filename = 'input34.txt'
#filename = 'test34.txt'

# read in our input
with open(filename) as f:
    ls = f.read().strip().split('\n')
train_schedule = defaultdict(list)
train_names = ls.pop(0).split(',')
train_names.pop(0) # first is a non-train label
station_names = []
for l in ls:
    station_info = l.split(',')
    station_name = station_info.pop(0)
    station_names.append(station_name)
    for i, t in enumerate(station_info):
        if t != '':
            hour, min = tuple(map(int, t.split(':')))
            train_time = datetime.now().replace(hour=hour, minute=min,
                                              second=0, microsecond=0)
            if len(train_schedule[train_names[i]]) < 1:
                train_schedule[train_names[i]].append(['N',
                                                       station_name,
                                                       train_time])
            else:
                last_station = train_schedule[train_names[i]][-1][1]
                train_schedule[train_names[i]].append([last_station,
                                                       station_name,
                                                       train_time])

# setup to loop through each minute of time
cur_time = datetime.now().replace(hour=0, minute=0,
                                              second=0, microsecond=0)
station_queues = defaultdict(list)
# the train on the platform will have a 5 second timer
station_platforms = dict()
train_statuses = defaultdict(list)
done = False
while not done:
    # ARRIVE
    for train in train_schedule.keys():
        if len(train_schedule[train]) > 0:
            last_station, station_name, train_time = train_schedule[train][0]
            if train_time == cur_time:
                # move to queued
                station_queues[station_name].append([last_station, train])
                train_statuses[train].append([cur_time, 'arrive',
                                              station_name])
    # QUEUE
    #  trains from lower stations have priority, else FIFO
    for station in station_queues.keys():
        station_queues[station].sort(key=lambda x: x[0])
    # DEPART
    #  even though enter is said to come next, trains seem to depart first
    # We will also update how late we are when leaving and remove the
    #  completed leg of the journey
    to_remove = []
    for platform in station_platforms.keys():
        station_platforms[platform][0] += 1
        if station_platforms[platform][0] == 5:
            # update this train status with new delay, remove station and
            #  update schedule
            train = station_platforms[platform][1]
            cur_delay = cur_time - train_schedule[train][0][2]
            train_schedule[train].pop(0)
            for train_stop in train_schedule[train]:
                train_stop[2] += cur_delay
            to_remove.append(platform)
            train_statuses[train].append([cur_time, 'depart', platform])
    for p in to_remove:
        del station_platforms[p]
    # ENTER
    for station in station_queues.keys():
        if station not in station_platforms and \
            len(station_queues[station]) > 0:
            train = station_queues[station][0][1]
            station_platforms[station] = [0, train]
            station_queues[station].pop(0)
            train_statuses[train].append([cur_time, 'enter', station])
    # check if all trains are done
    done = True
    for train in train_schedule.keys():
        if len(train_schedule[train]) > 0:
            done = False
            break
    cur_time += timedelta(minutes=1)

# find longest
longest = timedelta(minutes=0)
for train in train_statuses.keys():
    end_time = train_statuses[train][-1][0]
    start_time = train_statuses[train][0][0]
    duration = end_time - start_time
    if duration > longest:
        longest = duration
print("longest run was", longest.total_seconds() / 60)
