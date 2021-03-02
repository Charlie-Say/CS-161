import random
from random import randint


def create_random_tuple():
    '''
    function to make random tuple
    '''
    mytuple = tuple(i for i in (randint(0, 101) for x in range(randint(10, 21))))
    return(mytuple)


def choose_random(sometuple):
    '''
    function to take tuple as argument and returns a random element from it
    '''

    rand_tuple = create_random_tuple()
    rand_element = random.choice(rand_tuple)
    return(rand_element)


def has_common_element(list1, list2):
    '''
    compare two lists and returns true if there is a common element
    '''
    same_num = set(list1).intersection(list2)
    if len(same_num) == 0:
        print('Doesn\'t have a common integer.')
        return(False)
    else:
        print('Has a common integer.')
        return(True)


def filter_even(list):
    '''
    function that takes in a list and filters out the even integers
    even if there are string elements in the list and returns the
    new list with only odd integers
    '''
    odd_list = [i for i in list if isinstance(i, int) if i % 2 != 0]
    return(odd_list)

