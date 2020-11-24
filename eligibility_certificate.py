def certficate_eligible(lec_list,M,N,times_list):
    count=0
    for i in range(N):
        if sum(lec_list[i])>=M and times_list[i]<10:
            count=count+1
    return count

lec_list=[]
times_list=[]
count=0
N=int(input("Enter the number of students"))
M=int(input("Enter the number of minutes"))
K=int(input("Enter the number of lectures"))
for i in range(N):
    lec_list.append([int(j) for j in input().split()])
#print(lec_list)
for i in range(N):
    times_list.append(int(input("Enter the times of {}th student".format(i))))
approval=certficate_eligible(lec_list,M,N,times_list)
print(approval)
