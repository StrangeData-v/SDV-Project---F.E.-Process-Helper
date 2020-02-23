__version__ = 'v1'
__author__ = 'Vizerfur'
__function__ = ['del_unique_col','del_none_col','find_mul_class_col','translate',
                'none_values_description','one_hot_encoder','data_info_desc']
__last_edit_time__ = 2/23/2020

import numpy
import random
import re
import pandas
import SDV.support


# 1
def del_unique_col(df):
    """delete columns those values are just single one."""
    l = []
    for each in df:
        if len(df[each].value_counts()) == 1:
            l.append(each)
    df.drop(l,axis = 1,inplace = True)
    if len(l) > 0:
        print(f"Deleted {len(l)} features below:")
        return l
    else:
        print('No qualified feature to delete')
    
    
 # 2   
def del_none_col(df,threshold = 0.5):
    """delete those columns whose none values number is bigger than threshold."""
    l = []
    for each in df:
        if df[each].isnull().sum()/len(df[each]) > threshold:
            l.append(each)
    df.drop(l,axis = 1,inplace = True)
    if len(l) > 0:
        print(f"Deleted {len(l)} features below:")
        return l
    else:
        print('No qualified feature to delete')


# 3
def find_mul_class_col(df,threshold_of_category_num = 100,rand_num = 500):

    """
    A function for filter the object features that contain so many categories.
    Also make a infomation analysis for each object features using reguler expression.
    We divied the infomation to three types, number, alphabet and others.
    And then the function return a dataframe. Dataframe have 5 columns. 
    The meauring scaler for data structure is Percentage.
    
    ----------
    
    args:
    threshold_of_category_num(int type,default = 100): Mean the categories counts threshold. When the feature's categories number is bigger than this, then we calculate the feature, otherwise pass.
    
    rand_num(int type,default = 100) : Select rand_num sample from total data row randomly.
    """
    f = []
    f_m = []
    d_s = []
    length = len(df)

    for each in df.select_dtypes(include = 'object').columns:

        if len(df[each].value_counts()) > threshold_of_category_num:
            f.append(each)  
            f_m.append(len(df[each].value_counts()))
    
            random_list = [random.randint(0,length) for i in range(rand_num)] # select random numbers
            s = ''
            for ii in random_list:
                try:
                    string_ = str(df.iloc[ii][each])   # sometimes raise a error like 'out of range'.
                except:
                    pass
                if string_ != 'nan': # str(nan) = 'nan', so we should filter this negtive influence.
                    try:
                        s += string_.replace(' ','') # delete blanks.
                    except:
                        pass
            if len(s) == 0:
                d_s.append({'Number':0.0,'Alphabet':0.0,'Others':0.0})
            else:
                d_s.append(SDV.support.data_struc(s)) # data_struc() return a dict.

                
    return pandas.DataFrame(data ={'Object_features':f,
                               'Category_counts':f_m,
                               'Data_structure_number':[each['Number'] for each in d_s],
                               'Data_structure_alphebat':[each['Alphabet'] for each in d_s],
                               'Data_structure_others':[each['Others'] for each in d_s]})

# 4
def translate(t):
    """translate. (English to Chinese)"""
    if type(t) == pandas.core.frame.DataFrame:
        return pandas.DataFrame(data = {'Feature_name':t.columns,
                                    'Translation':[SDV.support.translate(each) for each in t.columns]})
    if type(t) ==  str:
        return SDV.support.translate(t)

# 5
def none_values_description(df,filter_ = False):
    """Count np.nan type values of dataframe and return by percentage.
    
    --------
    filter_: If filter_ is True, the returned dataframe will filter the full-value features.
    """
    fea_col = df.columns.tolist()
    length = len(df)
    null_num = [df[each].isnull().sum() for each in fea_col]
    null_penc = [i/length for i in null_num]
    return_ = pandas.DataFrame({'Feature_name':fea_col,
                        'None_values_counts':null_num,
                        'None_values_ratio':null_penc}).sort_values('None_values_ratio',ascending = False)
    return_.index = list(range(len(return_)))
    
    if filter_ is False:
        return return_
    if filter_ is True:
        return return_[return_['None_values_ratio'] > 0]

# 6
def one_hot_encoder(df,encode_list = []):
    """return a processed dataframe.If encode_list(default blank list) is not appointed, the function will processing all the object features of input datafrme. If not, then just proceesing the encode_list givend."""
    if len(encode_list) == 0:
        ojb_fea = df.select_dtypes(include = 'object')
        for each in ojb_fea:
            oh = pandas.get_dummies(df[each],prefix = each)
            df = pandas.concat([df,oh],axis = 1)
        df = df.drop(ojb_fea,axis = 1)
        return df
    else:
        for each in encode_list:
            oh = pandas.get_dummies(df[each],prefix = each)
            df = pandas.concat([df,oh],axis = 1)
        df = df.drop(ojb_fea,axis = 1)
        return df


# 7
def data_info_desc(df):
    """A all-sided description of dataframe, which is just a colloction of SVD.fea_eng function."""

    st = translate(df)
    st.index = st.Feature_name.values
    st = st.drop(['Feature_name'],axis = 1)
    
    sv = none_values_description(df)
    sv.index = sv.Feature_name.values
    sv = sv.drop(['Feature_name'],axis = 1)
    
    sm = find_mul_class_col(df,threshold_of_category_num = 0)
    sm.index = sm.Object_features.values
    sm = sm.drop(['Object_features'],axis = 1)
    
    sd = pandas.DataFrame(index = df.dtypes.index, data = df.dtypes.values, columns = ['Type'])
    
    return pandas.concat([st,sd,sv,sm],axis = 1).replace({numpy.nan:'/'})
            