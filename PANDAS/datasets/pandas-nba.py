from typing import KeysView
import pandas as pd

# 1)
# Numpy ve Pandas arasındaki fark ? 
# Numpy'de verilerin hepsi homojen yapıda olmak zorunda yani tek tipte olmak zorundadır ama Pandas'da homojen olmayabilir. (Daha esnek bir yapı)

# 2)
# Numpy daha çok sayısal veriler üzerinde işlem yapılması için tercih edilir.
# Pandas veri setleri üzerinde işlem yapmak için tercih edilir.

##############################################################################################

## Pandas ile bir veri objesi oluşturulur.
# dataFrame = pd.read_csv("C:/Users/melih/Desktop/Python/PANDAS/datasets/Players.csv")               

# 1- İlk 10 kaydı getir

# result = dataFrame.head(10)
# print(result)

# 2- Toplam kaç kayıt var?

# result = len(dataFrame.index)
# print(result)

##############################################################################################

# Pandas Serileri


# numbers=[12,13,14,15,16]
# print(pd.Series(numbers))
#   0    12     
#   1    13     
#   2    14     
#   3    15     
#   4    16     
#   dtype: int64



# letters=['m','n','a','c']
# print(pd.Series(letters))
#   0    m       
#   1    n       
#   2    a       
#   3    c       
#   dtype: object



# integer=10
# print(pd.Series(integer))
#   0    10
#   dtype: int64



# my_dictionary={'a':12,'b':13,'c':14,'d':15}
# print(pd.Series(my_dictionary))
#  a    12     
#  b    13     
#  c    14     
#  d    15     
#  dtype: int64


# Kural: pd.Series([data],[index])
# print(pd.Series([15,16,17,18],["A","B","C","D"]))
# A    15     
# B    16     
# C    17     
# D    18     
# dtype: int64



# DataFrame: Serilerin birleştirilmesi ile oluşur.







