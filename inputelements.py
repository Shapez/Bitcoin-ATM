def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    new_list = []
    for item in list1:
        if item not in new_list:
            new_list.append(item)
    return new_list

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    intersect = []
    for item in list1:
        if item in list2:
            intersect.append(item)
    return intersect

def merge(list1, list2):
    """
     return a new sorted list that contains all of the elements in either list1 and list2.
     """
    sorted_list = []
    for item in list1:
        sorted_list.append(item)
    for item in list2:
        if item not in sorted_list:
            sorted_list.append(item)
    return sorted_list

def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) < 2:
        return list1
    else:
        mid = len(list1) // 2
        return merge(merge_sort(list1[:mid]), merge_sort(list1[mid:]))

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    word_list = []
    if len(word) <= 1:
        return ['', word]
    else:
        first = word[0]
        rest = word[1:]
        rest_strings = gen_all_strings(rest)
        for word in rest_strings:
            for letter in range(len(word) + 1):
                new_string = word[:letter] + first + word[letter:]
                word_list.append(new_string)
        return rest_strings + word_list

            
testlist = []  
testlist2 = []
testsort = merge(testlist, testlist2)
gentest = 'Missy the cat'
print gen_all_strings(gentest)

        

