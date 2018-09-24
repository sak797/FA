def insertion_sort(lis):
    length = len(lis)
    for x in range(2, length):
        prev = x-1
        key = lis[x]
        while prev>=0 and key <= lis[prev]:
            lis[prev+1] = lis[prev]
            prev = prev -1
        lis[prev+1] = key
    return lis

def merge(l,r):
    start_l = 0
    start_r = 0
    count = 0
    res = []
    while count < len(l) + len(r):
        if start_l < len(l) and start_r <len(r):
            if l[start_l] <= r[start_r]:
                res.append(l[start_l])
                start_l += 1
                count += 1
            elif l[start_l] > r[start_r]:
                res.append(r[start_r])
                start_r += 1
                count += 1
        if start_r == len(r):
            res.append(l[start_l])
            start_l += 1
            count += 1
        elif start_l == len(l):
            res.append(r[start_r])
            start_r += 1
            count += 1
    return res

def merge_sort(lis):
    if len(lis) == 1:
        return lis
    if len(lis) > 1:
        mid = len(lis)//2
        return merge(merge_sort(lis[:mid]), merge_sort(lis[mid:]))
    return []

def count_sort(input_array, range_input):
    output = [0]*len(input_array)
    count = [0]*range_input
    # Count
    for number in input_array:
        count[number] +=1
    # cumulative sum
    for ind in range(1,range_input):
        count[ind] += count[ind-1]
    # Keep the output at correct place
    for ind in range(len(input_array)-1, -1, -1):
        output[count[input_array[ind]]-1] = input_array[ind]
        count[input_array[ind]] -= 1
    return output

if __name__ == '__main__':
    lis = [4, 5, 2, 3, 9, 1]
    sort_lis = insertion_sort(lis)
    print(sort_lis)
    lis = [4, 5, 2, 3, 9, 1]
    sort_lis = merge_sort(lis)
    print(sort_lis)
    lis = [4, 5, 2, 3, 9, 1]
    sort_lis = count_sort(lis,11)
    print(sort_lis)