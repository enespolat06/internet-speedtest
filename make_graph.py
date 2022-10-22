import matplotlib.pyplot as plt
import csv
import matplotlib.ticker as ticker
times = []
download = []
upload = []

with open('test2.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        times.append(str(row[0]))
        download.append(float(row[1]))
        upload.append(float(row[2]))
	

print(times, "\n", download, "\n", upload)

plt.figure(figsize=(30, 30))
plt.plot(times, download, label='download', color='r')
plt.plot(times, upload, label='upload', color='b')
plt.xlabel('time')
plt.ylabel('speed in Mb/s')
plt.title("internet speed")
plt.legend()
plt.savefig('test_graph2.jpg', bbox_inches='tight')


