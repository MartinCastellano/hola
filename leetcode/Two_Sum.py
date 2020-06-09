
nums = [2, 7, 11, 15]
target = 13

def twoSum(nums, target):
   
    for i in range(len(nums)):
        
        for j in range(i+1,len(nums)) :
            if i != j:

                
                suma = nums[i]+nums[j]
                
                
                if suma == target:
                    return [i,j]
                   
            
   
    
    
print(twoSum(nums, target))