class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, preorder):
        if not inorder or not preorder:
            return None
        dic={val:key for key,val in enumerate(inorder)}
        pre=0
        def built(l,r):
            if l>r:
                return 
            
            nval= preorder[pre]
            pre += 1
            root=TreeNode(nval)

            mid=dic[nval]

            root.left=built(l,mid-1)
            root.right=built(mid+1,r)

            return root
        return built(0,len(inorder)-1)
inorder=[9,3,15,20,7]
preorder=[3,9,20,15,7]
s=Solution()    
print(s.buildTree(inorder,preorder))