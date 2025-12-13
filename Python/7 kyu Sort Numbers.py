"""
Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.

For example:

solution([1,2,3,10,5]) # should return [1,2,3,5,10]
solution(None) # should return []
test.assert_equals(solution([1,2,3,10,5]), [1,2,3,5,10])
test.assert_equals(solution(None), [])
test.assert_equals(solution([]), [])
test.assert_equals(solution([20,2,10]), [2,10,20])
test.assert_equals(solution([2,20,10]), [2,10,20])
"""
def solution(nums):
    return sorted(nums) if nums is not None else []
