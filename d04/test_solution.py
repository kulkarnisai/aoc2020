
import os
import sys
import re

required_fields = { 'byr' : '', 
                    'iyr' : '', 
                    'eyr' : '', 
                    'hgt' : '', 
                    'hcl' : '', 
                    'ecl' : '', 
                    'pid' : ''  }

ecls = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

def has_all_fields(passport):
    return all([field in passport for field in required_fields])

def valid_yr(value, minyr, maxyr):
    yrre = re.compile(r'^\d{4}')
    if yrre.fullmatch(value):
        if int(value) in range(minyr, maxyr+1):
            return True
    return False

def valid_byr(passport):
    return valid_yr(passport['byr'], 1920, 2002)

def valid_iyr(passport):
    return valid_yr(passport['iyr'], 2010, 2020)
    

def valid_eyr(passport):
    return valid_yr(passport['eyr'], 2020, 2030)

def valid_hgt(passport):
    inre = re.compile(r'^\d{2}in')
    cmre = re.compile(r'^\d{3}cm')
    if inre.fullmatch(passport['hgt']):
        return int(passport['hgt'][:2]) in range(59, 76+1)
    elif cmre.fullmatch(passport['hgt']):
        return int(passport['hgt'][:3]) in range(150, 193+1)
    return False


def valid_hcl(passport):
    hclre = re.compile(r'^\#[a-fA-F0-9]{6}')
    return hclre.fullmatch(passport['hcl']) is not None

def valid_ecl(passport):
    return passport['ecl'] in ecls

def valid_pid(passport):
    pidre = re.compile(r'^\d{9}')
    return pidre.fullmatch(passport['pid']) is not None 


def has_valid_fields(passport):
    if has_all_fields(passport):
        if valid_byr(passport):
            if valid_iyr(passport):
                if valid_eyr(passport):
                    if valid_hgt(passport):
                        if valid_hcl(passport):
                            if valid_ecl(passport):
                                if valid_pid(passport):
                                    return True
    return False

def count_valid_passports1(passports):
    valid = [1 if has_all_fields(passport) else 0 for passport in passports]
    return sum(valid)


def count_valid_passports(passports):
    valid = [1 if has_valid_fields(passport) else 0 for passport in passports]
    return sum(valid)

def parse_passports(passports):
    pdicts = []
    for passport in passports:
        pdict = {}
        for field in passport.split(' '):
            if field:
                [key, value] = field.split(":")
                pdict[key] = value
        pdicts.append(pdict)
    return pdicts
        

def preprocess(fname):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    
    with open(fpath) as f:
        lines = f.readlines()

    passports = []
    currpassport = ''
    for line in lines:
        if len(line) > 1:
            currpassport = currpassport + ' ' + line[:-1]
        else:
            passports.append(currpassport)
            currpassport = ''

    if currpassport: passports.append(currpassport)
    return parse_passports(passports)

def test_day4(outfile):

    test_passports1 = preprocess("test_input1")
    test_passports2 = preprocess("test_input2")
    passports = preprocess("input")

    if outfile:
        log = open(outfile, 'a')
        sys.stdout = log  
        header = '## '
        codeblock = '\n```'
    else:
        header = ''
        codeblock = ''

    print(header + "Day 4 Results:" + codeblock)

    assert count_valid_passports1(test_passports1) == 2
    print("P1:\t" + str(count_valid_passports1(passports)))

    assert count_valid_passports(test_passports2) == 4
    print("P2:\t" + str(count_valid_passports(passports)) + codeblock)

if __name__ == "__main__":
    test_day4(None)