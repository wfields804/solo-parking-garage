#Question 1 

my_list = [1,11,14,5,8,9]
blank_list = []

def less_than(my_list):
    
    for x  in blank_list:
        if (x) < (10):
            print(my_list.append(x))
#Could not quite get this




#Question 2

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

l_3 = l_1 + l_2
print(l_3)

#I believe I made a sorted list  like the question asked for. However I understand I did not use a "function".
# I do not understand functions below I will try to solve using information I got from youtube and google

#Question 2.2

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

for x in l_2:
    l_1.append(x)
    l_1.sort(reverse=True)
print(l_1)

#Here I used the .append method, in a for loop, which I think goes through every integer of the list
# I then added (.append) x which is l_2 to l_1.... then print the new l_1 which is now combined
#I then sorted it reverse.



    

