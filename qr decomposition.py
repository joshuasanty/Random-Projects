import numpy as np


# check if noninvertible:
def isInvertible(matrix):
    return abs(np.linalg.det(matrix)) > 1e-10 # returns true if determinant is > 0

def qr(matrix: list[list]):
    A = np.array(matrix)
    m,n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    if not isInvertible(matrix):
        raise ValueError("Matrix Not Invertible")
    else:
        for j in range(n):
            v = A[:, j]  # take j-th column
            for i in range(j):
                R[i, j] = np.dot(Q[:, i], A[:, j])
                v = v - R[i, j] * Q[:, i]
            R[j, j] = np.linalg.norm(v)
            Q[:, j] = v / R[j, j]

        return Q, R

A = [
    [-3, 2, -1],
    [1, 1, -4],
    [2, 4, -1]
]



Q, R = qr(A)
print("Q =")
print(Q)
print("\nR =")
print(R)

A = [
    [4, 2, -1],
    [8, 4, -2],
    [7, -2, -5]
]

Q, R = qr(A)
print("Q =")
print(Q)
print("\nR =")
print(R)

print("\n".join(" ".join(str(v) for v in r) for r in Q), "\n\n")
print("\n".join(" ".join(str(v) for v in r) for r in R))
