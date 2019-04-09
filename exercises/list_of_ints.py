"""
Exercise: create a function that takes an int parameter. 
Generate an unordered list of the lenght of the parameter.
Run a script like word_count.py where you use this module to 
generate lists and test the algorithms we worked and will work with
"""
import sys
import random
import time


def list_of_ints(num):
    """ Generates an unordered list of ints of the length of 'num'
        Takes a number parameter
        Returns: lists of unordered numbers where all numbers from 0-num are represented """
    list = []
    for i in range(num):
        list.append(i)

    for i in range(num-1):
        temp_1 = random.randint(0, num-1)
        temp_2 = random.randint(0, num-1)

        list[temp_1], list[temp_2] = list[temp_2], list[temp_1]

    return list

def list_of_benj(num):
    
    list = []
    while len(list) != num:
        newnum = random.randint(0, num)
        if newnum not in list:
            list.append(newnum)

    return list
    
def list_of_tobias(num):
    list = []
    i = 0
    while i < num:
        rand = random.randint(1, num)
        if rand not in list:
            list.append(rand)
            i += 1

    return list



def main():
    
    start = time.time()
    list_of_ints(int(sys.argv[1]))
    end = time.time()
    print('The list_of_ints execusion time was', format(end - start, '.6f'), 'seconds')

    start = time.time()
    list_of_benj(int(sys.argv[1]))
    end = time.time()
    print('The list_of_benj execusion time was', format(end - start, '.6f'), 'seconds')

    start = time.time()
    list_of_tobias(int(sys.argv[1]))
    end = time.time()
    print('The list_of_tobias execusion time was', format(end - start, '.6f'), 'seconds')

    

    

    #except IndexError:
       # print('You need to specify the an argument (length of the list to be generated)')
       # print('ie. ($ python list_of_ints.py 100)')


if __name__ == "__main__":
    main()
