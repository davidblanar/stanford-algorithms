from abc import ABC, abstractclassmethod
from utils import swap

class Heap(ABC):
    def __init__(self, heap = None):
        if heap != None:
            assert len(heap) > 0 and heap[0] == None
        self.heap = heap if heap != None else [None]

    def get_heap(self):
        return self.heap

    def get_size(self):
        return len(self.heap)

    def get_parent_idx(self, child_idx):
        return int(child_idx / 2)

    def get_parent(self, child_idx):
        idx = self.get_parent_idx(child_idx)
        return self.heap[idx]

    def get_children_idx(self, parent_idx):
        left_idx = parent_idx * 2
        right_idx = left_idx + 1
        return left_idx, right_idx

    def get_children(self, parent_idx):
        left_idx, right_idx = self.get_children_idx(parent_idx)
        size = self.get_size()
        left = None if left_idx >= size else self.heap[left_idx]
        right = None if right_idx >= size else self.heap[right_idx]
        return left, right
        
    def swap(self, i1, i2):
        swap(self.heap, i1, i2)

    def insert(self, key):
        child_idx = self.get_size()
        parent = self.get_parent(child_idx)
        # insert
        self.heap.append(key)
        if parent != None:
            # bubble up
            while self.should_bubble_up(parent, key):
                parent_idx = self.get_parent_idx(child_idx)
                self.swap(child_idx, parent_idx)
                child_idx = parent_idx
                parent = self.get_parent(child_idx)

    def _extract(self):
        size = self.get_size()
        if size == 1:
            return None
        # move root to the end
        self.swap(1, size - 1)
        # extract the root
        val = self.heap.pop()
        # bubble down
        key_idx = 1
        while True:
            left_child_idx, right_child_idx = self.get_children_idx(key_idx)
            left_child, right_child = self.get_children(key_idx)
            if left_child == None or right_child == None:
                break
            else:
                idx = self.get_bubble_down_index(left_child, right_child, left_child_idx, right_child_idx)
                self.swap(key_idx, idx)
                key_idx = idx
        return val

    @abstractclassmethod
    def should_bubble_up(self, parent, key):
        raise NotImplementedError()

    @abstractclassmethod
    def get_bubble_down_index(self, left_child, right_child, left_child_idx, right_child_idx):
        raise NotImplementedError()
        
class MinHeap(Heap):
    def should_bubble_up(self, parent, key):
        return parent > key

    def get_bubble_down_index(self, left_child, right_child, left_child_idx, right_child_idx):
        return left_child_idx if left_child <= right_child else right_child_idx

    def extract_min(self):
        return self._extract()

class MaxHeap(Heap):
    def should_bubble_up(self, parent, key):
        return parent < key

    def get_bubble_down_index(self, left_child, right_child, left_child_idx, right_child_idx):
        return left_child_idx if left_child > right_child else right_child_idx

    def extract_max(self):
        return self._extract()
