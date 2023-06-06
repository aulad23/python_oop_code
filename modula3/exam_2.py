size = int(input());
good_sequence = [int(str_int) for str_int in input().split()];
map = {};
remove_times = 0;

for number in good_sequence :
    if(not map.get(number)):
        map[number] = 1;
    else:
        has = map[number];

        if(has >= number):
            remove_times += 1;
        else:
            map[number] += 1;
            
for number in good_sequence:
    has = map[number];

    if not has : continue;

    if has < number :
        remove_times += has;
        map[number] = 0;

print(remove_times);