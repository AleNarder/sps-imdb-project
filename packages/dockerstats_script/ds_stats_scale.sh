echo "Insert parent destination folder: "
read folder;
echo "Insert load duration(sec): "
read loadDuration;


mkdir -p ${folder}/db1;
mkdir -p ${folder}/backend1;
mkdir -p ${folder}/nginx1;
mkdir -p ${folder}/backend2;
mkdir -p ${folder}/backend3;

d1=$(date +%s);
d2=$(date +%s);
timetemp=0;
while true; 
do
	d2=$(date +%s);
	time=$((d2-d1+timetemp));
	d1=$(date +%s);
	var=$(docker stats --no-stream );

	declare -A arr=( ["server-db-2"]="db1" ["server-backend-1"]="backend1" ["server-nginx-1"]="nginx1" ["server-backend-2"]="backend2" ["server-backend-3"]="backend3")

	## now loop through the above array
	for i in "${arr[@]}"
	do
		echo "$var" | grep "$i"| awk -v date="$(date +%T)" -v time=$time -v binput=0 -v boutput=0 '{
		if(index($11,"B")){gsub("B","",$11); binput=$11/1000000;}
		if(index($11,"kB")){gsub("kB","",$11); binput=$11/1000;}
		if(index($11,"MiB")){gsub("MiB","",$11); binput=$11;}
		if(index($11,"GiB")){gsub("GiB","",$11); binput=$11*1000;}
		if(index($13,"B")){gsub("B","",$13); boutput=$13/1000;}
		if(index($13,"kB")){gsub("kB","",$13); boutput=$13;}
		if(index($13,"MiB")){gsub("MiB","",$13); boutput=$13*1000;}
		if(index($13,"GiB")){gsub("GiB","",$13); boutput=$13*1000000;}
		if(index($4, "GiB")) 
		{gsub("GiB","",$4); print $3","$4 * 1000","$7","binput","boutput","date","time } 
		else {gsub("MiB","",$4); print $3","$4","$7","binput","boutput","date","time}}'| sed -e 's/MiB//g'| sed -e 's/GiB//g' | sed -e 's/%//g' >> ${folder}/${array[$i]}/${array[$i]}.csv; 
	done

	timetemp=$time;
	if [ $timetemp -gt $loadDuration ] || [ $timetemp -eq $loadDuration ]
	then
		python3 ./plot.py ${folder};
		break;
	fi
done