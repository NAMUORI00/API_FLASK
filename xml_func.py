import pickle
import API_REQUEST

vaildroadid = 4000000000 #DBF에서 제주도 도로가 시작되는 지점

# xml 트리를 이용해 유효한 LINK_ID 값만 추려서 xml_tree_nodlink.txt 파일에 저장
def xmllistdump(file_path):
    xml_tree = API_REQUEST.api_request()  # API 리퀘스트 후, XML 반환 데이터를 xml_tree 에 담기
    temp_list = list()
    for child in xml_tree.iter('list'):
        alpha = list(child)
        if int(alpha[0].text) >= vaildroadid: # DBF 파일 내의 제주도 영역이 시작되는 지점의 LINKID 부터 XML에서 로드
            node = {'LINKID':int(alpha[0].text), 'OCPY_RATE':alpha[1].text, 'PRCN_DT':alpha[2].text, 'SPED':alpha[3].text, 'TFVL':alpha[4].text, 'TRVL_HH':alpha[5].text}
            temp_list.append(node)
    with open(file_path, 'wb') as file:
        pickle.dump(temp_list, file)
    file.close()
    return 1


# xml list 덤프파일 읽어와서 리스트 생성후 리턴해주는 함수
def xmldumpopen(file_path):
    with open(file_path, 'rb') as file:
        temp_list = pickle.load(file)
    file.close()
    return temp_list


# xml_list의 LINK_ID중 최소값과 최대값을 찾습니다
def minmaxlinkid(xml_list):
    minmax = [int(xml_list[0]['LINKID']), 0]
    for count in range(len(xml_list)):
        minmax[0] = int(xml_list[count]['LINKID']) if minmax[0] > int(xml_list[count]['LINKID']) else minmax[0]
        minmax[1] = int(xml_list[count]['LINKID']) if minmax[1] < int(xml_list[count]['LINKID']) else minmax[1]
    return minmax