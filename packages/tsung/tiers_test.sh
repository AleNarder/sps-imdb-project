#!/bin/sh

for i in $(seq 1 5);
do
    task run:tsung:db_test
    task run:tsung:db+be_test
    task run:tsung:db+be+rp_test
done

for i in $(seq 1 3);
do
    task run:tsung:bottleneck_test
done