from gmpy2 import invert
from Crypto.Util.number import long_to_bytes
import string

printset = set(string.printable)

n = 208644129891836890527171768061301730329

# from http://www.factordb.com/
p = 13037609104445998727
q = 16003250919732396127
phi = (p-1)*(q-1)


c1 = 173743301171240370198046699578309731314
c2 = 18997024455485040483743919351219518166
c3 = 49337945995780286416188917529635194536

enc = [c1, c2, c3]
true_e = -1
for e in range(100000):
    try:
        d = invert(e,phi)
        c = long_to_bytes(pow(c1,d,n))
        try:
            a = c.decode('ascii')
            a_set = set(a)
            if a_set.issubset(string.printable):
                true_e = e
                break
        except:
            pass
    except:
        pass


d = invert(true_e,phi)
dec = []
for c in enc:
    dec.append(long_to_bytes(pow(c,d,n)))

print(b''.join(dec))