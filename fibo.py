def recursive_nth_fibo(n):
    if n < 2:
        return n
    else:
        return recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)


def main():
    n = 6
    output = recursive_nth_fibo(n)
    print(output)


if __name__ == '__main__':
    main()
