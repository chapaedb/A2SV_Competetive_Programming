if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    comb = [[m,k,l] for m in range(x + 1) for k in range(y + 1) for l in range(z + 1) if m + k + l != n]
    print(comb)
