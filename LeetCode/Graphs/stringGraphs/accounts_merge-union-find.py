from collections import Counter, defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        """
        Given a list of accounts where each element accounts[i] is a list of strings,
        where the first element accounts[i][0] is a name,
        and the rest of the elements are emails representing emails of the account.

        Now, we would like to merge these accounts.
        Two accounts definitely belong to the same person if there is some common email to both accounts.
        Note that even if two accounts have the same name,
        they may belong to different people as people could have the same name.
        A person can have any number of accounts initially,
        but all of their accounts definitely have the same name.

        After merging the accounts, return the accounts in the following format:
        the first element of each account is the name,
        and the rest of the elements are emails in sorted order.
        The accounts themselves can be returned in any order.
        """
        
        names = {}
        universe = UnionFind()
        
        for account in accounts:
            names[account[1]] = account[0]
            for i in range(1, len(account)):
                universe.union(account[1], account[i])
        
        components = defaultdict(list)

        for email in universe.up_bound:
            components[universe.find(email)].append(email)
        
        result = []
        for rep, comp in components.items():
            comp.sort()
            result.append( [names[rep]] + comp)
        
        return result
    
class UnionFind:
    def __init__(self):
        self.up_bound = {}
        self.rank = Counter()
        
    def find(self, x):
        if x not in self.up_bound:
            self.up_bound[x] = x
    
        if self.up_bound[x] == x:
            return x

        self.up_bound[x] = self.find(self.up_bound[x])
        return self.up_bound[x]
    
    def union(self, x, y):
        repr_x = self.find(x)
        repr_y = self.find(y)
        if repr_x == repr_y: # already in the same component
            return False
        if self.rank[repr_x] == self.rank[repr_y]:
            self.rank[repr_x] += 1
            self.up_bound[repr_y] = repr_x
        elif self.rank[repr_x] > self.rank[repr_y]:
            self.up_bound[repr_y] = repr_x
        else:
            self.up_bound[repr_x] = repr_y
            
            
        return True