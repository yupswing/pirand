# pirand
calculate π from pairs of random numbers

MIT Licence (c) 2017 Simone Cingano

Made on 3.15 2017

Happy (Pi Day)+0.01 2017

# Usage

`python pirand.py [faces] [rolls]`


default parameters (with output):
```
» python pirand.py
500 random rolls of two d120
progress [====================] 100.0% | current error 1.85373%
 math.pi | 3.14159265359
   Final | 3.19982934699 (1.8537315246% error)
    Best | 3.14112506384 (0.0148838441% error at the roll number 147)
```

a better run (with output):
```
» python pirand.py 9999999999 9999999
9,999,999 random rolls of two d9,999,999,999
progress [====================] 100.0% | current error 0.00931%
 math.pi | 3.14159265359
   Final | 3.14130030793 (0.0093056515% error)
    Best | 3.14159265202 (0.0000000501% error at the roll number 812,427)
python pirand.py 9999999999 9999999  60,06s user 0,72s system 97% cpu 1:02,02 total
```

# Why have you done this?
Watch this video by Matt Parker and you will understand

https://www.youtube.com/watch?v=RZBhSi_PwHU
