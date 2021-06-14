import signal
import pandas as pd
import math
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
        y2.append(100000)

y1 = timeDiffer
average = float(sum/(n[1]-n[0]))

plt.axis([n[0], n[1], 0, 500100])

plt.xticks([i for i in range(0, n[1]-n[0]+4, 5)])
plt.yticks([i for i in range(0, 500100, 50000)])

plt.xlabel("Number of received package[-]")
plt.ylabel("time for each interval [µs]")
plt.title("%s" % (sys.argv[4]))

plt.grid(color="silver", linestyle=":", axis="y")
plt.grid(color="silver", linestyle=":", axis="x")

plt.plot(y1, color="royalblue", linestyle="-", linewidth=1, label="interval_is")
plt.plot(y2, color="gold", linestyle="-", linewidth=2, label="interval_set")


plt.legend(loc="upper right", bbox_to_anchor=(0.9, 0.97))
plt.savefig("/Users/apple/Real_time_test/rt_test_data/%s.png" % (sys.argv[4]))
plt.show()

sys.exit(0)













