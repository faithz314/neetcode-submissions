class Solution:
    def reverseBits(self, n: int) -> int:
        n_bit = bin(n)[2:].zfill(32) #n_bit is a string
        n_bit_reversed= n_bit[::-1]

        return int(n_bit_reversed, 2)