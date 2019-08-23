# https://www.reddit.com/r/dailyprogrammer/comments/bqy1cf/20190520_challenge_378_easy_the_havelhakimi/
if __name__ == '__main__':
    # Optional warmup 1
    def warmup1(l: list):
        return [x for x in l if x != 0]

    print("Warmup 1")
    print(str(warmup1([5, 3, 0, 2, 6, 2, 0, 7, 2, 5])) + " should equal [5, 3, 2, 6, 2, 7, 2, 5]")
    print(str(warmup1([4, 0, 0, 1, 3])) + " should equal [4, 1, 3]")
    print(str(warmup1([1, 2, 3])) + " should equal [1, 2, 3]")
    print(str(warmup1([0, 0, 0])) + " should equal []")
    print(str(warmup1([])) + " should equal []")

    def warmup2(l: list):
        return sorted(l, reverse=True)

    # Optional warmup 2
    print("\nWarmup 2")
    print(str(warmup2([5, 1, 3, 4, 2])) + " = > [5, 4, 3, 2, 1]")
    print(str(warmup2([0, 0, 0, 4, 0])) + " = > [4, 0, 0, 0, 0]")
    print(str(warmup2([1])) + " = > [1]")
    print(str(warmup2([])) + " = > []")

    # And now... the maaain event of the eveniiing!
    def hh(l: list):
        while True:
            l = [x for x in l if x != 0]
            if len(l) == 0:
                return True
            else:
                l = sorted(l, reverse=True)

                h, *t = l
                if h > len(t):
                    return False
                else:
                    for x in range(h):
                        t[x] = t[x] - 1
                    l = t

    print("\nChallenge:")
    print(str(hh([5, 3, 0, 2, 6, 2, 0, 7, 2, 5])) + " => false")
    print(str(hh([4, 2, 0, 1, 5, 0])) + " => false")
    print(str(hh([3, 1, 2, 3, 1, 0])) + " => true")
    print(str(hh([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16])) + " => true")
    print(str(hh([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12])) + " => true")
    print(str(hh([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3])) + " => false")
    print(str(hh([6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1])) + " => false")
    print(str(hh([2, 2, 0])) + " => false")
    print(str(hh([3, 2, 1])) + " => false")
    print(str(hh([1, 1])) + " => true")
    print(str(hh([1])) + " => false")
    print(str(hh([])) + " => true")
