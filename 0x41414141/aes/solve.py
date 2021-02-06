outputs = [[b'1210374ff7b52c4b', b'265c3e4050e61d54', b'45deb95cf4f78c13', b'bcb4135d4365e327', b'63305d63ac7c5657',
            b'ec3ad64a021548e5'],
           [b'1210374ff7b52c4b', b'265c3e4050e61d54', b'5ebdd73480b1dc2b', b'db8b6935241eb31f', b'7853330bd83a066f',
            b'8b05ac22656e18dd'],
           [b'1210374ff7b52c4b', b'265c3e4050e61d54', b'45deb95cf4f78c13', b'bcb4135d4365e327', b'63305d63ac7c5657',
            b'ec3ad64a021548e5'],
           [b'1210374ff7b52c4b', b'265c3e4050e61d54', b'45deb95cf4f78c13', b'bcb4135d4365e327', b'63305d63ac7c5657',
            b'ec3ad64a021548e5'],
           [b'1210374ff7b52c4b', b'265c3e4050e61d54', b'5ebdd73480b1dc2b', b'db8b6935241eb31f', b'7853330bd83a066f',
            b'8b05ac22656e18dd'],
           [b'1210374ff7b52c4b', b'265c3e4050e61d54', b'45deb95cf4f78c13', b'bcb4135d4365e327', b'63305d63ac7c5657',
            b'ec3ad64a021548e5'],
           [b'1c4d2577fb9d4623', b'0e3338145be07117', b'5ebdd73480b1dc2b', b'db8b6935241eb31f', b'760e2133d4126c07',
            b'a36aaa766e68749e'],
           [b'072e4b1f8fdb161b', b'690c427c3c9b212f', b'45deb95cf4f78c13', b'bcb4135d4365e327', b'760e2133d4126c07',
            b'a36aaa766e68749e'],
           [b'1210374ff7b52c4b', b'265c3e4050e61d54', b'45deb95cf4f78c13', b'bcb4135d4365e327', b'63305d63ac7c5657',
            b'ec3ad64a021548e5'],
           [b'1210374ff7b52c4b', b'265c3e4050e61d54', b'45deb95cf4f78c13', b'bcb4135d4365e327', b'63305d63ac7c5657',
            b'ec3ad64a021548e5']]


def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


for blocks in outputs:
    xored = []
    iv = byte_xor(blocks[0], blocks[1])
    xored.append(iv)
    for i in range(1, 4):
        iv = byte_xor(blocks[i], iv)
        xored.append(iv.decode("utf-8"))
    print(xored)
