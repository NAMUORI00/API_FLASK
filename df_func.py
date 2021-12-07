import pandas as pd


# list of dic 형식의 데이터를 DataFrame 으로 저장
def DicToDF(param1, dex = None, col = None):
    df = pd.DataFrame(param1, index=dex, columns = col)
    return df

def selectDF(param1):
    return 0