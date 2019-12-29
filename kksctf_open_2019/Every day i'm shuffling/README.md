# kksctf open 2019 – Every day i'm shuffling

* **Category:** Crypto
* **Points:** 481

## Challenge

> (you are given memo.jpg, shufflin.py and fsegovs_meaoerbma_.txt)

## Solution

`seed(randint(1, len(file_name)))` looks pretty unsecure

1) We know filename ('fsegovs_meaoerbma_') =>  we know it's len (and it is not very big)

2) We know filename before and after shuffling => we can use brute-force attack to get seed

OK, we used it, got to know that seed = 3

Now we need to reverse shuffle

We repeat everyting from `shufflin.py`, but replace original permutation to reverse one.

After we get original text and there is flag in the last line
