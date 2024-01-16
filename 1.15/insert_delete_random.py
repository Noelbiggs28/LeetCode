from random import randint
class RandomizedSet:

    def __init__(self):
        self.set= []

    def insert(self, val: int) -> bool:
        present = val in self.set
        if not present:
            self.set.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        present = val in self.set
        if present:
            self.set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        length = len(self.set)-1
        number = randint(0,length)
        return self.set[number]