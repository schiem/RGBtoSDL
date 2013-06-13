RGBtoSDL
========

SDL colors work as follows:

The Uint32 colors are stored in 32 bit integers. 
That gets divided into four segments of 8 bits each:
R - 0000 0000
G - 0000 0000
B - 0000 0000
A - 0000 0000

To find the Uint 32 color of a number, first find it's RGB.
Let's take yellow for example.  It has an RGB of (255, 255, 0)
So, we convert 255 to binary, which is:

1111 1111

giving us an RGB of:
R - 1111 1111
G - 1111 1111
B - 0000 0000
A - Ignore it :)

which gives a final binary number of :

1111 1111 1111 1111 0000 0000,

which translates to 16776960 in decimal, as you can see below.

This project will perform this conversion for you, and perhaps more
in the future.
