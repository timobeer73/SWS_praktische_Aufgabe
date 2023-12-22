import numpy as np
import unitest as ut
from testVariables import args, publicKey, plainText, correspondingCipherText
from functions import calculateCipherText


# Test if the plaintext is correctly encrypted
class TestMethods(ut.TestCase):
    def test_calculateCipherText(self):
        np.testing.assert_array_equal(calculateCipherText(args, publicKey, plainText), correspondingCipherText)


if __name__ == '__main__':
    ut.main()