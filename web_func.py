

# 웹 프론트 생성 및 서버 실행
# #dataframe param1
def df2htmltable(param1):
    html = param1.to_html()
    text_file = open("static\index.html", "w")
    text_file.write(html)
    text_file.close()
    return 1