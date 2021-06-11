from sklearn.preprocessing import FunctionTransformer
import pandas as pd

def upper_case(s):
    count=0
    for i in s:
        if(i.isupper()):
            count+=1
    return count 

def cust_transform(X,verbose=True):
    X = pd.DataFrame(data=X.ravel(),columns=['password'])
    X['length'] = X['password'].str.len()
    X['num_len'] = X['password'].str.count('\d')
    X['uppercase']=X['password'].apply(lambda x : upper_case(x))
    X=X.iloc[:,X.columns !='password']
    return X

col_transform = FunctionTransformer(cust_transform)


