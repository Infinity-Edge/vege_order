from sort_data.portion_rule_lists import *

def create_combined_dict(list1, list2):
    """
    두 개의 리스트를 입력으로 받아, 품목 이름을 키로 하고 하위 딕셔너리에서 단위와 리스트 이름을 매핑한 딕셔너리를 생성합니다.
    
    :param list1: 첫 번째 리스트 (내부 리스트 형태)
    :param list2: 두 번째 리스트 (내부 리스트 형태)
    :return: 결합된 딕셔너리
    """
    result_dict = {}

    #t_name = '22번(엽채류)'
    t_name = '209번(버섯류)'

    # 첫 번째 리스트 처리
    for item in list1:
        name, unit = item
        if name not in result_dict:
            result_dict[name] = {}
        result_dict[name][unit] = f"{t_name} 박스"

    # 두 번째 리스트 처리
    for item in list2:
        name, unit = item
        if name not in result_dict:
            result_dict[name] = {}
        result_dict[name][unit] = f"{t_name} 소분"

    return result_dict

def write_dict_to_txt(result_dict, filename):
    """
    딕셔너리 내용을 보기 좋게 텍스트 파일로 출력하는 함수.
    
    :param result_dict: 품목 및 단위 정보가 포함된 딕셔너리
    :param filename: 출력할 텍스트 파일의 이름
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("result_dict = {\n")
        for name, units in result_dict.items():
            file.write(f"    '{name}': {{\n")
            for unit, source in units.items():
                file.write(f"        '{unit}': '{source}',\n")
            file.write("    },\n")
        file.write("}\n")

# 함수 사용 예시

list1 = [['깻순', '키로'], ['아욱','키로'],['고수','단']]
list2 = [['깻순', '박스'], ['아욱','박스'],['적상추','박스']]

result_dict = create_combined_dict(list209_box, list209_por)

# 결과 출력
print(result_dict)

write_dict_to_txt(result_dict, '209번.txt')
