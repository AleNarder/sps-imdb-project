import matplotlib.pyplot as plt
import pandas as pd
import argparse
from colorama import init, Fore, Back, Style

# Initializes Colorama
init(autoreset=True)

parser = argparse.ArgumentParser()
parser.add_argument('foldername', help = "Stats Directory")
args = parser.parse_args()

def change_unit(x, pos):
	# global measurement_unit

	# Since Data is expressed in KB
	if x >= 1000000:
		# measurement_unit = "GB"
		return f"{x/1000000:.1f}"
	elif x >= 1000:
		# measurement_unit = "MB"
		return f"{x/1000:.1f}"
	else:
		# measurement_unit = "KB"
		return f"{x:.1f}"

def set_m_unit(x):
	if x >= 1000000:
		return "GB"
	elif x >= 1000:
		return "MB"
	else:
		return "KB"

containers = ["db1", "backend1", "nginx1", "backend2", "backend3"]
colors=["red","blue","green","yellow","black"]
df_merge=[]


components = {"CPU" : ["CPU (%)", "cpu"],
	      	  "RAM" : ["RAM (MiB)", "mem"],
	          "RAM_percent" : ["RAM (%)", "mempercent"],
			  "Block_I" : ["Block Input", "blockI"],
			  "Block_O" : ["Block Output", "blockO"],
			  "PIDS" : ["PIDS", "pids"]}

headers = ['cpu','mem','mempercent','blockI','blockO','pids','date','time']

try:
	for container in containers:
		df = pd.read_csv(f"{args.foldername}/{container}/{container}.csv", names=headers)
		df_merge.append(df)
		for key, value in components.items():
			print(f"plotting {container} {value[0]} usage ...")
			plt.title(value[0])
			plt.xlabel('Time (sec)') 
			plt.ylabel(value[0])
			plt.plot(df['time'], df[value[1]])

			if key == "Block_I" or key == "Block_O":
				ax = plt.gca()
				ax.yaxis.set_major_formatter(change_unit)
				measurement_unit = set_m_unit(df[value[1]].max())
				# and update the plot title with the correct measurement unit
				plt.title(f"{value[0]} ({measurement_unit})")
				
			plt.savefig(f"{args.foldername}/{container}/{key}plot.svg")
			plt.clf()

except Exception as e:
	print(Fore.YELLOW + "Stats file (*.csv) needed \nCheck for Database, Backend or Proxy subdirecotry existence")
	print(Fore.RED + str(e))
	pass


# Create comparison plots
for key, value in components.items():
	print(f"plotting Comparison Plots: {value[0]}")
	plt.title(value[0])
	plt.xlabel('Time (sec)') 
	plt.ylabel(value[0])
	index = 0
	max = 0
	for df in df_merge:
		plt.plot(df['time'], df[value[1]], color=colors[index], label=containers[index])
		max = df[value[1]].max() if max < df[value[1]].max() else max
		index += 1
	plt.legend(loc="center right")

	if key == "Block_I" or key == "Block_O":
		ax = plt.gca()
		ax.yaxis.set_major_formatter(change_unit)
		measurement_unit = set_m_unit(max)
		plt.title(f"{value[0]} ({measurement_unit})")

	plt.savefig(f"{args.foldername}/comparison_plots/{key}plot.svg")
	plt.clf()