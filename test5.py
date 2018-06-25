

def diff_of_element_list(lst, k):

    newlst = [i + k for i in lst]
    # print newlst
    return len(set(lst) & set(newlst))


if __name__ == '__main__':

    n, k = raw_input().split()
    lst = raw_input().split()
    lst = [int(i) for i in lst]
    # diff_of_element_list(lst, int(k))
    print(diff_of_element_list(lst, int(k)))


"""
def diff_of_element_list(lst, k):

    # newlst = [i + k for i in lst]
    newlst = lst+k
    return len(set(lst) & set(newlst))


if __name__ == '__main__':

    n, k = raw_input().split()
    lst = raw_input().split()
    lst = [int(i) for i in lst]
    print(diff_of_element_list(lst, int(k)))
"""

