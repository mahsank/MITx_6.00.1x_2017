'''
mplement a function that meets the specifications below.

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    # Your code here
For example,

max_val((5, (1,2), [[1],[2]])) returns 5.
max_val((5, (1,2), [[1],[9]])) returns 9.

'''

def max_val(t):
    """ t, tuple
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    deflate_list = []
    for j in t:
        if isinstance(j, list):
            temp = flatten(j)
            deflate_list += temp
        elif isinstance(j, tuple):
            temp_list = [ list(x) if type(x) != int else x for x in j]
            temp = flatten(temp_list)
            deflate_list += temp
        else:
            deflate_list.append(j)
    return max(deflate_list)

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    if aList == []:
        return aList
    if isinstance(aList[0], list):
            return flatten(aList[0]) + flatten(aList[1:])
    else:
        return aList[:1] + flatten(aList[1:])

