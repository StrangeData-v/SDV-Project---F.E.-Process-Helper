# SDV-Project---F.E.-Process-Helper

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

|  ***No.*** |  Function Name | Description |
|---|---|---|
|***1***|`del_unique_col(df)`|   delete columns those values are just a single one.    |
|***2***|`del_none_col(df)`|   delete those columns whose none values number is bigger than threshold    |
|***3***|`find_mul_class_col(df)`|   A function for filter the object features that contain so many categories.Also make a infomation analysis for each object features using reguler expression.We divied the infomation to three types, number, alphabet and others.And then the function return a dataframe. Dataframe have 5 columns. The meauring scaler for data structure is Percentage    |
|***4***|`translate(s)`|    translate function. if input __s__ is a string, then function will return a translated string. If __s__ is a dataframe, then the function will return a translation dataframe of __s.columns__.   |
|***5***|`none_values_description(df)`|   Count np.nan type values of dataframe and return by percentage    |
|***6***|`one_hot_encoder(df)`|   return a processed dataframe.If encode_list(default blank list) is not appointed, the function will processing all the object features of input datafrme. If not, then just proceesing the encode_list givend    |
|***7***|`data_info_desc(df)`|    A all-sided description of dataframe, which is just a colloction of SVD.fea_eng function.   |
