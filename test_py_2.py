


def outerfunc():
    var1=555

    def innerfunc1():
        nonlocal var1
        var1 += 101

    innerfunc1()
    return var1

print(outerfunc())


