def happypredict(notebook,k,n,y):
    for i in range(n):
        if y+notebook[i][0]>=x and notebook[i][1]<=k:
            return 1
            break
        else:
            continue
    return 0
test_case=int(input("Enter the number of test cases"))
for i in range(test_case):
    x=int(input("Enter the number of pages the chef wants to write"))
    y=int(input("Enter the number of pages he has now"))
    k=int(input("Enter the budget of chef"))
    n=int(input("Enter the number of notebooks in the shop"))
    notebook=[]
    for i in range(n):
        notebook.append([int(j) for j in input().split()])
    result=happypredict(notebook,k,n,y)
    if result==1:
        print("LuckyChef")
    else:
        print("UnluckyChef")
