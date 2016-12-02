import email
import re
import nltk
from io import StringIO
from email.generator import Generator
from nltk.tokenize import word_tokenize, sent_tokenize, RegexpTokenizer
import rarfile
import unrar
import pickle
from statistics import mean, stdev


def all_punctuation(text):
    punctuations = ['.', ',', ';', ':']
    count = 0
    for w in text:
        if w in punctuations:
            count += 1
    return count

def count_commas(text):
    count = 0
    for w in text:
        if w == ',':
            count += 1
    return count

def count_pattern(text):
    grammar = RegexpTokenizer(r'\@')
    pattern = grammar.tokenize(text)
    return len(pattern)

def count_exclamation(text):
    grammar = RegexpTokenizer(r'\!')
    pattern = grammar.tokenize(text)
    return len(pattern)

def ex_links(text):
    grammar = RegexpTokenizer(r'http?\S+\w(?:(?:\/[^\s/]*))*|www\S+\w(?:(?:\/[^\s/]*))*|ftp\S+\w(?:(?:\/[^\s/]*))*')
    pattern = grammar.tokenize(text)
    return len(pattern)

def firs_sinpronouns(text):
    sigpronouns = ['i', 'me', 'my', 'mine', 'we']
    count = 0
    for w in text:
        if w.lower() in sigpronouns:
            count += 1
    return count

def negative_particle(text):
    with open('negative-words.txt') as neg:
        neg = neg.read()
    words = nltk.word_tokenize(neg)
    grammar = RegexpTokenizer(r'\w+')
    nopunctuation = grammar.tokenize(text)
    count = 0
    for w in nopunctuation:
        if w.lower() in words:
            count += 1
    return count

def negative_emoticon(text):
    grammar = RegexpTokenizer(r"(?::|;|=)(?:-)?(?:\()")
    emoticons = grammar.tokenize(text)
    return len(emoticons)

def numbers(text):
    grammar = RegexpTokenizer(r'\d+')
    pattern = grammar.tokenize(text)
    return len(pattern)
    
def parenthesis(text):
    pat = '\([^)]*\)'
    parent = re.findall(pat, text)
    return len(parent)

def positive_emoticon(text):
    grammar = RegexpTokenizer(r'(?::|;|=)(?:-)?(?:\)|D|P)')
    emoticons = grammar.tokenize(text)
    return len(emoticons)

def prepositions(text):
    tagged = nltk.pos_tag(text)
    count = 0
    for w in tagged:
        if w[1] == 'IN':
            count += 1
        if 'txt' in w[0]:
            count = count -1
    return count

def pronouns(text):
    tagged = nltk.pos_tag(text)
    count = 0
    for w in tagged:
        if (w[1] == 'PRP' or w[1] == 'PRP$' or w[1] == 'WP' or w[1] == 'WPR$'):
            count += 1
    return count

def count_question(text):
    grammar = RegexpTokenizer(r'\?')
    pattern = grammar.tokenize(text)
    return len(pattern)

def long_words(text):
    grammar = RegexpTokenizer(r'\w{7,}')
    pattern = grammar.tokenize(text)
    return len(pattern)

def firs_pronouns(text):
    firstpronouns = ['i', 'me', 'my', 'mine', 'we', 'our', 'ours', 'us']
    count = 0
    for w in text:
        if w.lower() in firstpronouns:
            count += 1
    return count

def swears_count(text):
    with open('swears.txt') as test:
        words = test.read()
        swears = re.sub(r'[^\w+\s]+', '', words)
        swears = swears.split('\n')
        count = 0
    for w in text:
        if w.lower() in swears:
            count += 1
    return count

def typetoken_ratio(text):
    typed = set(text)
    token = text
    ratio = len(typed)/len(token)
    return ratio

def count_words(text):
    grammar = RegexpTokenizer(r'\w+')
    pattern = grammar.tokenize(text)
    return len(pattern)

def firs_pluralpronouns(text):
    pluralpronouns = ['we', 'our', 'ours', 'us']
    count = 0
    for w in text:
        if w.lower() in pluralpronouns:
            count += 1
    return count

def sec_pronouns(text):
    secpronouns = ['you', 'your', 'yours']
    count = 0
    for w in text:
        if w.lower() in secpronouns:
            count += 1
    return count

def mean_freq(text):
    mean = count_words(text) / 2
    return mean

def training(rf):
    ff1 = []
    ff2 = []
    ff3 =[]
    ff4 =[]
    ff5 =[]
    ff6= []
    ff7= []
    ff8= []
    ff9 =[]
    ff10 =[]
    ff11 =[]
    ff12 =[]
    ff13 =[]
    ff14=[]
    ff15=[]
    ff16=[]
    ff17=[]
    ff18=[]
    ff19=[]
    ff20=[]
    ff21=[]
    ff22=[]
    for f in rf.infolist()[:42]:
        f1 = f2 =f3 =f4 =f5 =f6= f7= f8= f9 =f10 =f11 =f12 =f13 =f14=f15=f16=f17=f18=f19=f20=f21=f22=0
##        print(f.filename, f.file_size)
        with rf.open(f) as file:
            for body in file:
                b = email.message_from_string(str(body))
                body = ""
                test = str(b.get_payload(decode=True))
                words = word_tokenize(str(b.get_payload(decode=True)))
                f1 = f1 + all_punctuation(words)
                f2 = f2 + count_commas(words)
                f3 = f3 + count_pattern(test)
                f4 = f4 + count_exclamation(test)
                f5 = f5 + ex_links(test)
                f6 = f6 + firs_sinpronouns(words)
                f7 = f7 + negative_particle(test)
                f8 = f8 + negative_emoticon(test)
                f9 = f9 + numbers(test)
                f10 = f10 + parenthesis(test)
                f11 = f11 + positive_emoticon(test)
                f12 = f12 + prepositions(words)
                f13 = f13 + pronouns(words)
                f14 = f14 + count_question(test)
                f15 = f15 + long_words(test)
                f16 = f16 + firs_pronouns(words)
                f17 = f17 + swears_count(words)
                f18 = f18 + typetoken_ratio(words)
                f19 = f19 + count_words(test)
                f20 = f20 + firs_pluralpronouns(words)
                f21 = f21 + sec_pronouns(words)
                f22 = f22 + mean_freq(test)
        ff1.append(f1)
        ff2.append(f2)
        ff3.append(f3)
        ff4.append(f4)
        ff5.append(f5)
        ff6.append(f6)
        ff7.append(f7)
        ff8.append(f8)
        ff9.append(f9)
        ff10.append(f10)
        ff11.append(f11)
        ff12.append(f12)
        ff13.append(f13)
        ff14.append(f14)
        ff15.append(f15)
        ff16.append(f16)
        ff17.append(f17)
        ff18.append(f18)
        ff19.append(f19)
        ff20.append(f20)
        ff21.append(f21)
        ff22.append(f22)
        

    return [ff1, ff2,ff3,ff4,ff5,ff6,ff7,ff8,ff9,ff10,ff11,ff12,ff13,ff14,ff15,ff16,ff17,ff18,ff19,ff20,ff21,ff22]
        
##save_file = open('sample_value.pickle', 'wb')
##pickle.dump(training(rf), save_file)
##save_file.close()

savedfile = open('sample_value.pickle', 'rb')
trained = pickle.load(savedfile)
savedfile.close()


rf = rarfile.RarFile('inbox1.rar')
def personality_detect(rf):
    for f in rf.infolist():
        print(f.filename)
        f1 = f2 =f3 =f4 =f5 =f6= f7= f8= f9 =f10 =f11 =f12 =f13 =f14=f15=f16=f17=f18=f19=f20=f21=f22=0
        with rf.open(f) as file:
            for body in file:
                b = email.message_from_string(str(body))
                body = ""
                test = str(b.get_payload(decode=True))
                words = word_tokenize(str(b.get_payload(decode=True)))
                f1 = f1 + all_punctuation(words)
                f2 = f2 + count_commas(words)
                f3 = f3 + count_pattern(test)
                f4 = f4 + count_exclamation(test)
                f5 = f5 + ex_links(test)
                f6 = f6 + firs_sinpronouns(words)
                f7 = f7 + negative_particle(test)
                f8 = f8 + negative_emoticon(test)
                f9 = f9 + numbers(test)
                f10 = f10 + parenthesis(test)
                f11 = f11 + positive_emoticon(test)
                f12 = f12 + prepositions(words)
                f13 = f13 + pronouns(words)
                f14 = f14 + count_question(test)
                f15 = f15 + long_words(test)
                f16 = f16 + firs_pronouns(words)
                f17 = f17 + swears_count(words)
                f18 = f18 + typetoken_ratio(words)
                f19 = f19 + count_words(test)
                f20 = f20 + firs_pluralpronouns(words)
                f21 = f21 + sec_pronouns(words)
                f22 = f22 + mean_freq(test)
        E = 0
        S = 0
        A = 0
        C = 0
        O = 0
        if f1 > (mean(trained[0])+stdev(trained[0])):
            E =E -0.08
            S=S - 0.04
            A=A - 0.01
            C=C - 0.04
            O=O - 10
        if f2 > (mean(trained[1])+stdev(trained[1])):
            E=E -0.02
            S=S + 0.01
            A=A - 0.02
            C=C - 0.01
            O=O + 0.1
        if f3 > (mean(trained[2])+stdev(trained[2])):
            E=E - 0.07
            S=S + 0.02
            A =A+ 0.01
            C =C+ 0.01
            O =O+ 0.06
        if f4 > (mean(trained[3])+stdev(trained[3])):
            E=E - 0
            S =S- 0.05
            A =A + 0.06
            C =C + 0
            O =O- 0.03
        if f5 > (mean(trained[4])+stdev(trained[4])):
            E=E - 0.05
            S =S- 0.02
            A =A- 0.01
            C =C- 0.03
            O =O+0.09
        if f6 > (mean(trained[5])+stdev(trained[5])):
            E =E+ 0.05
            S =S- 0.15
            A =A+ 0.05
            C =C+ 0.04
            O =O- 0.14
        if f7 > (mean(trained[6])+stdev(trained[6])):
            E =E-0.08
            S =S+ 0.12
            A =A+ 0.11
            C =C- 0.07
            O =O+ 0.01
        if f8 > (mean(trained[7])+stdev(trained[7])):
            E=E - 0.03
            S =S-0.18
            A =A- 0.11
            C =C- 0.11
            O =O+ 0.04
        if f9 > (mean(trained[8])+stdev(trained[8])):
            E =E- 0.03
            S =S+0.05
            A =A- 0.03
            C =C- 0.02
            O =O-0.06
        if f10 > (mean(trained[9])+stdev(trained[9])):
            E =E- 0.06
            S =S+ 0.03
            A =A- 0.04
            C =C- 0.01
            O =O+0.1
        if f11 > (mean(trained[10])+stdev(trained[10])):
            E =E+0.07
            S =S+ 0.07
            A =A+ 0.05
            C =C+ 0.02
            O =O+ 0.02
        if f12 > (mean(trained[11])+stdev(trained[11])):
            E =E+ 0
            S =S+ 0.06
            A =A+ 0.04
            C =C+ 0.08
            O =O- 0.04
        if f13 > (mean(trained[12])+stdev(trained[12])):
            E =E+ 0.07
            S =S+ 0.12
            A =A+ 0.04
            C =C+ 0.02
            O =O- 0.06
        if f14 > (mean(trained[13])+stdev(trained[13])):
            E=E - 0.06
            S =S- 0.05
            A =A- 0.04
            C =C- 0.06
            O =O+ 0.08
        if f15 > (mean(trained[14])+stdev(trained[14])):
            E =E- 0.06
            S =S+ 0.06
            A =A- 0.05
            C =C+ 0.02
            O =O+ 0.1
        if f16 > (mean(trained[15])+stdev(trained[15])):
            E=E + 0.07
            S =S- 0.14
            A =A- 0.06
            C =C- 0.04
            O =O- 0.14
        if f17 > (mean(trained[16])+stdev(trained[16])):
            E=E - 0.01
            S =S+ 0
            A =A- 0.14
            C =C- 0.11
            O =O+ 0.08
        if f18 > (mean(trained[17])+stdev(trained[17])):
            E =E- 0.05
            S =S+ 0.1
            A =A- 0.04
            C =C- 0.05
            O =O+ 0.09
        if f19 > (mean(trained[18])+stdev(trained[18])):
            E =E- 0.01
            S =S+ 0.02
            A =A+ 0.02
            C =C- 0.02
            O =O+ 0.06
        if f20 > (mean(trained[19])+stdev(trained[19])):
            E =E+ 0.06
            S =S+ 0.07
            A =A+ 0.04
            C =C+ 0.01
            O =O+ 0.04
        if f21 > (mean(trained[20])+stdev(trained[20])):
            E =E- 0.01
            S =S+ 0.03
            A =A- 0.06
            C =C- 0.04
            O =O+ 0.11
        if f22 > (mean(trained[21])+stdev(trained[21])):
            E =E+ 0.05
            S=S - 0.06
            A =A+ 0.03
            C =C+ 0.06
            O =O- 0.07
        print('E:',round(E,2),'\nS:', round(S,2),'\nA:', round(A,2),'\nO:', round(O,2))
                
                    
                    
personality_detect(rf)           
            











