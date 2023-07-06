echo "Insert parent destination folder: "
read folder;
echo "Insert load duration(sec): "
read loadDuration;


mkdir -p ${folder}/db1;
mkdir -p ${folder}/backend1;
mkdir -p ${folder}/nginx1;
mkdir -p ${folder}/backend2;


d1=$(date +%s);
d2=$(date +%s);
timetemp=0;
while true; 
do
	d2=$(date +%s);
	time=$((d2-d1+timetemp));
	d1=$(date +%s);
	var=$(docker stats --no-stream );
	echo "$var" | grep server-db-1 | awk -v date="$(date +%T)" -v time=$time -v binput=0 -v boutput=0 '{
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
	else {gsub("MiB","",$4); print $3","$4","$7","binput","boutput","date","time}}'| sed -e 's/MiB//g'| sed -e 's/GiB//g' | sed -e 's/%//g' >> ${folder}/db1/db1.csv; 
	echo "$var" | grep server-backend-1 | awk -v date="$(date +%T)" -v time=$time -v binput=0 -v boutput=0 '{
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
	else {gsub("MiB","",$4); print $3","$4","$7","binput","boutput","date","time}}' | sed -e 's/MiB//g'| sed -e 's/GiB//g' | sed -e 's/%//g' >> ${folder}/backend1/backend1.csv; 
	echo "$var" | grep server-backend-2 | awk -v date="$(date +%T)" -v time=$time -v binput=0 -v boutput=0 '{
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
	else {gsub("MiB","",$4); print $3","$4","$7","binput","boutput","date","time}}' | sed -e 's/MiB//g'| sed -e 's/GiB//g' | sed -e 's/%//g' >> ${folder}/backend2/backend2.csv; 
	
	echo "$var" | grep server-nginx-1 | awk -v date="$(date +%T)" -v time=$time -v binput=0 -v boutput=0 '{
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
	else {gsub("MiB","",$4); print $3","$4","$7","binput","boutput","date","time}}' | sed -e 's/MiB//g'| sed -e 's/GiB//g' | sed -e 's/%//g' >> ${folder}/nginx1/nginx1.csv; 
	timetemp=$time;
	if [ $timetemp -gt $loadDuration ] || [ $timetemp -eq $loadDuration ]
	then
		break;
	fi
done