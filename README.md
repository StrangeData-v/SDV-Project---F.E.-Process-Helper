# SDV-Project---F.E.-Process-Helper
`Sycain Vizerfur` `continuous updating`
## BRIEF INTRODUCTION:

This is a package used for engineering feature process, which could make it easier for recognizing and processing the original data. 

## COMPONENTS:
#### `fea_eng` : Mainbody part of SDV package involved all funtions.
#### `support` : Support functions of fea_eng.

## Functions:
#### Function list:

```
['del_unique_col','del_none_col','find_mul_class_col','translate','none_values_description','one_hot_encoder','data_info_desc']
```

#### Demonstration Sample: [example.ipynb](https://github.com/StrangeData-v/SDV-Project---F.E.-Process-Helper/blob/master/example.ipynb)


#### Functions Description:
#### Fea_eng:
|  ***No.*** |  Function Name | Description |
|---|---|---|
|***1***|`del_unique_col(df)`|   delete columns those values are just a single one.    |
|***2***|`del_none_col(df,threshold = 0.5)`|   delete those columns whose none values number is bigger than threshold    |
|***3***|`find_mul_class_col(df,threshold_of_category_num = 100,rand_num = 500)`|   A function for filter the object features that contain so many categories.Also make a infomation analysis for each object features using reguler expression.We divied the infomation to three types, number, alphabet and others.And then the function return a dataframe. Dataframe have 5 columns. The meauring scaler for data structure is Percentage    |
|***4***|`translate(s)`|    translate function. if input __s__ is a string, then function will return a translated string. If __s__ is a dataframe, then the function will return a translation dataframe of __s.columns__.   |
|***5***|`none_values_description(df,filter_ = False)`|   Count np.nan type values of dataframe and return by percentage    |
|***6***|`one_hot_encoder(df,encode_list = [])`|   return a processed dataframe.If encode_list(default blank list) is not appointed, the function will processing all the object features of input datafrme. If not, then just proceesing the encode_list givend    |
|***7***|`data_info_desc(df)`|    A all-sided description of dataframe, which is just a colloction of SVD.fea_eng function.   |

#### lp:
|***1***|`del_punctuation(text,language = 'english')`|   [input:string,output:list] input a long string and output a list without punctuation and /n(enter).Both operated amony Chinese and English.    --------args: language : 'english'(default) or 'chinese'    |
|***2***|`stmmerized(word_list,language = 'english')`|   [input:list,output:list]  A stemmer extracts the root form of a given word. In a word, simplifing the decorated word.    --------args:language : 'english'(default) or 'chinese',if lanuage == 'chinese', then just return the original word_list  |
|***3***|`del_stopwords(word_list)`|   just delete the stopwords from words list, and return a new list   |
|***4***|`text_fully_process(text,language)`|     [input:string,output:list]  intergration of language processing. --------args:language : 'english'(default) or 'chinese'   |
