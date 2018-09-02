'''Extract datetimes from log entries and calculate the time
between the first and last shutdown events'''

from datetime import datetime
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# read in the log file
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)
with open(logfile) as f:
    loglines = f.readlines()


def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime
       object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    timestamp = re.findall(r'\d{4}-\d{2}-\w+:\d{2}:\d{2}', line)
    timestamp_fmt = re.sub('T', ' ', timestamp[0])
    # print('Found timestamp: ', timestamp_fmt)
    # print(datetime.strptime(timestamp_fmt, "%Y-%m-%d %H:%M:%S"))
    d = datetime.strptime(timestamp_fmt, "%Y-%m-%d %H:%M:%S")
    return d


def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object.'''
    lines = []
    for line in loglines:
        if 'Shutdown initiated' in line:
            lines.append(line)

    delta = convert_to_datetime(lines[len(lines)-1]) - convert_to_datetime(lines[0])
    # print(delta)
    return delta


for line in loglines:
    convert_to_datetime(line)

time_between_shutdowns(loglines)
