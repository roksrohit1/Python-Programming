# #Compute the reciprocal for all elements in a
# given list and handle exceptions if found.
# lst = [1, 3, 0, ‘A’, 34, 10]
import numpy as np
try:
    x = np.array([1., 2., .2, .3])
    print("Original array: ")
    print(x)
    r1 = np.reciprocal(x)
    r2 = 1/x
    assert np.array_equal(r1, r2)
    print("Reciprocal for all elements of the said array:")
    print(r1)
    raise ValueError()

except(ValueError):
    print("erroe found")