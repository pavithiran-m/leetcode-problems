
def isSymmetric(root):
    
    def mirror(left, right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        return (left.val == right.val and
                mirror(left.left, right.right) and
                mirror(left.right, right.left))
    
    if not root:
        return True
    
    return mirror(root.left, root.right)