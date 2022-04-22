**Name: Divya Sai Pinnamaneni**

**Run Procedure:**

> Install all the below specified libraries using the following command pipenv install modulename.

> Install pipenv using pip install pipenv

> Run the project using  pipenv run python redactor.py --input --names --dates --phones --genders --address --output --concept --stats in which only input,output,stats flags take arguments and the remaining are not mandatory.

> Run testfiles using pipenv run python -m pytest

**Libraries used in this project:**

glob, argparse, os.path, re, nltk, numpy, pathlib

**Changes from previous project**

From the previous project, I have added few changes for names, genders and addresses functions.

**redactnames(text_data):**

Earlier I have joined first and last names together and now I have returned each individual name count.

**redactgenders(text_data):**

Enhanced genders identiication list by adding some other gender detecting words

**redactaddress(text_data):**

From last version, I only redacted below formats which are with street numbers, street names, city, state and ZIP code. Now, along with these formats I have also redacted without ZIP codes as well.

+ 660 Parrington Oval, Norman, OK 73019
+ 660 Parrington

  Oval, Norman, OK 73019
+ 660 Parrington, Oval

  university of oklahoma

  Norman, OK 73019
+ 660 Parrington Oval
 
  Norman, OK 73019

+ 660 Parrington Oval, Norman, OK 
+ 660 Parrington

  Oval, Norman, OK 
+ 660 Parrington, Oval

  university of oklahoma

  Norman, OK 
+ 660 Parrington Oval
 
  Norman, OK 

