import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

folder=input("Enter the desired folder: ")
headers = ['cpu', 'mem', 'mempercent','date',"time"]

try:
	df_db = pd.read_csv(folder+'/db1/db1.csv', names=headers)
	df_backend= pd.read_csv(folder+'/backend1/backend1.csv', names=headers)
	df_nginx= pd.read_csv(folder+'/nginx1/nginx1.csv', names=headers)

	#plot db data

	print("plotting Database Cpu usage (%) ...")
	plt.title("Cpu")
	plt.xlabel('Time (sec)') 
	plt.ylabel('Cpu (%)')
	plt.plot(df_db["time"],df_db["cpu"])
	plt.savefig(folder+'/db1/cpuplot.png')
	plt.clf()

	print("plotting Database Ram usage (Mib) ...")
	plt.title("Ram Usage")
	plt.xlabel('Time (sec)') 
	plt.ylabel('Ram (MiB)')
	plt.plot(df_db["time"],df_db["mem"])
	plt.savefig(folder+'/db1/ramplot.png')
	plt.clf()

	print("plotting Database Ram usage (%) ...")
	plt.title("Ram")
	plt.xlabel('Time (sec)') 
	plt.ylabel('Ram (%)')
	plt.plot(df_db["time"],df_db["mempercent"])
	plt.savefig(folder+'/db1/rampercentplot.png')
	plt.clf()
	#########################################################################

	#plot backend data
	print("plotting Backend Cpu usage (%) ...")
	plt.title("Cpu")
	plt.xlabel('Time (sec)') 
	plt.ylabel('Cpu (%)')
	plt.plot(df_backend["time"],df_backend["cpu"])
	plt.savefig(folder+'/backend1/cpuplot.png')
	plt.clf()

	print("plotting Backend Ram usage (Mib) ...")
	plt.title("Ram Usage")
	plt.xlabel('Time (sec)') 
	plt.ylabel('Ram (MiB)')
	plt.plot(df_backend["time"],df_backend["mem"])
	plt.savefig(folder+'/backend1/ramplot.png')
	plt.clf()

	print("plotting Backend Ram usage (%) ...")
	plt.title("Ram")
	plt.xlabel('Time (sec)') 
	plt.ylabel('Ram (%)')
	plt.plot(df_backend["time"],df_backend["mempercent"])
	plt.savefig(folder+'/backend1/rampercentplot.png')
	plt.clf()
	##########################################################################

	#plot nginx data
	print("plotting Proxy Cpu usage (%) ...")
	plt.title("Cpu")
	plt.xlabel('Time (sec)') 
	plt.ylabel('Cpu (%)')
	plt.plot(df_nginx["time"],df_nginx["cpu"])
	plt.savefig(folder+'/nginx1/cpuplot.png')
	plt.clf()

	print("plotting Proxy Ram usage (Mib) ...")
	plt.title("Ram Usage")
	plt.xlabel('Time (sec)') 
	plt.ylabel('Ram (MiB)')
	plt.plot(df_nginx["time"],df_nginx["mem"])
	plt.savefig(folder+'/nginx1/ramplot.png')
	plt.clf()

	print("plotting Proxy Ram usage (%) ...")
	plt.title("Ram")
	plt.xlabel('Time (sec)') 
	plt.ylabel('Ram (%)')
	plt.plot(df_nginx["time"],df_nginx["mempercent"])
	plt.savefig(folder+'/nginx1/rampercentplot.png')
	plt.clf()
except Exception as e:
	print("Stats file (*.csv) needed")
	print("Check for Database, Backend or Proxy subdirecotry existence")
	print(e)

###backend scaling#####
try:
	df_backend= pd.read_csv(folder+'/backend2/backend2.csv', names=headers)

	print("plotting replicated Backend Cpu usage (%) ...")
	plt.title("Cpu")
	plt.xlabel('Time (sec)') 
	plt.ylabel('Cpu (%)')
	plt.plot(df_backend["time"],df_backend["cpu"])
	plt.savefig(folder+'/backend2/cpuplot.png')
	plt.clf()

	print("plotting replicated Backend Ram usage (Mib) ...")
	plt.title("Ram Usage")
	plt.xlabel('Time (sec)') 
	plt.ylabel('Ram (MiB)')
	plt.plot(df_backend["time"],df_backend["mem"])
	plt.savefig(folder+'/backend2/ramplot.png')
	plt.clf()

	print("plotting replicated Backend Ram usage (%) ...")
	plt.title("Ram")
	plt.xlabel('Time (sec)') 
	plt.ylabel('Ram (%)')
	plt.plot(df_backend["time"],df_backend["mempercent"])
	plt.savefig(folder+'/backend2/rampercentplot.png')
	plt.clf()

except Exception as e:
	print("No BackEnd scaling for this configuration")
	print(e)
