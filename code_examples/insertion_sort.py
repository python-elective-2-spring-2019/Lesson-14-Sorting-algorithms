# Traverse through 1 to len(l)

def insertion_sort(l):

    for i in range(1, len(l)):
        print(l)
        key = l[i]  # = 5

        j = i-1  # 2

        while j >= 0 and key < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key

# Driver code to test above
l = [12, 11, 13, 5, 6]

insertion_sort(l)

for i in range(len(l)):
    pass
    # print (f'{l[i]}')
