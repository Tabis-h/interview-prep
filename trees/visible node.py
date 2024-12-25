def visible_tree(root: Node):
  visible = 0
  
  
  def dfs(node,max_val):
    nonlocal visible
    if not node:
      return

    if node.val > max_val:
      max_val = node.val
      visible += 1       # this part could be made much smaller but to me this is the simplest way
    dfs(node.left)
    dfs(node.right)

    
  dfs(root,-inf)
  return visible
  
