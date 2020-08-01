# -*- coding: utf-8 -*-

from model.group import Group
import random
import  string

constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

def radom_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group ( name="", header="", footer="" )] + [
    Group ( name = radom_string("name",10), header = radom_string("header",20), footer=radom_string("footer",20))
    for i in range(5)
