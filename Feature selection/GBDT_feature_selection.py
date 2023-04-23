# -*-codeing = utf-8 -*-
# @Time : 2023/3/21 13:38
# @Author : Jiahui Guan
# @File : GBDT2.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

feature=pd.read_csv('/Users/ggcl7/Desktop/THP_small_feature/small_train_test_all2.csv')
dataset=pd.read_csv('/Users/ggcl7/Desktop/THP_small_feature/small_label.csv')
# print(dataset)
# dataset=np.matrix(dataset)
#
X= feature.iloc[:,1:]
print(X)
label=dataset.iloc[:,2]
print(label)
def GBDT():
    from sklearn.feature_selection import SelectFromModel
    from sklearn.ensemble import GradientBoostingClassifier
    clf=GradientBoostingClassifier(random_state=10).fit(X,label)
    model=SelectFromModel(clf,prefit=True)
    support = model.get_support()
    selected_cols = X.columns[support]
    # newMat=model.transform(X)
    newMat = X[selected_cols]
    print(newMat)
    newMat.to_csv('/Users/ggcl7/Desktop/THP_small_feature/Train_test_all_feature_selected2.csv')
# header=False,index=False
if __name__ == '__main__':
       GBDT()