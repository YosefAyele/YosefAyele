class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        # output=[]
        # m=len(arr)
        # f=len(arr)-1
        # for j in arr:
        #     for i in range(len(arr)):
        #         if arr[i]==m:
        #             arr[:i+1]=arr[i::-1]
        #             output.append(len(arr[:i+1]))
        #             arr[:f+1]=arr[f::-1]
        #             output.append(len(arr[:f+1]))
        #             m-=1
        #             f-=1
        # return output
                 
                
#         res = []
#         for x in range(len(arr), 1, -1):
            
#             i = arr.index(x)
#             res.extend([i + 1, x])
#             arr= arr[len(arr)-1:i:-1] + arr[:i]
            
#         return res
# class Solution:
#     def pancakeSort(self, A: List[int]) -> List[int]:
        """ sort like bubble-sort
            sink the largest number to the bottom at each round
        """
        def flip(sublist, k):
            i = 0
            while i < k / 2:
                sublist[i], sublist[k-i-1] = sublist[k-i-1], sublist[i]
                i += 1

        ans = []
        value_to_sort = len(A)
        while value_to_sort > 0:
            # locate the position for the value to sort in this round
            index = A.index(value_to_sort)

            # sink the value_to_sort to the bottom,
            #   with at most two steps of pancake flipping.
            if index != value_to_sort - 1:
                # flip the value to the head if necessary
                if index != 0:
                    ans.append(index+1)
                    flip(A, index+1)
                # now that the value is at the head, flip it to the bottom
                ans.append(value_to_sort)
                flip(A, value_to_sort)

            # move on to the next round
            value_to_sort -= 1

        return ans