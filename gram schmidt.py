import numpy as np

def gram_schmidt(A):

    A = np.copy(A).astype(np.float64)
    n = A.shape[1]
    for j in range(n):

        for k in range(j):
            A[:, j] -= np.dot(A[:, k], A[:, j]) * A[:, k]
        if np.isclose(np.linalg.norm(A[:, j]), 0, rtol=1e-15, atol=1e-14, equal_nan=False): #if cols are not linearly independent
            A[:, j] = np.zeros(A.shape[0])
            print("Columns are not linearly independent")
        else:
            A[:, j] = A[:, j] / np.linalg.norm(A[:, j])
    return A

A = np.array([[-3,2,1], [2,1,4], [-1,-4,-1]]).T
print(gram_schmidt(A))
A = np.array([[4,8,7],[2,4,-2],[-1,-2,-5]]).T
print(gram_schmidt(A))
