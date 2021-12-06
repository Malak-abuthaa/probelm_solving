"""
Given an array a of positive integers, find the number of pairs of integers for which the difference between the two numbers is equal to a given number k. Since the number of pairs could be quite large, take it modulo 109 + 7 for your output.

Example

For k = 3 and a = [1, 6, 8, 2, 4, 9, 12], the output should be
solution(k, a) = 3.

There are three pairs of integers whose difference is equal to 3: (1, 4), (6, 9) and (9, 12).

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer k

The specified difference between two numbers.

Guaranteed constraints:
1 ≤ k ≤ 1000.

[input] array.integer a

Guaranteed constraints:
1 ≤ a.length ≤ 105,
1 ≤ a[i] ≤ 1000.

[output] integer

The number of pairs of integers with difference k modulo 109 + 7
"""
def solution(k, a):

    count = 0
    for i in range(len(a)):
        for j in range(i ,len(a)):
            if (a[j] - a[i]) == k or a[j ]+ k == a[i] or a[i ]+ k == a[j]:
                count +=1
    return count

    # nums = {}

    # for item in a:
    #         nums[item] = []



    # count = 0
    # for item in a:
    #     print(nums)

    #     if item + k  in nums and (item +k not in nums[item] or item not in nums[item + k ]):
    #         print(item , item + k)
    #         nums[item].append(item+k)
    #         count += 1
    #     if item - k  in nums and item - k not in nums[item] or item not in nums[item - k ]:
    #         print(item , item - k)
    #         nums[item].append(item - k)
    #         count += 1




    # return count
    
    
    int solution(int k, int[] a) {
   HashMap<Integer,Integer> map  = new HashMap<Integer,Integer>(); 
   int counter = 0; 
   int mod = 1000000007; 
   for(int num : a){
       if(map.containsKey(num)){
           map.put(num, map.get(num)+1);
       }
       else{
           map.put(num,1);
       }
   }
   for(int num : a){
       int diff = num-k; 
       if(map.containsKey(diff)){
           if(diff == num){
             counter= (counter+map.get(diff)-1)%mod;  
           }
           else{
             counter= (counter+map.get(diff))%mod;  
           }
       }
   }
   
   return counter%mod; 
}
