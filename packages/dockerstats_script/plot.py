import matplotlib.pyplot as plt
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('foldername', help = "Stats Directory")
args = parser.parse_args()

containers = ["db1", "backend1", "nginx1", "backend2", "backend3"]
components = {"CPU" : ["CPU (%)", "cpu"], "RAM" : ["RAM (MiB)", "mem"], "RAM_percent" : ["RAM (%)", "mempercent"]}

try:
	for container in containers:
		headers = ['cpu', 'mem', 'mempercent','blockI','blockO', 'date',"time"]

		df = pd.read_csv(args.foldername + '/' + container + '/' + container + '.csv', names=headers)
		for key, value in components.items():
			print("plotting Database " + value[0] + " usage ...")
			plt.title(value[0])
			plt.xlabel('Time (sec)') 
			plt.ylabel(value[0])
			plt.plot(df["time"], df[value[1]])
			plt.savefig(args.foldername + '/' + container + '/' + key + 'plot.png')
			plt.clf()

except Exception as e:
	print("Stats file (*.csv) needed")
	print("Check for Database, Backend or Proxy subdirecotry existence")
	print(e)