# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def __init__(self, s):
        self.g = Solution.readGraph(s)
        

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        

    def readGraph(s):
        ll = s.split("[")
        ln = [x.split("]")[0] for x in ll]
        l = [x.split(",") for x in ln]
        i = 0
        while i<len(l):
            if l[i][0]=='':
                l.pop(i)
            else:
                i+=1
        l = [[int(y) for y in x] for x in l]
        return l

def main():
    s = input()
    Solution(s)

if __name__ == "__main__":
    main()