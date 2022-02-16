def expanded_sum(nums):
    """ Receives a list of integers and adds them up. 
        
        It prints out the numbers being added and the final sum value."""
    
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
    """ Receives a list of integers and returns a list containing the min and max integers from the array"""
    
    if isinstance(nums, list):
        newlist = [min(nums), max(nums)]
        
        return newlist
    
def is_list_empty(lists):
    """ Receives a list and checks to see if the list is empty or not.
        This will return True for an empty list and False for nonempty lists"""
    
    if not lists:
        return True
    else:
        return False
    
def common_member(list1, list2):
    """ Receives two lists and compares the elements in the two lists to see if there is an element that
        are in both of the lists """
    
    if isinstance(list1, list) and isinstance(list2, list):
        for x in list1:
            if x in list2:
                return True
        
        return False
