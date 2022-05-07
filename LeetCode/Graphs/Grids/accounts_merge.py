from collections import defaultdict
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

        graph = defaultdict(list)
    
        for acc in accounts:
            name = acc[0]
            emailsToMerge = set(acc[1:])

            merged = False
            i = 0
            while i < len(graph[name]):
                if emailsToMerge & graph[name][i]:
                    if not merged:
                        graph[name][i] |= emailsToMerge
                        emailsToMerge = graph[name][i]
                    else:
                        emailsToMerge |= graph[name][i]
                        graph[name][i] = graph[name][-1]
                        graph[name].pop()
                        continue
                    merged = True
                i += 1

            if not merged:
                graph[name].append(emailsToMerge)

        result = []
                
        for name in graph:
            for emails in graph[name]: 
                emailsList = list(emails)
                emailsList.sort()
                result.append([name]+emailsList)
            
            
        return result