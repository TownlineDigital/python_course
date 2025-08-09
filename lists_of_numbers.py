list_of_lists = [
    [2, 6, 8],
    [10, 18, 13, 16, 18, 19],
    [26, 18, 86, 54, 52, 88],
    [26, 52, 84, 99, 11, 15, 18, 77],
    [15, 16, 19, 62, 23],
    [23, 52, 63, 18, 69, 84, 52, 18, 18, 51, 18, 88, 74, 51]
]

# for numlist in list_of_lists:
#     if 18 not in numlist:
#         print(numlist)
#     else:
#         print('{} has 18 appearing {} times'.format(numlist, numlist.count(18)))

for each_list in list_of_lists:
    for index in range(len(each_list)-1, -1, -1):
        if each_list[index] == 18:
            del each_list[index]

print(list_of_lists)

#              0   1   2   3   4   5    6
# random_list = [22, 34, 56, 69, 10, 100, 77]
# random_list1 = [2, 55, 88, 48, 73, 103, 73]
#
# # for number in random_list:
# #     print(number)
#
# for index in range(len(random_list)):
#     print(random_list[index])
#
# for index in range(len(random_list1)):
#     print(random_list1[index])
#
# print(random_list[0])
# print(random_list[1])
# print(random_list[2])
# print(random_list[3])
# print(random_list[4])
# print(random_list[5])
# print(random_list[6])
