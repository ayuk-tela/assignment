def display_table(base, start, end, inc):
    print("Database Table:")
    print("---------------")
    for i in range(start, end + 1, inc):
        result = base * i
        print(base, '*', i, '=', result)
    print("---------------")


def main():
    base = 5
    start = 1
    end = 10
    inc = 2
    display_table(base, start, end, inc)

if __name__ == "__main__":
    main()