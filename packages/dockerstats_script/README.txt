OVERVIEW

- "ds_stats.sh": retrive docker stats for the simple SUT configuration (proxy+be+db) and write the result in a .csv file.
The parent directory where stats are collected is specified in the input by the user.
The full path where the files are written looks like : /${input_parentdir}/${componentdir}/
For example db1.csv, in the 128m named parent dir, will be written in /128m/db1/
(Note: mkdir in the .sh files are commented. You have to create the full path directories by hand or uncomment the code)

- "ds_stats_scale.sh": retrieve docker stats for be-scaled SUT configuration (proxy+be/be+db). The rest is the same bro.

-the data in the .csv files contains the mesuration (in column order) of: CPU(%), MEMUSAGE, MEM(%), DATE, TIME.
The first free are retrieved from docker stats whereas:
DATE is the time (nearly) when the command docker stats is executed.
TIME is a counter that is increased every iteration by the difference in seconds between dates of subsequent calls of docker stats. It starts from zero and at the end will match the test duration in seconds.

- "plot.py": plot data stored in the .csv files on all subdirectory of an input specified parent dir.
The genereted plot regards Cpu(%), Ram(MiB) and Ram(%) values over time

DEPENDENCIES
- pandas
- matplotlib
- maybe something else i dunno

HOW TO USE

- when launching the tsung load test launch also one of the 2 .sh scripts based on the SUT configuration (with commands "sh ds_stats.sh" for example)
- the .sh script will ask the user two inputs (so set up the inputs before launching tsung).
- the first input is the parent folder.

As said before make sure that the folder exists (or that the mkdir code is uncommented). 
If you are creating folder by hand make sure that also the subdirectory are there.
Subdirs are : (db1,backend1,nginx1) for the base SUT and (db1,backend1,backend2,nginx1) for the be-scaled SUT

- the second input is the load duration of the tsung test in seconds that corresponds to the time limit for the script. This will help the script automatically break out the loop when the time limit is reached (check against a time variable).
- last step is plotting the results. All you need to do is calling "python plot.py" that will ask you a parent directory and then easy plot 