nums  = [1,0]



"""
nums.extend(nums)

c = 1
for i in range(len(nums)-1):

    if nums[i] <= nums[i+1]:

        c += 1

    else:

        c = 1

    if c == len(nums)//2:

        print(True)
        exit()
print(len(nums)//2==1) 

"""

n = len(nums)
c  = 1
for i in range(2*n-1):

    if nums[i%n] <= nums[(i+1)%n]:

        c += 1

    else:

        c = 1

    if c == n :

        print(True)
        exit()

print(n == 1) # to handle one element in lst