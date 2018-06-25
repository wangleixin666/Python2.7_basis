# coding:utf_8


def result(N, M):
    if N == 0:
        return M
    return M * (M-1)**(N - 1) - result(N-1, M)


if __name__ == '__main__':
    N = input()
    M = input()

    print result(N, M)
