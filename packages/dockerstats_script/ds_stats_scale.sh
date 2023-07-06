echo "Insert parent destination folder: "
read folder;
echo "Insert load duration(sec): "
read loadDuration;

: ' 
mkdir -p /${folder}/db1;
mkdir -p /${folder}/backend1;
mkdir -p /${folder}/nginx1;
mkdir -p /${folder}/backend2;
'

d1=$(date +%s);
d2=$(date +%s);
timetemp=0;
while true; 
do
	d2=$(date +%s);
	time=$((d2-d1+timetemp));
	d1=$(date +%s);
	var=$(docker stats --no-stream );
	echo "$var" | grep server-db-1 | awk -v date="$(date +%T)" -v time=$time '{ if(index($4, "GiB")) {gsub("GiB","",$4); print $3","$4 * 1000","$7","date","time } else {gsub("MiB","",$4); print $3","$4","$7","date","time}}'| sed -e 's/MiB//g'| sed -e 's/GiB//g' | sed -e 's/%//g' >> ${folder}/db1/db1.csv; 
	echo "$var" | grep server-backend-1 | awk -v date="$(date +%T)" -v time=$time '{ if(index($4, "GiB")) {gsub("GiB","",$4); print $3","$4 * 1000","$7","date","time } else {gsub("MiB","",$4); print $3","$4","$7","date","time}}'| sed -e 's/MiB//g'| sed -e 's/GiB//g' | sed -e 's/%//g' >> ${folder}/backend1/backend1.csv;
	echo "$var" | grep server-backend-2 | awk -v date="$(date +%T)" -v time=$time '{ if(index($4, "GiB")) {gsub("GiB","",$4); print $3","$4 * 1000","$7","date","time } else {gsub("MiB","",$4); print $3","$4","$7","date","time}}'| sed -e 's/MiB//g'| sed -e 's/GiB//g' | sed -e 's/%//g' >> ${folder}/backend2/backend2.csv;  
	echo "$var" | grep server-nginx-1 | awk -v date="$(date +%T)" -v time=$time '{ if(index($4, "GiB")) {gsub("GiB","",$4); print $3","$4 * 1000","$7","date","time } else {gsub("MiB","",$4); print $3","$4","$7","date","time}}'| sed -e 's/MiB//g'| sed -e 's/GiB//g' | sed -e 's/%//g' >> ${folder}/nginx1/nginx1.csv; 
	timetemp=$time;
	if [ $timetemp -gt $loadDuration ] || [ $timetemp -eq $loadDuration ]
	then
		break;
	fi
done