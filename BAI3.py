import numpy as np
import copy

originMatrix = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

rotate90Matrix = copy.copy(originMatrix)
rotate180Matrix = copy.copy(originMatrix)

def rotate90(matrix):
    for i in range(0, len(matrix)):
        matrix[i] = matrix[i][::-1]
    result = matrix.transpose()
    return result

def rotate180(matrix):
    temp = matrix.flatten()
    temp = temp[::-1]
    result = np.reshape(temp, (len(matrix), len(matrix)))
    return  result

print("origin: ")
print(originMatrix)
print("After rotate 90 counter clockwise: ")
print(rotate90(rotate90Matrix))
print("After rotate 180: ")
print(rotate180(rotate180Matrix))


