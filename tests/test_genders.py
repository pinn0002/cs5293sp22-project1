from project1 import redactormain
import glob
path = "..\\cs5293sp22-project1\\docs\\*.txt"
def test_redactgenders():
    li = []
    data = glob.glob(path)
    for file in data:
        with open(file, 'r') as f:
            readfile = f.read()
            li.append(readfile)
    inputfiles = redactormain.redactgenders(li)
    assert isinstance(inputfiles,list)