class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        
#         Q=[i for i in range(1,n+1)]
#         r=-1
#        #solution 1 
#         while len(Q)>1:
#             r=(r+k)%len(Q)
#             Q.pop(r)
#             r-=1
            
#         return Q[0]
        
        #solution2--------Using circular Queue
        # Friends=deque(i for i in range(1,n+1))
        # while len(Friends)>1:
        #     for i in range(k-1):
        #         Friends.append(Friends.popleft())
        #     Friends.popleft()
        # return Friends[0]
# Recursive Solution
        def recur(n,k):
            if n==1:
                return 0
            return (recur(n-1,k)+k)%n
        
        return recur(n,k)+1
        
            
            