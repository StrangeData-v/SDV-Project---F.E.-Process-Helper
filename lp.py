__version__ = 'v1'
__author__ = 'Vizerfur'
__function__ = ['del_punctuation','stmmerized','del_stopwords','text_fully_process']
__last_edit_time__ = '3/7/2020'


import string
import nltk
import jieba
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# 1
def del_punctuation(text,language = 'english'):
    text = text.lower()
    """
    [input:string,output:list] input a long string and output a list without punctuation and /n(enter).Both operated amony Chinese and English. 

    --------args.
    language : 'english'(default) or 'chinese'
    """
    if language == 'english':
        tranform_dict = dict([(ord(pun),None) for pun in (string.punctuation + '•')]) # '•' is also a punctuation but not exist in string.punctuation
        text = text.translate(tranform_dict)
        word_list = nltk.word_tokenize(text)

        return word_list

    if language == 'chinese':
        n_list = []
        add_punc='，。、【 】 “”：；（）《》‘’{}？！⑦()、%^>℃：.”“^-——=&#@￥...…' # add some chinese punctuations.
        punc = string.punctuation + add_punc
        for each in list(jieba.cut(text)):
            if each not in punc:
                if each != '\n':
                    n_list.append(each)

        return n_list

# 2
def stmmerized(word_list,language = 'english'):
    """
    [input:list,output:list]  A stemmer extracts the root form of a given word. In a word, simplifing the decorated word.

    --------args.
    language : 'english'(default) or 'chinese',if lanuage == 'chinese', then just return the original word_list
    """
    if language == 'english':
        stemmer = PorterStemmer()
        new_list = []
        for each in word_list:
            new_list.append(stemmer.stem(each))
        return new_list

    else:
        return word_list

# 3
def del_stopwords(word_list):
    # just delete the stopwords from words list, and return a new list
    with open('C:\\Users\\13115\\Anaconda3\\Lib\\site-packages\\SDV\\stopwords.txt',encoding='utf-8') as fr:
        stopwords_ = fr.read()
    stop = list(set(stopwords_.split() + stopwords.words()))
    
    return [w for w in word_list if w not in stop]

# 4
def text_fully_process(text,language):
    """
    [input:string,output:list]  intergration of language processing.
    --------args.
    language : 'english'(default) or 'chinese'
    """
    word_list_ = del_punctuation(text,language)
    word_list_ = stmmerized(word_list_,language)
    word_list_ = del_stopwords(word_list_)

    return word_list_
