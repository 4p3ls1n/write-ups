# kksctf open 2019 – kacker Bob and kacker Alice

* **Category:** Crypto
* **Points:** 100

## Challenge

> n = 208644129891836890527171768061301730329
> 
> c1 = 173743301171240370198046699578309731314
> c2 = 18997024455485040483743919351219518166
> c3 = 49337945995780286416188917529635194536


## Solution

Only numbers are given which look like modulus ans chipertexts.

Firstly, we tried find N in factordb (http://www.factordb.com/)
(I have no information for any attack I know, so I started with factoring)

Fortunately, there is factoring in the db.
So we can calulate phi(n) = (p-1)(q-1)

After we need to find private exponent. Because there is no information about public, we can just guess it (or use brute-force attack)

One of possible ways you can find in solver.py
(brute-force e until we get readable text)