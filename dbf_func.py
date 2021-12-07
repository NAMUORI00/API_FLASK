from dbfread import DBF
import pickle

#   도로정보 DBF 파일에서 xml_list에 있는 범위 내의 도로만 추출합니다
def dbf2dump(file_path, dump_path, xmlmin, xmlmax):
    linkdiclist = list()
    readdbf = DBF(file_path, encoding='cp949')

    for record in readdbf:
        if int(record['LINK_ID']) > xmlmin and int(record['LINK_ID']) < xmlmax:
            nodedic = dict()
            nodedic['LINKID'] = int(record['LINK_ID'])
            nodedic['ROAD_NAME'] = record['ROAD_NAME']
            nodedic['MAX_SPD'] = int(record['MAX_SPD'])
            nodedic['LENGTH'] = float(record['LENGTH'])

            linkdiclist.append(nodedic)
            #   linkdic[int(record['LINK_ID'])] = nodedic

    with open(dump_path, 'wb') as dump_file:
        pickle.dump(linkdiclist, dump_file)
    dump_file.close()
    return 1


def opendbfdump(file_path):
    with open(file_path, 'rb') as temp_file:
        temp_list = pickle.load(temp_file)
    temp_file.close()
    return temp_list


def listOFdic_search(name, lista):
    for p in lista:
        if p['LINKID'] == name:
            return p


# xmlist, dbflist
def filter_dbfdata_list(xmllist, dbflist):
    temp_list = list()
    for i in range(0, len(xmllist)):
        a = listOFdic_search(xmllist[i]['LINKID'], dbflist)
        if a is not None:
            temp_list.append(a)
    return temp_list
