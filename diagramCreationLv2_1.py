import signal
import pandas as pd
import math
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt
import sys
plt.rcParams['figure.figsize'] = (8.0, 7.0)


filename = sys.argv[1]
pubcsv = pd.read_csv(filename)
#pubcsv=pd.read_excel(filename)
n = [int(sys.argv[2]), int(sys.argv[3])]
# number = [2]
# for item in n.split(","):
    # number = int(n)

#pubcsv = pd.read_csv("/Users/apple/Real_time_test/rt_test_data/pub2.csv")

time = [item for item in pubcsv.iloc[:, 1]]

timeDiffer = []
y2 = []
sum = 0
for i in range((n[0]), (n[1])):
        sum += ((time[i] - time[i-1])*1000000)
        timeDiffer.append((time[i] - time[i-1])*1000000)
        y2.append(250)

y1 = timeDiffer
average = float(sum/(n[1]-n[0]))
#x3 = [i for i in range(n[0], n[1]+1, int((n[1]-n[0])/60))]
#y3 = [(time[i]) for i in range(n[0], n[1]+1, int((n[1]-n[0])/60))]

## Plot setting
fig, host = plt.subplots()
#host = host_subplot(111, axes_class=AA.Axes)
#plt.subplots_adjust(right=0.75)
par1 = host.twiny()
#new_fixed_axis = par1.get_grid_helper().new_fixed_axis
#par1.axis["top"] = new_fixed_axis(loc="top", axes=par1, offset=(0, 0))

host.set_xlim(0, 12000)
host.set_ylim(0, 600)

host.set_xlabel("Number of received packet [-]")
host.set_ylabel("Time duration for each packet [µs]")

host.set_xticks([i for i in range(0, n[1]-n[0]+1, int((n[1]-n[0])/12))])
host.set_yticks([i for i in range(0, 610, 50)])
for i in range(0, n[1]-n[0]+1, int((n[1]-n[0])/12)):
    host.annotate(s='%.6f'%time[i+n[0]], xy=(i, time[i+n[0]]), xytext=(i, 20), rotation=45, color="mediumseagreen")

par1.set_xlim(time[n[0]], time[n[1]])

#par1.set_xticks([(time[i]) for i in range(n[0], n[1]+1, int((n[1]-n[0])/12))])
for label in par1.xaxis.get_ticklabels():
    label.set_color("mediumseagreen")
par1.set_xlabel("Timestamp of received packet [s]", color="mediumseagreen")
#par1.grid(color="mediumturquoise", linestyle="--", axis="x")
host.set_title("%s\n Ave. %lf µs" % (sys.argv[4], average))

host.grid(color="silver", linestyle=":", axis="y")
host.grid(color="silver", linestyle=":", axis="x")

p1 = host.plot(y1, color="royalblue", linestyle="-", linewidth=1, label="interval_is")
p2 = host.plot(y2, color="gold", linestyle="-", linewidth=2, label="interval_set")
#p3 = par1.scatter(x3,y3, color="lightseagreen", s=5, marker=".")

host.legend(loc="upper right", bbox_to_anchor=(0.9, 0.95))

plt.draw()
plt.savefig("/Users/apple/Real_time_test/rt_test_data/%s.png" % (sys.argv[4]))
plt.show()

sys.exit(0)













