#!/bin/sh

find ./logs/ -mindepth 2\
             -maxdepth 3\
             -type d\
             -name '2023*'\
             -exec sh\
             -c 'cd "{}" && pwd && if [ ! -f ./report.html ]; then
                                        if [[ $OSTYPE == 'darwin'* ]]; then
                                             /usr/local/Cellar/tsung/1.8.0/lib/tsung/bin/tsung_stats.pl
                                        else
                                             /usr/lib/x86_64-linux-gnu/tsung/bin/tsung_stats.pl;
                                        fi;
                                   fi;' \;