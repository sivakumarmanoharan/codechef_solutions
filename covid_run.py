def covid_run(n,k,x,y):
    city_arr=[]
    city_arr.append(x)
    next_city=(x+k)%n
    while next_city not in city_arr:
        if next_city not in city_arr:
            city_arr.append(next_city)
            x=next_city
            next_city=(x+k)%n
    for i in city_arr:
        if i==y:
            return True
    return False
test_case=int(input("Enter the number of test cases"))
for i in range(test_case):
    n=int(input("Enter the number of cities"))
    k=int(input("Enter the jump count"))
    x=int(input("Enter the current city of virus"))
    y=int(input("Enter your city"))
    print(covid_run(n,k,x,y))
