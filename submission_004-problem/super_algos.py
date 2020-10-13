"""Send in a list of integer elements, the length of the list and the maximum integer
value as parameters. This function will return the minimum value element in the list."""
# def find_min(element, count, min_num):
#     """TODO: complete for Step 1"""
#     while count >= 0:
#         if str(element[count]).isdigit() == False or element[count] == "":
#             return -1
#         if element[count] < min_num:
#             min_num = element[count]
#         return find_min(element, count - 1, min_num)
#     return min_num


"""This function receives a list of integers as a parameter. It then iterates through the list
recursively to find the minimum integer value and then returns that value. This function tests
that this parameter is a list that isn't empty and also that the elements in the list aren't
strings. If it finds one of these exceptions the function will return (-1)."""
def find_min(element):
    if type(element) != list or len(element) == 0:
        return -1
    for ele in element:
        if str(ele).strip("-").isdigit() == False:
            return -1
    while len(element) != 1:
        if element[0] >= element[1]:
            del element[0]
            find_min(element)
        else:
            del element[1]
            find_min(element)
    else:
        return element[0]


"""Send in a list of integer elements, the length of the list and null as parameters.
This function will return the sum total of all the integer values in the list."""
# def sum_all(element, count, sum_num):
#     while count >= 0:
#         if str(element[count]).isdigit() == False or element[count] == "":
#             return -1
#         sum_num += element[count]
#         count -= 1
#         return sum_all(element, count, sum_num)
#     return sum_num


"""his function receives a list of integers as a parameter. It then iterates through the list
recursively and adds up all of the values to return the sum total. This function tests
that this parameter is a list that isn't empty and also that the elements in the list aren't
strings. If it finds one of these exceptions the function will return (-1)."""
def sum_all(element):
    if type(element) != list or len(element) == 0:
        return -1
    for ele in element:
        if str(ele).strip("-").isdigit() == False:
            return -1
    while len(element) != 1:
        element[0] += element[1]
        del element[1]
    else:
        return element[0]


"""A character set and integer n is being passed as parameters. This function runs recursively to find
all possible string combinations for length n, using only the characters in the set. The function returns
a list of all the possible combinations. If an empty list or a non-character element is passed, the function
will return an empty list."""
def find_possible_strings(char_set, n):
    for x in char_set :
        if type(x) != str:
            return []
    if len(char_set) == 0:
        return []
    if n == 0:
        return [""]
    answer_list = []
    try:
        for i in char_set:
            for j in find_possible_strings(char_set, n-1):
                answer_list.append(i+j)
    except :
        return []
    return answer_list


if __name__ == "__main__":
    element = [8, 4, 9, 5]
    element2 = [2, 3, 7, 8]
    element3 = [3,100,-101,4,-5]
    new_list = ["a", "b"]

    # print(find_min(element, len(element) - 1, element[0]))
    # print(sum_all(element, len(element) - 1, 0))

    print(find_min(element3))
    print(sum_all(element2))
    print(find_possible_strings(new_list, 3))
