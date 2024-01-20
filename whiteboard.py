# Fizz Buzz #2
# Write a function to print all numbers 1 to n, but there are some constraints
# If the number is divisible by 3, print ‘Fizz’ instead of the number
# If the number is divisible 5, print ‘Buzz’ instead of the number
# If the number is divisible by both 3 and 5, print ‘FizzBuzz’ instead of the number
# Otherwise, simply print the number

#  n is always positive >1 and a whole number

# pseudo code
# define a function that takes in n as a positive integer > 1 x
#  for loop using range() starting with 1, ending with n
#  3 constraints so o need possibly 3 conditionals
# num % 3 == 0, print 'Fizz'
#  num % 5 == 0, print 'Buzz'
#  nuj % 3 == 0 and num % 5 == 0 pirnt 'fizzBuzz'
#  else print num

def fizz_buzz(n): 

    for i in range(1,n): #will grab all numbers from 1 to n, not inlcuding n
        if i % 3 == 0 and i % 5 == 0:
            print ('Fizzbuzz')
        elif i % 3 == 0 # modulo helps us see if something is divisible by something {in this case 3}
            print('Fizz')
        elif i % 5 == 0:
            print ('Buzz')
        else:
            print(1)

    fizz_buzz(16)