Couplets.py

A program utilizing Python 3.4 to run operations on sets of data in couplet
pairs. Used for Calculation of Nuclear Magnetic Resonance.


Ex.
There is a set of data consisting of 6, 5, 4, 3, 2, 1
(Data is always in DECENDING order).

In sets of couplet pairs you will have [6,5], [4,3], [2,1].

In each couplet, you will subtract the first from the second and then you will
add all the results and divide by the number of couplets, which in this case
is 3.

You will repeat the process with pairing every other number: [6,4],
[5,3], [4,2], [3,1].

This also works with odd numbered data. It accounts for the chemical shift which
is the value in the center of the data set.

Requirements to run:

Python 3.4


To Run:

In command line/terminal move into directory that the program is stored in
(i.e. C:\Users\Username\Documents\).

Type python3 couplets.py
