size = int(input());
odd_found = False;
operation_times = 0;

number_list = [int(str_int) for str_int in input().split()];
i = 0;
while not odd_found:
    for num in number_list:
        if(num & 1) :
            odd_found = True;
            break;
        number_list[i] = int(num/2);
        i+=1;
    i = 0;
    if not odd_found : 
        operation_times += 1;

print(operation_times)