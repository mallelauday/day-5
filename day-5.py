L='Udaykumar'
size=int(input("Enter the size of Request List:"))
request=[0]*size
for i in range(size):
    request[i]=int(input("Enter the requests:"))
pli=len(L)%3
count=0
valid=0
no_demand=0
low_demand=[]
moderate_demand=[]
high_demand=[]
invalid_request=[]
for i in range(size):
    if request[i]<0:
        invalid_request.append(request[i])
    elif request[i]==0:
        valid+=1
        no_demand+=1
    elif 1<=request[i]<=20:
        low_demand.append(request[i])
        valid+=1
    elif 21<=request[i]<=50:
        moderate_demand.append(request[i])
        valid+=1
    elif request[i]>=51:
        high_demand.append(request[i])
        valid+=1
print("Low Demand:",low_demand)
print("Moderate Demand:",moderate_demand)
print("High Demand:",high_demand)
print("Invalid Requests:",invalid_request)
if pli==0:
    low_demand=[0]
    count=len(low_demand)
elif pli==1:
    high_demand=[0]
    count=len(high_demand)
elif pli==2:
    low_demand=[0]
    high_demand=[0]
    count=len(low_demand)+len(high_demand)
print("Name:",L,"\nPLI:",pli)
print("Valid Requests:",valid)
print("Count removed requests due to PLI:",count)
print("No Demand:",no_demand)
print("Low Demand:",low_demand)
print("Moderate Demand:",moderate_demand)
print("High Demand:",high_demand)
print("Invalid Requests:",invalid_request)