import argparse
from project1 import redactormain

def main(input_files):
    if (input_files.input):
        text_data = redactormain.fetchtextdata(input_files)
        text_stat = redactormain.fetchtextdata(input_files)
    if(input_files.names):
        text_data = redactormain.redactnames(text_data)
    if (input_files.genders):
        text_data = redactormain.redactgenders(text_data)
    if (input_files.dates):
        text_data = redactormain.redactdates(text_data)
    if (input_files.phones):
        text_data = redactormain.redactphones(text_data)
    if (input_files.address):
        text_data = redactormain.redactaddress(text_data)
    if (input_files.concept):
        text_data = redactormain.redactconcept(input_files, text_data)
    if (input_files.output):
        redactormain.outputredactedfiles(input_files, text_data)
    if (input_files.stats):
        redactormain.redactedstats(input_files,text_stat)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True, action= "append", help="Input all text files")
    parser.add_argument("--names", help="remove names", action="store_true")
    parser.add_argument("--dates", required=False, help="remove dates", action="store_true")
    parser.add_argument("--phones", required=False, help="remove phonenumbers", action="store_true")
    parser.add_argument("--genders", help="remove genders", action="store_true")
    parser.add_argument("--address", required=False, help="remove address", action="store_true")
    parser.add_argument("--concept", type=str, required=False, help="redact sentence", action="append")
    parser.add_argument("--output", type=str, required=True, help="output all text redacted files")
    parser.add_argument("--stats", type=str, required=True, help="stats of redacted files")
    args = parser.parse_args()
    main(args)

