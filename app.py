from flask import Flask
import pandas as pd
import main
import web_func

app = Flask(__name__)


#출력을 dfdbf 를 이용하고 관계릴레이션으로 xmldbf를 참조할 것 임
@app.route('/')
def hello_world():  # put application's code here
    dfxml, dfdbf = main.initalizeData()
    web_func.df2htmltable(dfdbf)
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
