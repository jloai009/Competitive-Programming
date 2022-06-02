from random import getrandbits
RANDOM_MASK = getrandbits(31)
class myint(int):
    def __hash__(self):
        return self^RANDOM_MASK
int = myint
