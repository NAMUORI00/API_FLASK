

# 웹 프론트 생성 및 서버 실행
# #dataframe param1
def df2htmltable(param1, pagename="templates\index.html"):
    html = param1.to_html()
    text_file = open(pagename, "w", encoding='utf-8')
    text_file.write(html)
    text_file.close()
    return 1