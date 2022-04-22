import glob
import os.path
import re
import nltk
import numpy as np
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk import word_tokenize, ne_chunk, pos_tag,sent_tokenize
from nltk.corpus import wordnet
from pathlib import Path
from nltk.tree import Tree


def fetchtextdata(input_files):
    #creating a list to store the contents of all text files
    li = []
    for files in input_files.input:
        # use glob operator to represent text files
        eachfile = glob.glob(files)
        for file in eachfile:
            try:
                with open(file, 'r') as f:
                    readfile = f.read()
                    li.append(readfile)
            except:
                print('File cannot be read:' + file)
    return li
def redactnames(text_data):
    maskeddata = []
    for name in text_data:
        # to get nltk.tree.Tree object to traverse the tree
        namedentities = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(name)))
        nameslist = []
        for entity in namedentities.subtrees(filter=lambda t: t.label() == 'PERSON'):
            for leaf in entity.leaves():
                if leaf[0] not in nameslist:
                    nameslist.append(leaf[0])
        for person in nameslist:
            # hide names in textfiles
            name = name.replace(person, '\u2588' * len(person))
        maskeddata.append(name)
    return maskeddata

def redactgenders(text_data):
    genderentity = ['father','mother','daddy','mummy','businessman','businesswoman','she','he','him','her','hers','Mr.','Ms.','his','hers','son','daughter','sister','brother','woman','man','men','women','sir','madam','king','queen','uncle','aunt','nephew','niece','husband','wife','lord','lady','himself','herself','dad','mom','grandfather','grandmother','grandson','granddaughter','boy','girl','boys','girls','boyfriend','girlfriend','hero','heroine','gentleman','gentlemen','emperor','empress','waiter','waitress','son-in-law','father-in-law','mother-in-law','daughter-in-law','prince','princess','actor','actress','businessman','businesswoman','businessmen','businesswomen','god','goddess','bride','groom','bridegroom','ladies','gents','gent']
    maskedgender = []
    for gender in text_data:
        tokenizeword = nltk.word_tokenize(gender)
        extractgenders = []
        for word in tokenizeword:
            if word.lower() in genderentity and word not in extractgenders:
                extractgenders.append(word)
        #sort the list in descending order
        extractgenders.sort(key=len,reverse=True)
        for identity in extractgenders:
            #hide genders in text file
            gender = gender.replace(identity,'\u2588'*len(identity))
        maskedgender.append(gender)
    return maskedgender

def redactdates(text_data):
    maskeddate = []
    for word in text_data:
        datepatterns = []
        matchdate = re.findall(r'(\d{2,4}[-./]\d{1,2}[-./]\d{1,2})', word)
        for element in matchdate:
            if element not in datepatterns:
                datepatterns.append(element)
        matchdate1 = re.findall(r'(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})', word)
        for element in matchdate1:
            if element not in datepatterns:
                datepatterns.append(element)
        matchdate2 = re.findall(r'(\d{1,2}\s(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(?:,\s|\s)\d{2,4})',word)
        for element in matchdate2:
            if element not in datepatterns:
                datepatterns.append(element)
        matchdate3 = re.findall(r'((?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{1,2}(?:,\s|\s)\d{2,4})',word)
        for element in matchdate3:
            if element not in datepatterns:
                datepatterns.append(element)
        matchdate4 = re.findall(r'((?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{1,2})',word)
        for element in matchdate4:
            if element not in datepatterns:
                datepatterns.append(element)
        matchdate5 = re.findall(r'(\d{1,2}-(?:May|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-\d{2,4})', word)
        for element in matchdate5:
            if element not in datepatterns:
                datepatterns.append(element)
        matchdate6 = re.findall(r'((?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{1,2}(?:st|nd|rd|th)(?:,\s|\s)\d{2,4})',word)
        for element in matchdate6:
            if element not in datepatterns:
                datepatterns.append(element)
        matchdate7 = re.findall(r'(\d{1,2}(?:st|nd|rd|th)\s(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(?:,\s|\s)\d{2,4})',word)
        for element in matchdate7:
            if element not in datepatterns:
                datepatterns.append(element)
        matchdate8 = re.findall(r'((?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{1,2}(?:st|nd|rd|th))',word)
        for element in matchdate8:
            if element not in datepatterns:
                datepatterns.append(element)
        matchdate9 = re.findall(r'(\d{1,2}(?:st|nd|rd|th)\s(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec))',word)
        for element in matchdate9:
            if element not in datepatterns:
                datepatterns.append(element)
        datepatterns.sort(key=len,reverse=True)
        for date in datepatterns:
            word = word.replace(date,'\u2588'*len(date))
        maskeddate.append(word)
    return maskeddate

def redactphones(text_data):
    maskedphones = []
    for phone in text_data:
            phonepatterns = []
            matchphone = re.findall(r'((?:\+1\s|\+)\(\d{3}\)\s\d{3}-\d{4})',phone)
            for element in matchphone:
                if element not in phonepatterns:
                    phonepatterns.append(element)
            matchphone1 = re.findall(r'(\d{3}(?:\s|\.|\-)\d{3}(?:\s|\.|\-)\d{4})',phone)
            for element in matchphone1:
                if element not in phonepatterns:
                    phonepatterns.append(element)
            matchphone2 = re.findall(r'((?:1\-)\d{3}(?:\s|\.|\-)\d{3}(?:\s|\.|\-)\d{4})',phone)
            for element in matchphone2:
                if element not in phonepatterns:
                    phonepatterns.append(element)
            matchphone3 = re.findall(r'\d{3}-\d{4}',phone)
            for element in matchphone3:
                if element not in phonepatterns:
                    phonepatterns.append(element)
            matchphone4 = re.findall(r'(\(\d{3}\)\s\d{3}(?:\s|\.|\-)\d{4})', phone)
            for element in matchphone4:
                if element not in phonepatterns:
                    phonepatterns.append(element)
            phonepatterns.sort(key=len, reverse=True)
            for pattern in phonepatterns:
                phone = phone.replace(pattern, '\u2588' * len(pattern))
            maskedphones.append(phone)
    return maskedphones

def redactaddress(text_data):
    maskedaddress = []
    for word in text_data:
        addresspatterns = []
        matchaddress = re.findall(r'([0-9]{3,4}\s.+,\s.+,\s[A-Z]{2}(?:\s[0-9]{5}|\s))', word)
        for element in matchaddress:
            if element not in addresspatterns:
                addresspatterns.append(element)
        matchaddress1 = re.findall(r'([0-9]{3,4}.+\n.+,\s.+,\s[A-Z]{2}(?:\s[0-9]{5}|\s))', word)
        for element in matchaddress1:
            if element not in addresspatterns:
                addresspatterns.append(element)
        matchaddress2 = re.findall(r'([0-9]{3,4}.+,\s.+\n.+\n.+,\s[A-Z]{2}(?:\s[0-9]{5}|\s))', word)
        for element in matchaddress2:
            if element not in addresspatterns:
                addresspatterns.append(element)
        matchaddress3 = re.findall(r'([0-9]{3,4}.+\n.+,\s[A-Z]{2}(?:\s[0-9]{5}|\s))', word)
        for element in matchaddress3:
            if element not in addresspatterns:
                addresspatterns.append(element)
        for pattern in addresspatterns:
            print(pattern, len(pattern))
            word = word.replace(pattern,'\u2588'*len(pattern))
        maskedaddress.append(word)
    return maskedaddress

def outputredactedfiles(input_files, text_data):
    i=0
    for files in input_files.input:
        eachfile = glob.glob(files)
        for file in eachfile:
            path = Path(file)
            complete_name = os.path.join(input_files.output, path.stem + '.redacted')
            if not os.path.exists(input_files.output):
                os.makedirs(input_files.output)
                output = open(complete_name, 'wb')
                output.write(text_data[i].encode('utf8'))
            elif os.path.exists(input_files.output):
                output = open(complete_name, 'wb')
                output.write(text_data[i].encode('utf8'))
            i = i + 1

def redactconcept(input_files, text_data):
    maskedconcept = []
    conceptentity = []
    for sentence in input_files.concept:
        conceptentity.append(sentence)
        for syn in wordnet.synsets(sentence):
            for l in syn.lemma_names():
                conceptentity.append(l.lower())
    conceptentity = nltk.flatten(conceptentity)
    for sentence in text_data:
        tokenizesentence = nltk.sent_tokenize(sentence)
        conceptpattern = []
        for word in tokenizesentence:
            tokenizeword = nltk.word_tokenize(word)
            for eachword in tokenizeword:
                if eachword.lower() in conceptentity and word not in conceptpattern:
                    conceptpattern.append(word)
        for pattern in conceptpattern:
            sentence = sentence.replace(pattern, '\u2588' * len(pattern))
        maskedconcept.append(sentence)
    return maskedconcept
def redactedstats(input_files,text_stat):
    if input_files.stats == "stdout":
        statsfile = open(1, 'w')
    elif input_files.stats == "stderr":
        statsfile = open(2, 'w')
    else:
        statsfile = open(input_files.stats, 'w')
    try:
        li = []
        # print(input_files.input)
        for files in input_files.input:
            eachfile = glob.glob(files)
            li.append(eachfile)
        li = nltk.flatten(li)
        # print(li)
        # statsfile = open(input_files.stats, 'w')
        statsfile.write("*************Update stats of names***********\n")
        count1 = 0
        if input_files.names:
            name_stats = redactnames(text_stat)
            for i in range(0, len(name_stats)):
                count = 0
                tokenize = nltk.word_tokenize(name_stats[i])
                file = li[i]
                path = Path(file)
                for item in tokenize:
                    block = '\u2588' * len(item)
                    # print(item, block,end='\n')
                    if item == block:
                        count = count + 1
                        count1 = count1 + 1
                        #count2 = "Divya"+1
                statsfile.write("Total number of names redacted in %s is %s\n" % (path.stem, str(count)))
        statsfile.write("Total number of names redacted in all files is %s\n" % str(count1))
        # print(eachfile)
        statsfile.write("*************Update stats of genders***********\n")
        count1 = 0
        if input_files.genders:
            name_stats = redactgenders(text_stat)
            for i in range(0, len(name_stats)):
                count = 0
                tokenize = nltk.word_tokenize(name_stats[i])
                path = Path(li[i])
                # print(tokenize)
                for item in tokenize:
                    block = '\u2588' * len(item)
                    # print(item, block,end='\n')
                    if item == block:
                        count = count + 1
                        count1 = count1 + 1
                statsfile.write("Total number of genders redacted in %s is %s\n" % (path.stem, str(count)))
        statsfile.write("Total number of genders redacted in all files is %s\n" % str(count1))
        statsfile.write("*************Update stats of dates***********\n")
        count1 = 0
        if input_files.dates:
            name_stats = redactdates(text_stat)
            for i in range(0, len(name_stats)):
                count = 0
                tokenize = nltk.word_tokenize(name_stats[i])
                path = Path(li[i])
                # print(tokenize)
                for item in tokenize:
                    block = '\u2588' * len(item)
                    # print(item, block,end='\n')
                    if item == block:
                        count = count + 1
                        count1 = count1 + 1
                statsfile.write("Total number of dates redacted in %s is %s\n" % (path.stem, str(count)))
        statsfile.write("Total number of dates redacted in all files is %s\n" % str(count1))
        statsfile.write("*************Update stats of phones***********\n")
        count1 = 0
        if input_files.phones:
            name_stats = redactphones(text_stat)
            for i in range(0, len(name_stats)):
                count = 0
                tokenize = nltk.word_tokenize(name_stats[i])
                path = Path(li[i])
                # print(tokenize)
                for item in tokenize:
                    block = '\u2588' * len(item)
                    # print(item, block,end='\n')
                    if item == block:
                        count = count + 1
                        count1 = count1 + 1
                statsfile.write("Total number of phones redacted in %s is %s\n" % (path.stem, str(count)))
        statsfile.write("Total number of phones redacted in all files is %s\n" % str(count1))
        statsfile.write("*************Update stats of address***********\n")
        count1 = 0
        if input_files.address:
            name_stats = redactaddress(text_stat)
            for i in range(0, len(name_stats)):
                count = 0
                tokenize = nltk.word_tokenize(name_stats[i])
                path = Path(li[i])
                # print(tokenize)
                for item in tokenize:
                    block = '\u2588' * len(item)
                    # print(item, block,end='\n')
                    if item == block:
                        count = count + 1
                        count1 = count1 + 1
                statsfile.write("Total number of address redacted in %s is %s\n" % (path.stem, str(count)))
        statsfile.write("Total number of address redacted in all files is %s\n" % str(count1))
        statsfile.write("*************Update stats of concept***********\n")
        count1 = 0
        if input_files.concept:
            conceptentity = []
            # print(input_files.concept)
            for sentence in nltk.flatten(input_files.concept):
                conceptentity.append(sentence)
                # print(sentence)
                for syn in wordnet.synsets(sentence):
                    for l in syn.lemma_names():
                        conceptentity.append(l)
            conceptentity = nltk.flatten(conceptentity)
            i = 0
            for sentence in text_stat:
                tokenizesentence = nltk.sent_tokenize(sentence)
                path = Path(li[i])
                count = 0
                # print(tokenizesentence)
                conceptpattern = []
                for word in tokenizesentence:
                    tokenizeword = nltk.word_tokenize(word)
                    # print(conceptentity)
                    # print(tokenizeword)
                    for eachword in tokenizeword:
                        if eachword in conceptentity and word not in conceptpattern:
                            # print("true")
                            conceptpattern.append(word)
                            count = count + 1
                            count1 = count1 + 1
                i = i + 1
                statsfile.write("Total number of concept redacted in %s file is %s\n" % (path.stem, str(count)))
        statsfile.write("Total number of sentences redacted related to concept in all files is %s\n" % str(count1))
    except:
        statsfile.write("Exception Occurred!\n")
    statsfile.close()