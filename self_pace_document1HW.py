#Question 1.

cubed = [a**3 for a in range(0,1001) if (a**3)< 1001]
print(cubed)



#Question 2

prime = [a/a for a in range(1,101) if (a/1) in range(1,101)]
#print(prime)


def isPrime(n):
    
    if n > 1:
        #simple version here but both of these are completely valid
        for x in range(2, n):

        # Optimized version that takes 1/2 as many steps
            for x in range(2, (n//2)+1):

            
                if n % x == 0:
                
                    return False
                
        return True

    return False  
    
for x in range(101):
    
    if isPrime(x):
        print(x)




#Question 3

#I pretty much guessed on this. It works, but it seems like I missed something to make it more complex?

age = int(input('how old are you?  Please input NUMBERS!'))

if age < 18:
    print('Kiddo!')
elif age < 65:
    print('Adult')
else:
    print('Sorry, you\'re old!')
