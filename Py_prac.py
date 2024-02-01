# print("Hello world")

# message = "Hello Python world!"
# print(message)
# message = "Hello Python Crash Course world!"
# print(message)


# my_dict={}
# my_dict = {'num7': 1, 'num3': 2, 'num2': 3, 'num4': 6, 'num1': 5, 'num5': 4}
# sortedDict = sorted(my_dict)
# print("sorted on keys- print dict as lsit of keys: ", sortedDict) 

# sortedDict = sorted(my_dict.items())
# print("sorted on keys but item extracted both keys and values. printed as list of tuples: ", sortedDict)

# sortedDict = sorted(my_dict.items(), key=lambda x:x[1], reverse=True) #key=lambda tuple:tuple[second element of tuple]
# print("item extracted both keys and values, lambda part tells sorted function to sort on values. printed as list of tuples: ", sortedDict)

# back_to_dict = dict(sortedDict)
# print("list of tuples changed back to dict ", back_to_dict)

# name = [('sravan',7058,98.45),
#         ('ojaswi',7059,90.67),
#         ('bobby',7060,78.90),
#         ('rohith',7081,67.89),
#         ('gnanesh',7084,98.01)]
 
# # iterate using for loop
# for x in name:
#     print("x- ",x)
#   # iterate in each tuple element
#     for y in x:
#       print(y)
      
#     print() 


thisdict = {'num7': 1, 'num3': 2, 'num2': 3, 'num4': 6, 'num1': 5, 'num5': 4}
for x, y in thisdict.items():
  print(x, y)