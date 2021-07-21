import dummy


def testFirst():
    assert dummy.inc(3) == 5


def testSecond():
    assert dummy.con(5) == 15


if __name__ == "__main__":
    testFirst()
    testSecond()
