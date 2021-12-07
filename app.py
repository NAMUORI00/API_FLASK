from flask import Flask, render_template, request
import pandas as pd
import main
import web_func
import df_func

#dbf와 xml은 초기화시 JOIN 연산되어 반환될 것임.
app = Flask(__name__)
merged = main.initalizeData() 

#paging을 위한 list화
index = {'구간번호', '도로명', '제한속도', '도로길이', '점유율', '평균속도', '교통량', '통행시간'}
dbf = merged.values.tolist()


@app.route('/')
def hello_world():  # put application's code here
    web_func.df2htmltable(merged)
    return render_template('index.html')

@app.route('/list/')
def paging():
    page = request.args.get('page', type=int, default=1)
    partiallist = main.cutList(dbf, (page-1)*10, 10)
    indexrange = range((page-1)*10+1, page*10+1)
    listview = df_func.DicToDF(partiallist, indexrange, index)
    web_func.df2htmltable(listview, "templates\page.html")
    return render_template('page.html')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
