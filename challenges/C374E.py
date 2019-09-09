# https://www.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/
if __name__ == '__main__':

    def add_persist(n: int):
        print("\nNumber tested is %s" % str(n))
        n_of_iter = 0
        while n > 9:
            n = sum(map(int, list(str(n))))
            n_of_iter += 1
        return n_of_iter

    print("Challenge:")
    print(str(add_persist(13)) + " => 1")
    print(str(add_persist(1234)) + " => 2")
    print(str(add_persist(9876)) + " => 2")
    print(str(add_persist(199)) + " => 3")
