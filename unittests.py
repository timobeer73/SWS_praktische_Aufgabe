import numpy as np
import unittest as ut
import argparse
from pipeline import executePipeline


parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose',
                    action='store_true')
args = parser.parse_args()
args.filepath = '.\\unittestChallenge.txt'


# Test if the plaintext is correctly encrypted
class TestMethods(ut.TestCase):
    def test_pipeline(self):
        _, resultMatching = executePipeline(args)
        self.assertTrue(resultMatching)


if __name__ == '__main__':
    ut.main()