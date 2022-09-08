from struct import *


#'?'-> bool, 'h'-> short, 'i'-> integer, 'l'-> long, 'q'->long long, 'f'->float, 'l'->long


packed_data = pack('if',12,12.3)

print(type(packed_data))

sth = unpack('ii',packed_data)

print(sth)


sth2 = b'sthss'

print(type(sth2))

print(calcsize('q'))
