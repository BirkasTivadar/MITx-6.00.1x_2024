import sys


def teszt(test):
    lineNumber = sys._getframe(1).f_lineno
    if test:
        msg = "The test in line {0} is correct.".format(lineNumber)
    else:
        msg = "The test in line {0} is fail.".format(lineNumber)
    print(msg)
