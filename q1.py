# for i in range (1,11):
#   print(i, end = "")


# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)


# for i in range (10,0,-3):
#       print(i)


# total = 0 
# for i in range(1,10):
#  total += i 
#  print(total)


# a = "saif"
# for i in a:
#     print(i)


# i=1
# while i <= 5:
#     print (i)
#     i += 2


# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)


# for i in range(1, 10):
#     if i == 5:
#         continue
#     print(i)


# for i in range(1, 31):
#     if i % 3 == 0:
#         print(i)


# n = 12345
# count = 0
# while n > 0:
#     count += 1
#     n //= 10
# print(count)


# n = 123
# rev = 0
# while n > 0:
#     rev = rev * 10 + n % 10
#     n //= 10
# print(rev)

# nums = [-1, -2, 0]
# for n in nums:
#     if n > 0:
#         print("Positive")
#     elif n < 0:
#         print("Negative")
#     else:
#         print("Zero")


# n = 7
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(fact)


# n = 7

# is_prime = True
# for i in range(2, n):
#     if n % i == 0:
#         is_prime = False
#         break

# print(is_prime)

# a, b = 0, 1
# for _ in range(10):
#     print(a)
#     a, b = b, a + b


nums = [10, 5, 20, 8]
max_num = nums[0]

for n in nums:
    if n > max_num:
        max_num = n

print(max_num)

