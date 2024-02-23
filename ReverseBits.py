class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = bin(n)[2:].zfill(32)
        # initialize result
        k = 0
        # iterate over the binary string in reverse order
        for i, bit in enumerate(n):
            # if the bit is 1, add 2^i to the result
            if bit == '1':
                k += 2**i
        # return the result
        return k
