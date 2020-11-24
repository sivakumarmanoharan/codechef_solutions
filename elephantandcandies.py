def satisfy(c,want_list):
    if sum(want_list)>c:
        return False
    else:
        return True
n=int(input("Enter the number of elephants in the zoo"))
c=int(input("Enter the number of candies in the zoo"))
want_list=[]
for i in range(n):
    want_list.append(int(input("Enter the candies needed for the elephant")))
print(satisfy(c,want_list))
