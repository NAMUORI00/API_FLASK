import requests
from urllib.parse import urlencode, unquote
from xml.etree import ElementTree


# API 업데이트로 인한 폐기
# 사용하지 않게된 코드
# API 리퀘스트 후, XML 반환 데이터를 xml_tree 에 담기
# xml_func.xmllistdump('dump_file/xml_tree_nodlink.txt') # xml 트리에서 유효한 LINK_ID 만 리스트로 모아서 덤프파일 생성
# xml_tree = API_REQUEST.api_request()

# xml 리턴

# xml 리턴
def api_request():
    tree = ElementTree.parse('dump_file/getTrafficInfo.xml')
    return tree

#def api_request():
#    apikey = unquote("AU%2B3Jd9M%2F4EFoqDe43gUAyFC9QwBPwKS0grAx3kbZCqeAlO9yeNzqYh0OZT0gKYtAwVeJVkihmP8MyopkaQPfg%3D%3D")
#    paramdata = {"authApiKey": apikey}
#    resp = requests.get('http://openapi.jejuits.go.kr/rfcapi/rest/jejuits/getTrafficInfo', params=paramdata)
#    tree = ElementTree.fromstring(resp.content)
#    return tree