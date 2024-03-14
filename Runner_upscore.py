if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_ = list(set(arr))
    new_ = sorted(new_, reverse = True)
    print(new_[1])
