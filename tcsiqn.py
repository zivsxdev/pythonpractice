# def reverse_string(s):
#     rev =""
#     for i in range(len(s)-1,-1,-1):
#         rev = rev + s[i]
#     return rev
 
# text = input("enter  a string")
# result= reverse_string(text)
# print(result)
     
     
#     #  1. Reverse words in a sentence


# def reverse_words(sentence):
#     words = sentence.split()
#     reverse_words = []
    
#     for i in range(len(words)-1,-1,-1):
#         reverse_words.append(words[i])

#         return"".join(rev_words)


# # Largest Element in an Array

def largest_element(arr):
    largest = arr[0]
 
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    return largest
        
num = [3,4,5,3,5]
result = largest_element(num)
print("Largest element is:", result)