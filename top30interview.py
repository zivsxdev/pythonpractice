# reverse a number

# n= 123 
# rev = 0 

# while n > 0:
#     rev = rev * 10 + n % 10 
#     n //=10
# print (rev)

# Check palindrome number

# n = 121
# temp = n
# rev = 0

# while n > 0:
#     rev = rev * 10 + n % 10
#     n //= 10

# print(temp == rev)

#  sum of two num
# num= float(input("enter here 1st number : "))
# num2= float(input("enter another number here:"))

# sum= num + num2

# print ("the sum of thee provded  two number is",sum)


# x =12
# y = 13

# x,y=y,x

# print("the value of x is ", x)
# print ("the value of y is",y)


# arr = [1,2,3,4,5]

# count=0
# for _ in arr:
#     count += 1

#     print(count)


# arr = [12,3,4,56]

# for i in arr:
#         print (i)


arr = [2, 4, 6, 8]

total = 0
count = 0

for i in arr:
    total += i
    count += 1

avg = total / count
print(avg)
