#!/usr/bin/env python3

import sys

result = {}

for line in sys.stdin:
    key, sum_input, count_input = line.strip().split('\t')
    old_value = result.get(key)
    if old_value == None:
        sum = int(sum_input)
        count = int(count_input)
    else:
        sum = int(old_value[0])+int(sum_input)
        count = old_value[1]+1
    result.update({key: [sum, count]})

for key,value in result.items():
    avg = int(value[0])/int(value[1])
    print(f'{key}\t{avg}')