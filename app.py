from flask import Flask, render_template, request
from flask_paginate import Pagination
import pandas as pd
import main
import web_func
import df_func

#dbf와 xml은 초기화시 JOIN 연산되어 반환될 것임.
app = Flask(__name__)
merged = main.initalizeData() 

#paging을 위한 list화
index = ['구간번호', '도로명', '제한속도', '도로길이', '점유율', '평균속도', '교통량', '통행시간']
dbf = merged.values.tolist()
pp = 10
hiddenlist = [0 for i in range(len(dbf))]

#숨겨진 주소를 통해 테이블 전체를 확인할 수 있음
@app.route('/showAll/')
def hello_world():  
    web_func.df2htmltable(merged)
    return render_template('index.html')


#pagination과 css는 해당 모듈의 예제를 참조
@app.route('/')
@app.route('/', defaults={'page':1})
def paging():
    page = request.args.get('page', type=int, default=1)                    
    fakepaging = Pagination(page=page, per_page=10, total=len(dbf))         
    partiallist = main.cutList(dbf, (page-1)*pp, pp)                        #테이블 분할
    indexrange = range((page-1)*pp+1, (page-1)*pp+1+len(partiallist))       
    listview = df_func.DicToDF(partiallist, indexrange, index)              #분할된 테이블을 DF로 변환
    web_func.df2htmltable(listview, "static\page.html")                  #iframe용 html생성
    return render_template('final.html', pagination=fakepaging)

if __name__ == '__main__':
    app.run(threaded=True)
