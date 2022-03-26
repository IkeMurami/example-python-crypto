class JavaRandom:
    """
    java/util/Random
    """
    def __init__(self, seed):
        self.seed = (seed ^ 0x5DEECE66D) & ((1 << 48) - 1)

    def next_bytes(self, count):
        r = ''
        i = 0
        while i < count:
            r_int = self.next_int()
            for j in range(4):
                r += chr(r_int & 0xFF)
                r_int = r_int >> 8
                i += 1
                if i >= count:
                    break
        return r

    def next_int(self):
        self.seed = (self.seed * 0x5DEECE66D + 0xB) & ((1 << 48) - 1)
        return self.seed >> (48 - 32)