class LRUelement:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.pred = None
        self.succ = None


class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._head = None
        self._tail = None
        self._elements = {}

    def _move_to_head(self, element: LRUelement):
        if self._head == element:
            return
        # Connect element pred and succ
        element.pred.succ = element.succ
        if element.succ != None:
            element.succ.pred = element.pred
        # Update tail
        if self._tail == element:
            self._tail = element.pred
        # Update head
        element.pred = None
        element.succ = self._head
        self._head.pred = element
        self._head = element

    def _create_new_element(self, key: int, value: int) -> LRUelement:
        element = LRUelement(key, value)
        if self._head == None:
            self._head = element
            self._tail = element
        else:
            self._head.pred = element
            element.succ = self._head
            self._head = element
        self._elements[key] = element
        return element

    def get(self, key: int) -> int:
        output = -1
        if key in self._elements:
            element = self._elements[key]
            self._move_to_head(element)
            output = element.value
        return output

    def put(self, key: int, value: int) -> None:
        if key in self._elements:
            self._move_to_head(self._elements[key])
            self._elements[key].value = value
        else:
            self._create_new_element(key, value)
            if self._capacity < len(self._elements):
                old_tail = self._tail
                self._tail = old_tail.pred
                self._tail.succ = None
                del self._elements[old_tail.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
