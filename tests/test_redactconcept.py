import glob
import sys
from project1 import redactormain
import argparse
path = "..\\cs5293p2r-project1\\docs\\*.txt"
def test_redactconcept():
    parser = argparse.ArgumentParser()
    parser.add_argument("--concept", type=str, required=False, action="append", metavar='value', help="Input all text files")
    args = parser.parse_args("--concept ../cs5293p2r-project1/docs/*.txt".split())
    li = []
    xyz = glob.glob(str(args))
    for file in xyz:
        with open(file, 'r') as f:
            readfile = f.read()
            li.append(readfile)
    #global data
    inputfiles = redactormain.redactconcept(args,li)
    assert isinstance(inputfiles,list)