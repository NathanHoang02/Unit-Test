# MergeSort in Python
def mergeSort(array):
    if len(array) > 1:

        r = len(array)//2
        L = array[:r]
        M = array[r:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

# Test case in Python that covers: Positive, Negative, Performance, Boundaries, and Idempotency
import unittest
import random
class TestMergeSort(unittest.TestCase):

    def test_positive(self):
    #    Test if it runs normally
        arr = [2, 133, 245, 72, 52, 1, 90]
        expected = sorted(arr)
        mergeSort(arr)
        self.assertEqual(arr, expected)

    def test_negative(self):
        # Test if it runs with a TypeError
        arr = [164, 34, "25", 55, 93, 1, 90]
        with self.assertRaises(TypeError):
            mergeSort(arr)

        # Test how long the algorithm will take
    def test_performance(self):
        arr = [random.randint(1, 1000) for _ in range(100000)]
        expected = sorted(arr)
        mergeSort(arr)
        self.assertEqual(arr, expected)

        #Test what the boundaries are of the algorithm
    def test_boundary(self):
        # Empty array
        arr1 = []
        mergeSort(arr1)
        self.assertEqual(arr1, [])
        # Array with 1 value
        arr2 = [5]
        mergeSort(arr2)
        self.assertEqual(arr2, [5])
        # Array with duplicate values
        arr3 = [13, 13, 44, 44, 15, 29, 2, 61, 53, 13, 35]
        expected3 = sorted(arr3)
        mergeSort(arr3)
        self.assertEqual(arr3, expected3)
        # Array with incorrect value
        arr4 = [6, 2, 3, 4, 5]
        mergeSort(arr4)
        self.assertNotEqual(arr4, [1, 2, 3, 4, 5])
        # Array with correct value
        arr5 = [6, 5, 4, 3, 2, 1]
        mergeSort(arr5)
        self.assertEqual(arr5, [1, 2, 3, 4, 5, 6])

    def test_idempotency(self):
        # Test if the the algorithm is consistent
        arr = [24, 13, 41, 11, 15, 29, 32, 6, 25, 33, 45]
        expected = sorted(arr)
        
if __name__ == '__main__':
    unittest.main()