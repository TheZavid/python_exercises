def parent_node(i):
    return (i - 1) // 2


def left_node(i):
    return 2 * i + 1

def right_node(i):
    return 2 * i + 2


class BinaryHeap:


    def __init__(self):
        self.a = [] # initially empty



    # The insert function will always run in O(logN) as only the the depth of the last
    # layer matters in this case
    def insert(self, i): # insert a value i into the heap
        self.a.append(i)
        cur_index = len(self.a) - 1
        if cur_index == 0:
            return
        while True:
            par = parent_node(cur_index)
            if cur_index == 0 or self.a[cur_index] >= self.a[par]:
                return

            self.a[cur_index], self.a[par] = self.a[par], self.a[cur_index]
            cur_index = par

    def valid_util(self, index):
        if index >= len(self.a):
            return True
        if left_node(index) < len(self.a) and self.a[index] > self.a[left_node(index)]:
            return False
        elif right_node(index) < len(self.a) and self.a[index] > self.a[right_node(index)]:
            return False
        elif self.valid_util(left_node(index)) and self.valid_util(right_node(index)):
            return True
        else:
            return False

    def is_valid(self):
        return self.valid_util(0)


    def remove_smallest(self): # remove the smallest value
        pass

heap = BinaryHeap()
heap.insert(2)
heap.insert(5)
heap.insert(4)
heap.insert(7)
heap.insert(6)
heap.insert(12)
heap.insert(8)
heap.insert(9)
heap.insert(11)
heap.insert(10)
heap.insert(15)
heap.insert(14)
print(heap.a)
print(heap.is_valid())
heap.insert(1)
print(heap.a)
print(heap.is_valid())
