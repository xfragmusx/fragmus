
#agreed = input('Do you want to continue? (yes/no):')

#if agreed == 'yes':
    #print('lets continuation')
        #if True:
#elif agreed == 'no':
    #print("no continuation")
#else:
    #print('wrong input')


#print(agreed, type(agreed))
age = int(input('Enter your age:'))
name = input("enter your name:")

if age < 18 or name == 'alice':
    print ('not allow to drink')
elif age <= 21 and name ==  'Bob':
    print('not allow to drink (USA CITIZEN)')
else:
    print ('allow to drink')