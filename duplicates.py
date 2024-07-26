list = [1,2,3,1,2,4,5,6]

count={}
duplicate = []

for i in list:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

for key, value in count.items():
    if value > 1:
        duplicate.append(key)

print(duplicate)