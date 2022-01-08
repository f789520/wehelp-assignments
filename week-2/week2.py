
def calculate(min, max):
    # 請用你的程式補完這個函式的區塊
    sum = 0
    for x in range(min,max+1):
            sum = sum + x
            # print(sum)
    print(sum)

calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30


# print("----------要求二----------")

def avg(data):
   
    b=data.get("employees")
    # print(b)
    sum=0
    for item in b:
        sum=sum+int(item["salary"])
    # print(sum)
    mean=sum/int(data["count"])
    print(mean)
    
avg({
        "count":3,
        "employees":[
            {
                "name":"John",
                "salary":30000
            },
            {
                "name":"Bob",
                "salary":60000
            },
            {
                "name":"Jenny",
                "salary":50000
            }
        ]
}) # 呼叫 avg 函式


# print("----------要求三----------")

def maxProduct(nums):
# 請用你的程式補完這個函式的區塊
    max=float('-inf') 
    for i in nums:
        for x in nums: 
            if i ==x :
                continue 
            c=i*x
            if c > max:
                max=c
    print(max)
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2


# print("----------要求四----------")

def twoSum(nums, target):
# your code here
    for i in nums:
        for x in nums: 
            if i ==x :
                continue  
            if target ==  i+x :
                return[nums.index(i),nums.index(x)]
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9