# num1 = float(input("pahela no."))
# num2 = float(input("dusra no"))

# avg = (num1 + num2) / 2
# print(avg)



# name = input("Enter name: ")
# date = input("Enter date: ")

# letter = F"""Dear {name},
# You are selected!
# {date}"""

# print(letter)

# a = "saiif"
# print (a[1])


# t= int(input("please tell me the tempreture"))

# if t < 0:
#     print("frezzinf cold")

# elif t >= 0 and t <10:
#     print("very cold")

# elif t >= 10 and t <=20 :
#     print("very very cold")

# else :
#     print("gnd pt gai")


def insert_at(self, val, position):
    new_node = Node(val)
    if position == 0:
        new_node = new_node
         

    else:
        current =self.head
        prev_node ==current.next
        count = 0
        while current is not None and count < position:
            prev_node = current 
            currrent = current.next
            count += 1

            prev_node.next = new_node
            new_node.next = current