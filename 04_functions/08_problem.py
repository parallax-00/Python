# def even_generator(x):
#     for num in range (1,x+1):
#         if (num%2==0): print (num)
# limit = int(input("Enter the upper limit: "))
# even_generator(limit)

def even_generator(number):
    for i in range (0,number+1,2):
        yield i
limit= int(input("Enter the limit: "))
for x in even_generator(limit):
    print (x)
        