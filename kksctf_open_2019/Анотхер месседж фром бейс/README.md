# kksctf open 2019 – Анотхер месседж фром бейс

* **Category:** Crypto
* **Points:** 698 

## Challenge

New intercepted message:
`гЖзпвшБпвшБзИЗНлШ3ЙлгВБуЩЧНщШЦглИЖЩшб20жа2Ейа2ХшвщоКХ2ФжШЧЙлИЖСпв2НхгмХшЩЦРтИЖ5лгшБиШЧНлИЖЕйШ2ХщвшБцШЧНщг29шЩВБпвшБса3Н7Ш3ХщгЖ9уЧ2И2НЕ9збЗБоШЦЙлгЕ9йНЖ50ЧшС0МЗБедУБ1еР==`

## Solution

This message looks very similar to Base64, but with different index table. With some guessing we can create new index table and map it to the standard one for decoding. 

```
import base64

encoded = 'гЖзпвшБпвшБзИЗНлШ3ЙлгВБуЩЧНщШЦглИЖЩшб20жа2Ейа2ХшвщоКХ2ФжШЧЙлИЖСпв2НхгмХшЩЦРтИЖ5лгшБиШЧНлИЖЕйШ2ХщвшБцШЧНщг29шЩВБпвшБса3Н7Ш3ХщгЖ9уЧ2И2НЕ9збЗБоШЦЙлгЕ9йНЖ50ЧшС0МЗБедУБ1еР=='

alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩабвгдежзийклмнопрстуфхцчшщ0123456789+/'
standard_base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

encoded = encoded.translate(str.maketrans(alphabet, standard_base))
decoded = base64.b64decode(encoded)

print(decoded.decode())
```

This outputs: 
>this is a secret message from kackers:
We are discovered, new base access password is kks{custom_b64_alphabet_c4nt_$t0p_y0u}


