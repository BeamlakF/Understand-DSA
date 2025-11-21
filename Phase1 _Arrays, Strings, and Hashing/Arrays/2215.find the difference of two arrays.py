class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        my_new_list = []
        answer1=[]
        answer2 =[]
        nums_1 = set(nums1)
        nums_2 = set(nums2)

        for i in nums_1:
            if i not in nums_2 and i not in answer1:
                answer1.append(i)

            

        for j in nums_2:
            if j not in nums_1 and j not in answer2:
                answer2.append(j)
        
        my_new_list.append(answer1)
        my_new_list.append(answer2)

        return my_new_list
        