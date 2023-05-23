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
    a1 = []
    for _ in range(7):
        


def main(stream):
    return parse_a(stream, 4)[0]