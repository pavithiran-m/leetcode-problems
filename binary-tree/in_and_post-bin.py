class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        dic={val:key for key,val in enumerate(inorder)}

        def built(l,r):
            if l>r:
                return 
            
            nval= postorder.pop()
            root=TreeNode(nval)

            mid=dic[nval]

            root.right=built(mid+1,r)
            root.left=built(l,mid-1)

            return root
        return built(0,len(inorder)-1)
    
inorder=[9,3,15,20,7]
postorder=[9,15,7,20,3]
s=Solution()    
print(s.buildTree(inorder,postorder))
