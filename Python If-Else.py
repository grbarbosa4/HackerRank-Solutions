#!/bin/python3
import math
import os
import random
import re
import sys


n = int(input())
if n%2==1:
    print ("Weird")
elif n%2==0:
    if n in list(range(2,6)):
        print ("Not Weird")
    elif n in list(range(6,21)):
        print ("Weird")
    elif n>20:
        print ("Not Weird")
    else: print ("Weird")
