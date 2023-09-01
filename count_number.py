def count_number(number,thislist):
    count=0
    for x in thislist:
        if x is number:
            count=count+1
    print(count)

thislist=[1,4,6,7,4]
count_number(4,thislist)