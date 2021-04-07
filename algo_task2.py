class Node:
    def __init__(self, left, val, right):
        self.val = val
        self.left = left
        self.right = right

def path(root) -> str:
    if root is None:
        return ''

    cur_val = root.val
    left_val = path(root.left)
    right_val = path(root.right)
    if len(left_val) >= len(right_val):
        cur_val += left_val
    else:
        cur_val += right_val

    return cur_val


k = Node(None, 'k', None)
n = Node(k, 'n', None)
p = Node(None, 'p', None)
u = Node(p, 'ef', n)
pp= Node(None, 'p', None)
t = Node(None, 't', None)
e = Node(pp, 'aksjdhsad', None)
P = Node(u, 'p', e)

print(path(P))

# The function doesnt really have a best-case or worst-case  as it always is going
# to traverse through all of the N nodes to find the deepest sequence resulting in
# complexity O(N)
