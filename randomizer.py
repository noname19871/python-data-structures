import random
from typing import Dict, List, Optional


class Randomizer:
    """
    Data structure with fast Insert/Delete/Find/GetRandomElement operations.
    All operations work with O(1) time complexity
    """
    def __init__(self):
        self.memory: List[int] = []
        self.hashtable: Dict[int, int] = {}

    def add(self, x: int) -> bool:
        self.memory.append(x)
        idx = len(self.memory) - 1
        self.hashtable[x] = idx
        return True

    def remove(self, x: int) -> bool:
        # O(1)
        x_pos = self.hashtable.get(x, None)
        if not x_pos:
            return False

        del self.hashtable[x]

        self.memory[x_pos], self.memory[-1] = self.memory[-1], self.memory[x_pos]

        # O(1) since it's last element
        self.memory.pop(-1)

        self.hashtable[self.memory[x_pos]] = x_pos

        return True

    def get_random(self) -> Optional[int]:
        if not self.memory:
            return None
        return random.choice(self.memory)

    def find(self, x: int) -> int:
        if x in self.hashtable:
            return self.hashtable[x]
        return -1


rand = Randomizer()
print(rand.get_random())
print(rand.add(3))
print(rand.add(5))
print(rand.remove(7))
print(rand.remove(3))
print(rand.find(3))
print(rand.find(5))
print(rand.add(15))
print(rand.add(172))
print(rand.get_random())
