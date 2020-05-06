import pandas
import re
import sys

# num_pass = 891
# data = pandas.read_csv('titanic.csv', index_col='PassengerId')
# print(data)

# 1
# num_male = 0
# num_female = 0
#
# for i in data['Sex']:
#     if i == "male":
#         num_male += 1
#
#     if i == "female":
#         num_female += 1
#
# print(num_male)
# print(num_female)

# 2
# num_survived = 0
# for i in data['Survived']:
#     num_survived += i
# print(num_survived * 100 / num_pass)

# 3
# num_1class = 0
# for i in data['Pclass']:
#     if i == 1:
#         num_1class += 1
# print(num_1class * 100 / num_pass)

# 4
# median = pandas.DataFrame.median(data['Age'])
# mean = pandas.DataFrame.mean(data['Age'])
# print(mean)
# print(median)

# 5
# corr = data['SibSp'].corr(data['Parch'])
# print(corr)


# 6
# def update_dictionary(n_dict, key):
#     if key in n_dict:
#         n_dict[key] += 1
#     else:
#         n_dict.update({key: 1})
#
#
# def index_num(name_arr):
#     if "Mr" in name_arr:
#         return name_arr.index("Mr")
#     if "Mrs" in name_arr:
#         return name_arr.index("Mrs")
#     if "Dr" in name_arr:
#         return name_arr.index("Dr")
#     if "Master" in name_arr:
#         return name_arr.index("Master")
#     if "Miss" in name_arr:
#         return name_arr.index("Miss")
#
#
# def print_name(str_name_surname, n_dict):
#     name_arr = str_name_surname.split()
#     if len(name_arr) == 1:
#         update_dictionary(n_dict, name_arr[0])
#         # print(name_arr[0])
#     elif (("Mr" in name_arr) or ("Mrs" in name_arr) or ("Dr" in name_arr)
#             or ("Master" in name_arr) or ("Miss" in name_arr)):
#         name_ind = index_num(name_arr)
#         if name_arr[name_ind + 1] != "de":
#             update_dictionary(n_dict, name_arr[name_ind + 1])
#             # print(name_arr[name_ind + 1])
#     else:
#         if len(name_arr[0]) != 1:
#             update_dictionary(n_dict, name_arr[0])
#             # print(name_arr[0])
#         else:
#             update_dictionary(n_dict, name_arr[1])
#             # print(name_arr[1])
#
#
# def pars_name(str_name, n_dict):
#     my_str = re.sub(r"[(.,)]", "", str_name)
#     my_str = my_str.replace('"', '')
#     print_name(my_str, n_dict)
#
#
# def only_name(name, n_dict):
#     # поиск того, что в скобках
#     name_surname = re.findall('\\(.*?\\)', name)
#     if len(name_surname) > 0:
#         pars_name(name_surname[0], n_dict)
#         return
#     name_surname = re.findall('\\[.*?\\]', name)
#     if len(name_surname) > 0:
#         pars_name(name_surname[0], n_dict)
#         return
#     name_surname = re.findall('\\".*?\\"', name)
#     if len(name_surname) > 0:
#         pars_name(name_surname[0], n_dict)
#         return
#     else:
#         pars_name(name, n_dict)
#         return
#
#
# def print_top_name(n_dict):
#     num = 0
#     name = ''
#     for k, value in n_dict.items():
#         if value > num:
#             num = value
#             name = k
#     print(name)
#
#
# name_dict = {}
# la = 0
# names = data[data['Sex'] == 'female']['Name']
# for i in names:
#     only_name(i, name_dict)
# print_top_name(name_dict)
