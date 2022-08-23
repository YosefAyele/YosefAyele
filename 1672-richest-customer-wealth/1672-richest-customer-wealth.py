class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich=0
        for customer in accounts:
            rich=max(sum(customer),rich)
        return rich