import glob
from project1 import redactormain
path = "..\\cs5293p2r-project1\\docs\\*.txt"
def test_redactdates():
    li = []
    data = glob.glob(path)
    for file in data:
        with open(file, 'r') as f:
            readfile = f.read()
            li.append(readfile)
    inputfiles = redactormain.redactdates(li)
    assert isinstance(inputfiles,list)