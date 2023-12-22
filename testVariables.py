import numpy as np
import argparse


# Example variables for unittesting
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose',
                    action='store_true')
args = parser.parse_args()

publicKey = ['x_1*x_3 + x_2*x_3 + x_2',
             'x_1*x_3 + x_1 + x_2 + x_3',
             'x_1*x_2 + x_3']

plainText = np.array([[False, False, False],
                      [False, False,  True],
                      [False, False, False],
                      [ True,  True, False],
                      [ True,  True,  True],
                      [ True,  True,  True],
                      [False,  True,  True],
                      [ True, False,  True],
                      [ True,  True,  True],
                      [ True,  True, False],
                      [False,  True, False],
                      [ True,  True, False],
                      [False, False, False],
                      [ True,  True,  True],
                      [False, False, False],
                      [ True, False,  True],
                      [ True,  True, False],
                      [ True,  True,  True],
                      [ True, False,  True]])

correspondingCipherText = np.array([[False, False, False],
                                    [False, True , True],
                                    [False, False, False],
                                    [ True, False,  True],
                                    [ True, False, False],
                                    [ True, False, False],
                                    [False, False,  True],
                                    [ True,  True,  True],
                                    [ True, False, False],
                                    [ True, False,  True],
                                    [ True,  True, False],
                                    [ True, False,  True],
                                    [False, False, False],
                                    [ True, False, False],
                                    [False, False, False],
                                    [ True,  True,  True],
                                    [ True, False,  True],
                                    [ True, False, False],
                                    [ True,  True,  True]])