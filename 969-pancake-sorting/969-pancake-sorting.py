class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        
    #Approach 1  
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
                 
  #Approach 2              
#         res = []
#         for x in range(len(arr), 1, -1):
            
#             i = arr.index(x)
#             res.extend([i + 1, x])
#             arr= arr[len(arr)-1:i:-1] + arr[:i]
            
#         return res


#Approach 3
        def flip(sublist, k):
            i = 0
            while i < k / 2:
                sublist[i], sublist[k-i-1] = sublist[k-i-1], sublist[i]
                i += 1

        ans = []
        value_to_sort = len(A)
        while value_to_sort > 0:
            
            index = A.index(value_to_sort)

            if index != value_to_sort - 1:

                if index != 0:
                    ans.append(index+1)
                    flip(A, index+1)
                
                ans.append(value_to_sort)
                flip(A, value_to_sort)

            value_to_sort -= 1

        return ans