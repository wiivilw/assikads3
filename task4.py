def isHappy(n):
    seen = set()

    while n != 1:
        if n in seen:
            return False
        seen.add(n)

        n = sum(int(d)**2 for d in str(n))

    return True

n = int(input())
print(isHappy(n))