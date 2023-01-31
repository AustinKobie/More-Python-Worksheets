#Excercise 1
#Given a list as a parameter,write a function that returns a list of numbers that 
# are less than ten
#For example: Say your input parameter to the function is 
# [1,11,14,5,8,9]...Your output should [1,5,8,9]
def new_List():
    new_list = []
    l_1 = [1, 11, 14, 5, 8, 9]
    for num in l_1[:]:
        if num < 10:
            new_list.append(num)
        return new_list
print(new_list)


#excercise 2
#Write a function that takes in two lists and 
# returns the two lists merged together and sorted
l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
def comb(l_1, l_2):
    comb_list = l_1 + l_2
    comb_list.sort()
    return(comb_list)
print(comb(l_1, l_2))
