
# i am going to write only the problem implementaion

def max_depth(root: node):
  
  def dfs(node):
    if not node:
      return 0

    left_depth = dfs(node.left)
    right_depth = dfs(node.right)
    return max(left_depth,right_depth)+1  # This is going to return the depth of each node
  
  return dfs(root) - 1 if root else 0 # this will essentially make sure we are returning depth according to the edges not the nodes
  
