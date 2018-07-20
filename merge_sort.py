def merge(A, p, q, r):
    L = [A[index] for index in range(p, q + 1)]
    R = [A[index] for index in range(q + 1, r + 1)]
    i = 0
    j = 0
    for index in range(p, r + 1):
        if L[i] < R[j]:
            A[index] = L[i]
            i += 1
            if i == len(L):
                for r_index in range(len(R[j:])):
                    #print("from R remaining, {}".format(R[r_index]))
                    A[index + 1 + r_index] = R[j + r_index]
                return
        else:
            A[index] = R[j]
            j += 1
            if j == len(R):
                for l_index in range(len(L[i:])):
                    #print("from L remaining, {}".format(L[l_index]))
                    A[index + 1 + l_index] = L[i + l_index]
                return


def merge_sort(A, p, r):
    if p < r:
        q = int((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
