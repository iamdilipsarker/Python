def get_largest(nums):
   largest = nums[0]
   for num in nums:
       if num > largest:
           largest.push(num)
   return largest
 
my_nums = [0,15,68,1,0,-55]
 
largest = get_largest(my_nums)
 
print('The largest number is: ', largest)















