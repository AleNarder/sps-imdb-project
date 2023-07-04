#!/bin/sh

for i in $(seq 1 10);
do
    task run:tsung:db_test
    task run:tsung:db+be_test
    task run:tsung:db+be+rp_test
    # task run:tsung:bottleneck_test
done
