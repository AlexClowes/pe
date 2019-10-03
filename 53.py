def get_combs(n):
    ret = [0] * (n + 1)
    ret[0] = 1
    for i in range(1, n + 1):
        ret[i] = ret[i-1] * (n - i + 1) // i
    return ret

def main():
    count = 0
    for n in range(1, 101):
        combs = get_combs(n)
        count += sum(i > 10**6 for i in combs)
    print(count)




if __name__ == "__main__":
    main()
