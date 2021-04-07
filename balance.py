heights = dict()


class Node:
    def __init__(self, left, val, right):
        self.left = left
        self.val = val
        self.right = right


def find_height(node):
    if node is None:
        heights[node] = -1
        return True
    heights[node] = 0
    output = False
    left_complete = find_height(node.left)
    right_complete = find_height(node.right)
    if (left_complete and right_complete) and heights[node.left] == heights[node.right]:
        heights[node] = heights[node.left] + 1
        output = True
    else:
        if heights[node.left] >= heights[node.right]:
            heights[node] = heights[node.left]
        else:
            heights[node] = heights[node.right]

        heights[node] += 1

    return output


def find_max(node, max):
    if node is None:
        return 0
    tmp = abs(heights[node.left] - heights[node.right])
    if tmp > max:
        max = tmp
    left_max = find_max(node.left, max)
    if left_max > max:
        max = left_max
    right_max = find_max(node.right, max)
    if right_max > max:
        max = right_max
    return max


def balance_factor(root):
    if find_height(root):
        return 0
    return find_max(root, 0)


n1 = Node(None, 3, None)
n2 = Node(n1, 5, None)
n3 = Node(None, 2, n2)
n5 = Node(None, 15, None)
n6 = Node(None, 30, None)
n7 = Node(n5, 20, n6)
root = Node(n3, 10, n7)
print(balance_factor(root))
