def expanded_sum(nums):
    sum = 0
    string = ""
    for i in range(len(nums)):
        if i == len(nums) -1:
            string = string + str(nums[i]) + " = "
        else:
            string = string + str(nums[i]) + " + "
        sum += nums[i]
    print(string + str(sum))
    
def get_high_low(nums):
    if isinstance(nums, list):
        newlist = [min(nums), max(nums)]
        
        return newlist
    
def is_list_empty(lists):
    if not lists:
        return True
    else:
        return False
    
def common_member(list1, list2):
    if isinstance(list1, list) and isinstance(list2, list):
        for x in list1:
            if x in list2:
                return True
        
        return False
