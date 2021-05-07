# altsonfly
Linux temporary alternate session generator that works through "xhost +" being enabled in Xorg to start graphical applications.

This hinges on the command "useradd" being a part of your system. There is no preliminary check for that, as well as for the /alts/ directory in / and it's access to that
granted via root elevation (which is to be supplied to the program itself).


Other changes will be done in the future as I get less lazy regarding this thing. This was mainly designed for me when it came to me being able to simply partition my
school life as well as my online life.


Another theorhetical thing that you can do as well, is to have it route the accounts to temp (which is usually a tempfs [i thinkm depending on how you've configured your fstab]), which would have them simply run in memory and be destroyed upon restart.


The syntax can be found either by simply looking at the source code and seeing it outlined very simply thrugh argparse, or through just -h.

An example of it would be:

```sudo python3 altsonfly.py -a 3 -p chromium```


This would create 3 unique sessions of Chromium, through adding two users and using sudo -U & -s to launch the program. It's quite simple and to the point and works,
as for it being in Python, it doesn't really matter or change much for me. Nor does having it work in the manner at which it does. It isn't redundant or anything.
