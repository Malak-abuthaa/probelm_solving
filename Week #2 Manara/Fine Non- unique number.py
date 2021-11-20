# This is not a cool solution
"""
Note: Try to solve this in-place. In a real interview, you will only be allowed to use O(1) additional memory.

You're given an array of integers a. It is guaranteed that there is a non-unique number with at least a.length / 2 occurences (where / is float division). The other numbers in a are unique. Find and return the non-unique number.

Example

For a = [1, 2, 3, 3, 3], the output should be
solution(a) = 3.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

An array of integers.

Guaranteed constraints:
3 ≤ a.length ≤ 105,
-106 ≤ a[i] ≤ 106.

[output] integer

The non-unique integer in a.

"""


def solution(a):
    for i in range(len(a)):
        if a[i] in a[i + 1:]:
            return a[i]


        
        """
        better solution is to use window of threee 

                for(int i = 1; i < N-1; i++){
                if(A[i-1] == A[i] || A[i] == A[i+1])
                return A[i];
                else if(A[i-1] == A[i+1])
                return A[i-1]
                }
        ""


