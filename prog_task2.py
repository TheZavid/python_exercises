histogram = dict()
cur_count = 0

while True:
    try:
        line = input().split()
        for word in line:
            cur_count += 1
            if '.' in word:
                if cur_count in histogram:
                    histogram[cur_count] += 1
                else:
                    histogram[cur_count] = 1
                cur_count = 0
    except:
        histogram = dict(sorted(histogram.items(), key = lambda item: item[1]))
        for key, val in histogram.items():
            output = ''
            if val == 1:
                output = str(val) + ' sentence '
            else:
                output = str(val) + ' sentences '
            print(output + 'with ' + str(key) + ' words')
        break


# It          was a summer          day. Alice was sitting
# by            the river with her sister.             Her sister was
# reading           a book
# with no              pictures. Then
# Alice saw something peculiar. It           was
# a           rabbit.
