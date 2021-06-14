import signal
import pandas as pd
import sys
import math

filename = sys.argv[1]
pubcsv = pd.read_csv(filename)
n = [int(sys.argv[2]), int(sys.argv[3])]

time = [item for item in pubcsv.iloc[:, 1]]

timeDiffer = []
y2 = []
jitter = 0
TimeJitter ={'packetNumber':[],'Timestamp':[],'Jitter':[],'JitterDiffer':[]}
sum = 0
for i in range((n[0]), (n[1])):
    interval = int(time[i]* 1000000 - time[i - 1]* 1000000)
    sum += interval
    timeDiffer.append(interval)
    if abs(interval - 250) > 50:
        jitter += 1
        TimeJitter['Timestamp'].append(time[i])
        TimeJitter['Jitter'].append(interval)
        TimeJitter['JitterDiffer'].append(interval - 250)
        TimeJitter['packetNumber'].append(i)
    y2.append(250)

y1 = timeDiffer
print("the rate is: %lf" %(100-(jitter *100/ (n[1] - n[0]))))
dataframe = pd.DataFrame(TimeJitter)
dataframe.to_csv("c:\\Users\\Snow\\Downloads\\test_without_kunbus\\%s.csv" % sys.argv[4], index=False, sep=',', encoding='utf-8')
print(TimeJitter)
