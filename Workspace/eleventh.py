from struct import *


FMT = dict(
    char='c',
    int8='b',
    uint8='B',
    int16='h',
    uint16='H',
    int32='i',
    uint32='I',
    int64='q',
    uint64='Q',
    float='f',
    double='d'
)


def parse(buf, offset, operation_type, order='>'):
    pattern = FMT[operation_type]
    size = calcsize(pattern)
    value = unpack_from(order + pattern, buf, offset)[0]
    return value, offset + size


def parse_a(buf, offset):
    a1, offset = parse_b(buf, offset)
    a2, offset = parse(buf, offset, 'double')
    a3, offset = parse(buf, offset, 'int32')
    size_a4, offset = parse(buf, offset, 'uint32')
    offset_a4, offset = parse(buf, offset, 'uint16')
    a4 = []
    for _ in range(size_a4):
        value, offset_a4 = parse(buf, offset_a4, 'int16')
        a4.append(value)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4), offset


def parse_b(buf, offset):
    b1 = ''
    for _ in range(7):
        value, offset = parse(buf, offset, 'char')
        b1 += value.decode('utf-8')
    offset_b2, offset = parse(buf, offset, 'uint32')
    b2, _ = parse_c(buf, offset_b2)
    size_b3, offset = parse(buf, offset, 'uint16')
    offset_b3, offset = parse(buf, offset, 'uint16')
    b3 = []
    for _ in range(size_b3):
        value, offset_b3 = parse_d(buf, offset_b3)
        b3.append(value)
    b4, offset = parse(buf, offset, 'uint64')
    b5 = []
    for _ in range(6):
        value, offset = parse(buf, offset, 'double')
        b5.append(value)
    b6, offset = parse(buf, offset, 'int32')
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6), offset


def parse_c(buf, offset):
    c1, offset = parse(buf, offset, 'double')
    c2, offset = parse(buf, offset, 'int64')
    c3, offset = parse(buf, offset, 'int32')
    return dict(C1=c1, C2=c2, C3=c3), offset


def parse_d(buf, offset):
    d1, offset = parse(buf, offset, 'double')
    d2, offset = parse(buf, offset, 'int8')
    return dict(D1=d1, D2=d2), offset


def main(stream):
    return parse_a(stream, 4)[0]
