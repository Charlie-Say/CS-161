#! /user/bin/python3
# coding=utf-8

'''
Demonstrate various methods of farmatting text output in Python
'''

name = "Susan"
count = 37
PI = 3.14

### old-school way ###
# You should not be using this type of output formatting in new Python code
print("Hello, %s. How are you today?" % (name))
print("Hello, %s. How are you today? You have %s coconuts." % (name, count))
print("Hello, %s. How are you today? You have %s coconuts. The value of PI is %.2f" % (name, count, PI))


### the newer way of formatting output ###
# This is fine method to use for Python 3+ ###

print("Hello, {}. How are you today?".format(name))
print("Hello, {}. How are you today? You have {} coconuts.".format(name, count))
print("Hello, {0}. How are you today? You have {1} coconuts.".format(name, count))
print("Hello, {2}. How are you today? You have {2} coconuts. The value of PI is {1}".format(name, count, PI))
print("Hello, {}. How are you today? You have {:4} coconuts.".format(name, count))
print("Hello, {0:.3}. How are you today? You have {0:4} coconuts.".format(name, count))
print("Hello, {0}. How are you today? You have {1:4} coconuts. The value of PI is {2:6.3}".format(name, count, PI))


