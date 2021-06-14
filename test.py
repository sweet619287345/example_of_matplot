import signal
import pandas as pd
import math
import matplotlib.pyplot as plt
import sys


filename = sys.argv[1]
#pubcsv = pd.read_csv(filename)
pubcsv=pd.read_excel(filename)
n = [int(sys.argv[2]), int(sys.argv[3])]
time = [item for item in pubcsv.iloc[:, 1]]
time1 = []
for i in range(0, 3999):
    time1.append(time[i]*1000000)
for i in range(3999,len(time)):
    time1.append(time[i])

timeDiffer = []
y2 = []
sum = 0
for i in range((n[0]+1), (n[1]+1)):
        sum += ((time1[i] - time1[i-1]))
        timeDiffer.append((time1[i] - time1[i-1]))
        y2.append(250)

y1 = timeDiffer
average = float(sum/(n[1]-n[0]))

plt.axis([n[0], n[1], 0, 600])

plt.xticks([i for i in range(0, 12001, 1000)])
plt.yticks([i for i in range(0, 610, 50)])

plt.xlabel("package receive /times")
plt.ylabel("time for each interval /µs")
plt.title("%s\n Ave.%lf µs" % (sys.argv[4], average))

plt.grid(color="k", linestyle=":", axis="y")

plt.plot(y1, color="cornflowerblue", linestyle="-", linewidth=3, label="interval_is")
plt.plot(y2, color="gold", linestyle="-", linewidth=3, label="interval_set")


plt.legend(loc="upper right", bbox_to_anchor=(0.9, 0.95))
plt.savefig("/Users/apple/Real_time_test/rt_test_data/%s.png" % (sys.argv[4]))
plt.show()

sys.exit(0)
