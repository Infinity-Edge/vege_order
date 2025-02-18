import pandas as pd
import os
import re
from collections import defaultdict
from datetime import datetime
import xlsxwriter
from sort_data.classification_rule import *
from sort_data.portion_rule_lists import *


def remove_parentheses(text):
    # 정규식으로 괄호 및 괄호 안의 내용 제거
    return re.sub(r'\(.*?\)', '', text).strip()

def quan_unit_extracter(quan_unit):
    """
    수량과 단위를 분리하는 함수. 수량과 단위가 합쳐진 문자열을 받아 수량과 단위를 출력.
    추출한 문자열이 수량과 단위 조건에 해당하지 못할 경우 해당 자리에 빈 문자열을 출력함.
    
    :param quan_unit: 수량과 단위가 합쳐진 문자열
    :return: 수량, 단위
    """
    total_list = list(quan_unit)
    new_quan = ''
    new_unit = ''
    for i in range(0, len(total_list)):
        if str.isdigit(total_list[i]) or str(total_list[i]) == '+' or str(total_list[i]) == '.':
            new_quan = f'{new_quan}{total_list[i]}'
        else:
            new_unit = f'{new_unit}{total_list[i]}'

    if new_quan and new_unit:
        return new_quan, new_unit
    elif str.isdigit(new_quan):
        return new_quan, ''
    elif new_unit:
        return '', new_unit
    else:
        return '', ''
    
def wherebuy_tagger(name, unit):

    where = ''

    for key, values in classification_rule.items():
        if name in values:
            where = str(key).strip()
            if where == '22번(엽채류)':
                if name in portion_rule315:
                    if unit in portion_rule315[name]:
                        where = portion_rule315[name][unit]

            elif where == '209번(버섯류)':
                if name in portion_rule209:
                    if unit in portion_rule209[name]:
                        where = portion_rule209[name][unit]

            elif where == '과일':
                if unit =='박스':
                    where = '과일_박스'
                else:
                    where = '과일_소분'
        #else :
        #    where = ''

    return where

def name_unit_correction(name, unit):

    if name in name_unit_matching:
        if unit in name_unit_matching[name]:
            unit = name_unit_matching[name][unit]

    return unit

def extract_a_column_data(file_paths, exclude_sheets):
    # 결과를 저장할 딕셔너리 초기화
    data_dict = {}

    # 각 파일을 순회하면서 A열 데이터 추출
    for file_path in file_paths:
        # 엑셀 파일 읽기
        xls = pd.ExcelFile(file_path, engine='openpyxl')
        
        # 각 시트를 순회하면서 A열 데이터만 추출
        for sheet_name in xls.sheet_names:
            # 제외할 시트인지 확인
            if sheet_name in exclude_sheets:
                continue
            
            # A열만 읽기, 헤더가 없는 경우를 처리하기 위해 header=None 사용
            df = pd.read_excel(xls, sheet_name=sheet_name, usecols='A', header=None)
            
            # A열이 존재하는지 확인하고, 존재하면 데이터를 저장
            if df.shape[1] > 0:  # A열이 존재하면
                # 기존에 시트 이름이 존재한다면, 데이터를 이어붙이기
                if sheet_name in data_dict:
                    data_dict[sheet_name].extend(df.iloc[:, 0].dropna().tolist())
                else:
                    # 존재하지 않으면 새로운 리스트로 저장
                    data_dict[sheet_name] = df.iloc[:, 0].dropna().tolist()

    return data_dict

def extract_item_details(data_dict):
    """
    data_dict의 각 값을 분석하여 품목명, 수량, 단위를 추출하는 함수.
    
    :param data_dict: 시트 이름을 키로 하고, 각 시트의 데이터를 리스트로 저장한 딕셔너리
    :return: 각 키에 대해 품목명, 수량, 단위, 담당자를 저장한 새로운 딕셔너리
    """
    result_dict = {}

    for key, values in data_dict.items():
        extracted_data = []
        
        for item in values:
            item_str = str(item).strip()
            # 1. 품목명과 수량+단위 구분
            num_tester = item_str.split(' ')
            if len(num_tester) < 2:
                extracted_data.append({
                    '품목명': item_str.strip(),
                    '수량': "",
                    '단위': "",
                    '담당자': str(key).strip(),
                    '구매처' : "",
                })
                continue
            
            item_name, quantity_unit = item_str.rsplit(' ', 1)

            item_name = item_name.strip()

            if item_name in brakets_correction:
                item_name = brakets_correction[item_name]

            sub_name = ''
            sub_unit = ''

            if '(' in item_name :
                main_name = item_name.split('(')
                item_name = main_name[0]
                sub_name = f'({main_name[1]}'

            if '(' in quantity_unit :
                main_unit = quantity_unit.split('(')
                quantity_unit = main_unit[0]
                sub_unit = f'({main_unit[1]}'

            if quantity_unit in unit_quan_correction:
                quantity_unit = unit_quan_correction[quantity_unit]

            # 2. 수량과 단위 구분

            quantity, unit = quan_unit_extracter(quantity_unit)
            if quantity and unit:

                tmp_name = item_name.strip()

                if tmp_name in name_correction:
                    tmp_name = name_correction[tmp_name]

                tmp_unit = unit.strip()

                if tmp_unit in unit_correction:
                    tmp_unit = unit_correction[tmp_unit]

                # 수량이 '개'일경우 변환
                if tmp_unit == '개':
                    #print(tmp_name+" "+tmp_unit)
                    for mat_key, mat_values in gae_unit_matching.items():
                        if tmp_name in mat_values:
                            tmp_unit = str(mat_key).strip()
                            #print(tmp_name+" "+tmp_unit)

                # 품목명에 다른 단위 통일

                tmp_unit = name_unit_correction(tmp_name.strip(), tmp_unit)

                where = wherebuy_tagger(tmp_name, tmp_unit)

                extracted_data.append({
                    '품목명': tmp_name.strip()+sub_name,
                    '수량': quantity.strip(),
                    '단위': tmp_unit.strip()+sub_unit,
                    '담당자' : str(key).strip(),
                    '구매처' : where,
                })
            else:
                extracted_data.append({
                    '품목명': item_str.strip(),
                    '수량': "",
                    '단위': "",
                    '담당자': str(key).strip(),
                    '구매처' : "",
                })
        
        result_dict[key] = extracted_data
    return result_dict

def  team_grouping(data_dict, teams):
    """
    주어진 dictionary에서 특정 키를 그룹화하고, 기존 딕셔너리를 수정하여 새 키 값으로 변경하는 함수.
    
    :param data_dict: 시트 이름을 키로 하고, A열 데이터를 저장한 딕셔너리
    :param teams: 팀별로 그룹화할 키 목록의 이중 리스트, 예: [['동헌', '치원', '정현'], ['광일', '태경', '승민']]
    :return: 수정된 원래의 data_dict (inplace 수정)
    """
    for index, team in enumerate(teams, 1):
        # 유효한 멤버만 포함한 리스트 생성
        valid_members = [member for member in team if member in data_dict]

        # 유효한 멤버가 2명 이상인 경우에만 그룹화 진행
        if len(valid_members) > 1:
            # 새로운 키 이름 생성 (순서에 따른 팀 이름)
            new_key = f'{index}팀(' + '-'.join(valid_members) + ')'
            # 팀 멤버들을 합쳐서 새로운 키로 데이터를 저장
            new_data = []

            for member in valid_members:
                new_data.extend(data_dict[member])

            # 새 키에 데이터 저장
            data_dict[new_key] = new_data

            # 기존 멤버 키 삭제
            for member in valid_members:
                del data_dict[member]

    return data_dict

def classify_and_aggregate(data):
    purchase_categories = [
        '22번(엽채류)_소분', '209번(버섯류)_소분', '22번(엽채류)_박스', '209번(버섯류)_박스', 
        '240번(숙주,나물)', '165번(고추,피망)', '33번(가지,오이)', '특수야채', '127번(깐쪽파)', 
        '과일_박스', '과일_소분', '314번', '부추', '가게', '계란', '사입', '푸드이엠', '상관없는거', '모름', '현황보고'
    ]
    
    classified_data = defaultdict(list)

    for team, items in data.items():
        for item in items:
            purchase_location = item['구매처'].strip() if item['구매처'] else '모름'
            purchase_location = purchase_location.replace(" ", "_")  # 공백을 제거한 문자열로 변경
            
            if purchase_location in purchase_categories:
                if purchase_location in ['22번(엽채류)_소분', '209번(버섯류)_소분']:
                    key = (team, item['품목명'], item['단위'])
                    found = False
                    for existing_item in classified_data[purchase_location]:
                        if (existing_item['팀'], existing_item['품목명'], existing_item['단위']) == key:
                            # 기존 수량과 새 수량을 합치고 정렬
                            all_quantities = existing_item['수량'].split('+') + item['수량'].split('+')
                            all_quantities = list(filter(None, all_quantities))  # 빈 문자열 제거
                            all_quantities = sorted(map(float, all_quantities))  # 숫자로 변환하여 정렬
                            # 정수형과 실수형 구분하여 문자열 결합
                            formatted_quantities = [str(int(q)) if q.is_integer() else str(q) for q in all_quantities]
                            existing_item['수량'] = '+'.join(formatted_quantities)  # 다시 문자열로 결합
                            found = True
                            break
                    if not found:
                        classified_data[purchase_location].append({
                            '팀': team,
                            '품목명': item['품목명'],
                            '수량': item['수량'],
                            '단위': item['단위'],
                            '담당자': item['담당자']  # 담당자 정보 추가
                        })
                else:
                    key = (item['품목명'], item['단위'])
                    found = False
                    for existing_item in classified_data[purchase_location]:
                        if (existing_item['품목명'], existing_item['단위']) == key:
                            # 기존 수량과 새 수량을 합치고 정렬
                            all_quantities = existing_item['수량'].split('+') + item['수량'].split('+')
                            all_quantities = list(filter(None, all_quantities))  # 빈 문자열 제거
                            all_quantities = sorted(map(float, all_quantities))  # 숫자로 변환하여 정렬
                            # 정수형과 실수형 구분하여 문자열 결합
                            formatted_quantities = [str(int(q)) if q.is_integer() else str(q) for q in all_quantities]
                            existing_item['수량'] = '+'.join(formatted_quantities)  # 다시 문자열로 결합
                            found = True
                            break
                    if not found:
                        classified_data[purchase_location].append({
                            '품목명': item['품목명'],
                            '수량': item['수량'],
                            '단위': item['단위'],
                            '담당자': item['담당자']  # 담당자 정보 추가
                        })
            else:
                item['구매처'] = purchase_location  # '미분류품목' 처리 시, 구매처 추가
                classified_data['미분류품목'].append(item)
                    
    return classified_data

def sum_or_group_quantity(quantity_str):
    """
    수량 문자열을 합산하거나 그룹화하는 함수.
    """
    if '+' in quantity_str:
        quantities = sorted([float(q) for q in quantity_str.split('+') if q.replace('.', '', 1).isdigit()])  # 빈 문자열 무시 및 숫자 변환
        tmp_quan = sum(quantities)
        if tmp_quan * 10 % 10 == 0: tmp_quan = int(sum(quantities)) 
        return str(tmp_quan)
    return quantity_str

def sum_checker(name, unit):
    if name in no_add_product_by_unit:
        if unit in no_add_product_by_unit[name]:
            return False

    return True

def save_to_excel(classified_data, filename):
    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        workbook = writer.book

        # 합산하지 않을 구매처 지정
        no_add_rule = ['127번(깐쪽파)', '계란', '부추','과일_박스','과일_소분', '사입','미분류품목']

        # 정렬하지 않을 구매처 지정
        no_sort_rule = ['모름']

        # '22번(엽채류)_소분'과 '209번(버섯류)_소분' 시트 생성
        for sheet_name in ['22번(엽채류)_소분', '209번(버섯류)_소분']:
            if sheet_name in classified_data:
                team_data = defaultdict(list)
                for item in classified_data[sheet_name]:
                    team_data[item['팀']].append({
                        '품목명': item['품목명'],
                        '수량': item['수량'],
                        '단위': item['단위']
                    })

                df = pd.DataFrame()
                
                for i, (team, items) in enumerate(team_data.items()):
                    temp_df = pd.DataFrame({
                        '품목명': [item['품목명'] for item in items],
                        '수량': [item['수량'] for item in items],
                        '단위': [item['단위'] for item in items]
                    })
                    temp_df = temp_df.sort_values(by=['품목명']).reset_index(drop=True)  # 품목명 기준 오름차순 정렬
                    df = pd.concat([df, temp_df], axis=1, ignore_index=False)  # 팀별로 병합

                # 팀 이름 병합하여 첫 번째 행에 추가
                #df.columns = pd.MultiIndex.from_product([[team for team in team_data.keys()], ['품목명', '수량', '단위']])
                df.to_excel(writer, sheet_name=sheet_name, startrow=1, index=False)
                worksheet = writer.sheets[sheet_name]
                for i, team in enumerate(team_data.keys()):
                    worksheet.merge_range(0, i * 3, 0, i * 3 + 2, team, workbook.add_format({'align': 'center', 'valign': 'vcenter'}))
                
                # 수량 열을 오른쪽 정렬하고 너비 설정
                for i in range(len(team_data)):
                    worksheet.set_column(i * 3 + 1, i * 3 + 1, 15, workbook.add_format({'align': 'right'}))  # 수량 열 오른쪽 정렬 및 너비 설정

        # 그룹1번, 그룹2번, 그룹3번 시트 생성
        group1 = ['22번(엽채류)_박스', '209번(버섯류)_박스', '240번(숙주,나물)', '165번(고추,피망)']
        group2 = ['33번(가지,오이)', '127번(깐쪽파)', '과일_박스','과일_소분','314번','부추']
        group3 = ['가게', '계란','특수야채', '푸드이엠']
        groups = [('그룹1번', group1), ('그룹2번', group2), ('그룹3번', group3)]
        #groups = [('그룹1번', group1)]
        
        for sheet_name, group in groups:
            df = pd.DataFrame()
            col = 0
            for purchase_location in group:
                if purchase_location in classified_data:
                    items = classified_data[purchase_location]
                    # 수량 합산
                    if not purchase_location in no_add_rule:
                        for item in items:
                            if sum_checker(item['품목명'], item['단위']):
                                item['수량'] = sum_or_group_quantity(item['수량'])
                    temp_df = pd.DataFrame({
                        '품목명': [item['품목명'] for item in items],
                        '수량': [item['수량'] for item in items],
                        '단위': [item['단위'] for item in items]
                    })
                    temp_df = temp_df.sort_values(by=['품목명']).reset_index(drop=True)  # 품목명 기준 오름차순 정렬
                    df = pd.concat([df, temp_df], axis=1)
                    col += 3  # 세 칸씩 이동

            df.to_excel(writer, sheet_name=sheet_name, startrow=1, index=False)
            worksheet = writer.sheets[sheet_name]
            for i, purchase_location in enumerate(group):
                if purchase_location in classified_data:
                    worksheet.merge_range(0, i * 3, 0, i * 3 + 2, purchase_location, workbook.add_format({'align': 'center', 'valign': 'vcenter'}))
                
                # 수량 열을 오른쪽 정렬하고 너비 설정
                for i in range(len(group)):
                    worksheet.set_column(i * 3 + 1, i * 3 + 1, 15, workbook.add_format({'align': 'right'}))  # 수량 열 오른쪽 정렬 및 너비 설정

        # 그룹4번 시트 생성
        group4 = ['사입', '미분류품목', '모름', '현황보고','상관없는거']
        df = pd.DataFrame()
        col = 0
        for purchase_location in group4:
            if purchase_location in classified_data:
                items = classified_data[purchase_location]
                
                # 수량과 단위가 있는 것과 없는 것을 분리
                items_with_quantity = [item for item in items if item['수량'] and item['단위']]
                items_without_quantity = [item for item in items if not (item['수량'] and item['단위'])]
                
                # 수량 합산
                if not purchase_location in no_add_rule:
                    for item in items_with_quantity:
                        if sum_checker(item['품목명'], item['단위']):
                            item['수량'] = sum_or_group_quantity(item['수량'])

                temp_df = pd.DataFrame({
                    '품목명': [item['품목명'] for item in items_with_quantity] + [item['품목명'] for item in items_without_quantity],
                    '수량': [item['수량'] for item in items_with_quantity] + [''] * len(items_without_quantity),
                    '단위': [item['단위'] for item in items_with_quantity] + [''] * len(items_without_quantity),
                    '담당자': [item['담당자'] for item in items_with_quantity] + [item['담당자'] for item in items_without_quantity]
                })
                if not purchase_location in no_sort_rule: temp_df = temp_df.sort_values(by=['품목명']).reset_index(drop=True)  # 품목명 기준 오름차순 정렬
                df = pd.concat([df, temp_df], axis=1)
                col += 4  # 네 칸씩 이동
               
        df.to_excel(writer, sheet_name='그룹4번', startrow=1, index=False)
        worksheet = writer.sheets['그룹4번']
        for i, purchase_location in enumerate(group4):
            if purchase_location in classified_data:
                worksheet.merge_range(0, i * 4, 0, i * 4 + 3, purchase_location, workbook.add_format({'align': 'center', 'valign': 'vcenter'}))
                
                # 수량 열을 오른쪽 정렬하고 너비 설정
                for i in range(len(group4)):
                    worksheet.set_column(i * 4 + 1, i * 4 + 1, 15, workbook.add_format({'align': 'right'}))  # 수량 열 오른쪽 정렬 및 너비 설정

def merge_quantities(수량):
    """
    여러 수량 값을 받아서 오름차순으로 정렬한 뒤 결합.
    소수점 아래 자리가 없는 경우 정수로 변환.
    """
    
    try:
        # 수량이 '+'로 결합된 형태라면 이를 분리해서 정렬
        수량_list = sorted(map(float, 수량.split('+')))
        
        # 정수로 변환할 수 있으면 정수로 변환
        결합된_수량 = []
        for qty in 수량_list:
            if qty.is_integer():  # 소수점 이하 자리가 0이면 정수로 변환
                결합된_수량.append(str(int(qty)))
            else:
                결합된_수량.append(str(qty))

        # 오름차순 정렬된 수량을 다시 '+'로 결합
        return '+'.join(결합된_수량)
    except Exception as e:
        print(f"수량 병합 에러: {e}")
        return 수량  # 문제가 발생하면 원래 수량 반환
    
# 1. 품목과 단위가 동일한 항목에 대해 수량을 결합하고, sep_rule에 따라 정수형 수량을 분리하여 새로운 항목 생성
def merge_quantities_by_item_with_sep(data, create_new_items=False):
    merged_data = defaultdict(lambda: {"수량": "", "총계": 0})

    def extract_numbers(quantity_string):
        # 수량 문자열에서 숫자만 추출하여 리스트로 반환
        return [float(q) for q in re.findall(r"[-+]?\d*\.\d+|\d+", quantity_string)]

    for item in data:
        품목명 = item[0]
        수량 = item[1]
        단위 = item[2]

        # 기존 수량을 숫자 리스트로 변환
        current_quantities = merged_data[(품목명, 단위)]["수량"]
        if current_quantities:
            # 기존 수량을 분리한 후 새 수량 추가
            all_quantities = extract_numbers(current_quantities) + extract_numbers(수량)
        else:
            all_quantities = extract_numbers(수량)

        # 오름차순으로 정렬
        all_quantities = sorted(all_quantities)
        
        # 정수로 표현 가능한 것은 정수형으로, 그렇지 않으면 소수로 유지하여 결합
        merged_data[(품목명, 단위)]["수량"] = '+'.join(str(int(q)) if q.is_integer() else str(q) for q in all_quantities)

        # 수량의 총합 계산
        총계 = sum(all_quantities)
        merged_data[(품목명, 단위)]["총계"] = int(총계) if 총계.is_integer() else 총계

        '''
        if 품목명 == '대파':
            print(f"전 {품목명} {단위}")
            print(f"품목일치 여부 : {품목명 in sep_rule}")
            print(f"단위일치 여부 : {단위 in sep_rule[품목명]} / {sep_rule[품목명]}")
        '''

        # sep_rule에 따른 새로운 품목 생성 및 merged_data에 추가 (옵션에 따라 동작)
        if create_new_items and 품목명 in sep_rule and 단위 in sep_rule[품목명]:
            수량_list = all_quantities  # 이미 정렬된 수량 리스트 사용
            new_quantities = defaultdict(int)
            
            # 실수형 수량과 정수형 수량을 분리하여 처리
            non_integer_quantities = []
            integer_quantities = []

            for qty in 수량_list:
                if qty.is_integer():
                    integer_quantities.append(int(qty))  # 정수형은 따로 저장
                else:
                    non_integer_quantities.append(qty)  # 실수형 수량 따로 저장

            # 실수형 수량이 존재하는 경우, 정수형 수량에 대한 새로운 품목 생성
            if non_integer_quantities:
                # 기존 품목의 소수형 수량은 남겨둠
                merged_data[(품목명, 단위)]["수량"] = '+'.join(str(qty) for qty in non_integer_quantities)
            else:
                # 수량이 모두 정수인 경우, 해당 품목의 수량 필드가 비어 있으면 삭제
                merged_data.pop((품목명, 단위), None)

            # 정수형 수량에 대한 새로운 품목 생성
            for qty in integer_quantities:
                new_quantities[qty] += 1  # 정수형 수량의 개수 기록

            # 정수형 수량으로 새로운 품목명 생성 및 merged_data에 추가
            for key, value in new_quantities.items():
                new_item_name = f"{품목명}({key}{단위})"
                if (new_item_name, "봉") in merged_data:
                    기존_수량 = int(merged_data[(new_item_name, "봉")]["수량"])
                    merged_data[(new_item_name, "봉")]["수량"] = str(기존_수량 + value)
                    merged_data[(new_item_name, "봉")]["총계"] += value
                else:
                    merged_data[(new_item_name, "봉")] = {"수량": str(value), "총계": value}

        # 품목 이름을 기준으로 merged_data 정렬
        sorted_merged_data = dict(sorted(merged_data.items(), key=lambda x: x[0][0]))

    return sorted_merged_data

# 수량 문자열을 합산하는 함수
def calculate_total(quantity_str):
    
    quantities = [int(q) for q in quantity_str.split('+') if q.isdigit()]  # 숫자를 추출하고 합산
    return sum(quantities)

# 1. 품목과 단위가 동일한 항목에 대해 수량을 결합하는 함수
def merge_quantities_by_item(data):
    merged_data = defaultdict(lambda: {'수량': [], '총계': 0})

    for 품목명, 수량, 단위, 총계 in data:
        key = (품목명, 단위)
        
        # 수량을 리스트에 추가 (숫자로 변환)
        merged_data[key]['수량'].extend(map(float, str(수량).split('+')))
        
        # 총계는 개별 항목마다 합산됨
        merged_data[key]['총계'] += 총계

    # 오름차순으로 정렬 후 결합된 수량 반환
    for key in merged_data:
        # 수량을 오름차순 정렬
        sorted_quantities = sorted(merged_data[key]['수량'])
        
        # 각 수량에 대해 소수점 아래 자리가 없으면 정수로 변환
        merged_data[key]['수량'] = '+'.join(
            [str(int(q)) if q.is_integer() else str(q) for q in sorted_quantities]
        )

    return merged_data

def save_sorted_products(classified_data, filename):
    # 1. 담당자별로 데이터를 분류
    담당자별_데이터 = defaultdict(list)
    
    for category, items in classified_data.items():
        for item in items:
            담당자 = item.get('담당자')
            if 담당자:
                담당자별_데이터[담당자].append(item)

    # 2. total_portion_rule에 따른 품목 분류 함수
    def classify_by_portion_rule(품목명, 단위):
        tmp_품목 = remove_parentheses(품목명).strip()
        tmp_단위 = remove_parentheses(단위).strip()

        out_tag = None

        for tag, rules in total_portion_rule.items():
            for rule in rules:
                rule_품목 = rule.get('품목')
                rule_단위 = rule.get('단위')
                if rule_품목 == tmp_품목 and rule_단위 == tmp_단위:
                    out_tag = tag# 품목명과 단위가 모두 일치하면 태그 반환
                    return out_tag
        
        if not out_tag and tmp_단위 == '박스':
            out_tag = '박스모음'
            return out_tag

        #print(f"미분류 처리된 품목: {품목명}, 단위: {단위}")
        return '나머지'  # 규칙에 맞지 않으면 '미분류'로 처리

    # 3. 엑셀 파일 생성 및 저장
    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        workbook = writer.book
        전체_데이터 = defaultdict(list)

        # 테두리 설정
        border_format = workbook.add_format({'border': 1})

        for 담당자, items in 담당자별_데이터.items():
            sheet_name = str(담당자)
            '''
            
            if sheet_name == '한울':
                continue
            '''

            worksheet = workbook.add_worksheet(sheet_name)

            # A1 셀에 담당자 이름을 굵게, 14pt로 설정
            worksheet.write('A1', sheet_name, workbook.add_format({'bold': True, 'font_size': 14}))

            # A2에 '품목명', B2에 '수량', C2에 '단위', D2에 '총계' 문자열 기입
            worksheet.write('A2', '품목명')
            worksheet.write('B2', '수량')
            worksheet.write('C2', '단위')
            worksheet.write('D2', '총계')

            row = 3  # 3번째 행부터 데이터 입력

            # 담당자별 데이터에서 total_portion_rule에 따라 품목 분류 및 중복 제거
            태그별_데이터 = defaultdict(list)
            품목_중복처리 = defaultdict(dict)
            
            # 태그에 따라 데이터를 분류 및 중복처리
            for item in items:
                품목명 = item['품목명'].strip()
                수량 = item['수량'].strip()
                단위 = item['단위'].strip()
                담당자 = item['담당자'].strip()
                
                if 품목명 == '' or 단위 == '':
                    continue

                # 분류 규칙에 따라 태그와 단위를 결정
                분류태그 = classify_by_portion_rule(품목명, 단위)
                key = (품목명, 단위)
                
                # 동일한 품목명과 단위에 대해서 수량 결합
                if key in 품목_중복처리:
                    기존_수량 = 품목_중복처리[key]['수량']
                    if 수량:
                        tmp_수량 = 기존_수량 + '+' + 수량 if 기존_수량 else 수량
                        tmp_수량 = merge_quantities(tmp_수량)
                        품목_중복처리[key]['수량'] = tmp_수량
                else:
                    품목_중복처리[key] = {
                        '품목명': 품목명,
                        '수량': 수량,
                        '단위': 단위,
                        '분류태그' : 분류태그,
                    }


            # 중복처리된 데이터로 태그별 정리
            for key, values in 품목_중복처리.items():
                품목명, 단위 = key
                수량 = values['수량']
                분류태그 = values['분류태그']
                태그별_데이터[분류태그].append((품목명, 수량, 단위))

            # 미리 지정된 태그 순서로 데이터를 기록
            for 태그 in 태그_순서:
                if 태그 in 태그별_데이터:
                    # 태그 이름을 한 줄 기록
                    worksheet.write(row, 0, 태그, workbook.add_format({'bold': True, 'font_size': 12}))
                    row += 1

                    # 태그에 속한 품목 기록
                    for 품목명, 수량, 단위 in 태그별_데이터[태그]:
                        worksheet.write(row, 0, 품목명, workbook.add_format({'font_size': 12}))
                        worksheet.write(row, 1, 수량, workbook.add_format({'font_size': 12}))   # 수량
                        worksheet.write(row, 2, 단위, workbook.add_format({'font_size': 12}))   # 단위
                        
                        print(품목명)
                        총계 = sum(map(float, 수량.split('+'))) if '+' in 수량 else float(수량)
                        worksheet.write(row, 3, str(총계), workbook.add_format({'font_size': 12})) # 총계
                        row += 1
                        # 총정리 시트를 위해 데이터를 전체에 저장
                        if not sheet_name == '한울':
                            전체_데이터[태그].append((품목명, 수량, 단위, 총계))

                    row += 1  # 태그와 태그 사이에 한 줄 띄우기

            # A열과 B열의 너비를 데이터 길이에 맞춰 조정 (품목명, 수량만 고려)
            worksheet.set_column('A:A', max([len(품목명) for 품목명, _, _ in 태그별_데이터[태그]] + [20]))
            worksheet.set_column('B:B', max([len(str(수량)) for _, 수량, _ in 태그별_데이터[태그]] + [20]))
            worksheet.set_column('C:C', max([len(단위) for _, _, 단위 in 태그별_데이터[태그]] + [15]))

            # 테두리 그리기 (데이터가 있는 모든 셀에 적용)
            worksheet.conditional_format(f'A2:D{row}', {'type': 'no_blanks', 'format': border_format})

        # 4. 총정리 시트 만들기
        summary_sheet = workbook.add_worksheet('총정리')
        summary_sheet.write('A1', '품목명')
        summary_sheet.write('B1', '수량')
        summary_sheet.write('C1', '단위')
        summary_sheet.write('D1', '총계')

        summary_row = 2

        # 2. 총정리 시트 작성
        for 태그 in 태그_순서:
            if 태그 in 전체_데이터:
                #print(f'{전체_데이터}')
                summary_sheet.write(summary_row, 0, 태그, workbook.add_format({'bold': True, 'font_size': 12}))
                summary_row += 1

                # 중복된 품목과 단위를 수량 결합 및 sep_rule에 따른 품목 추가
                merged_data = merge_quantities_by_item_with_sep(전체_데이터[태그], True)

                for (품목명, 단위), details in merged_data.items():
                    수량 = details["수량"]
                    총계 = sum(map(float, 수량.split('+'))) if '+' in 수량 else float(수량)


                    # 품목명과 수량, 단위, 총계를 엑셀 시트에 작성
                    summary_sheet.write(summary_row, 0, 품목명)
                    summary_sheet.write(summary_row, 1, 수량)
                    summary_sheet.write(summary_row, 2, 단위)
                    summary_sheet.write(summary_row, 3, 총계)
                    summary_row += 1

            summary_row += 1  # 태그 간격

        # 총정리 시트에도 테두리와 열 너비 자동 조정 적용
        max_item_len = max([len(품목명) for 태그 in 태그_순서 for 품목명, _, _, _ in 전체_데이터[태그]] + [20])  # 가장 긴 품목명 길이 계산
        summary_sheet.set_column('A:A', max_item_len)
        summary_sheet.set_column('B:B', max([len(str(수량)) for 태그 in 태그_순서 for _, 수량, _, _ in 전체_데이터[태그]] + [20]))
        summary_sheet.set_column('C:C', max([len(단위) for 태그 in 태그_순서 for _, _, 단위, _ in 전체_데이터[태그]] + [15]))

        summary_sheet.conditional_format(f'A2:D{summary_row}', {'type': 'no_blanks', 'format': border_format})



# 엑셀 파일 경로
file_paths = [
    #'./2.19장부_1컴.xlsm',
    #'./2.19장부_2컴.xlsm',
    './2.19야채_코스_분류_총정리.xlsx',
    #'./통합 문서1.xlsx',
]

#file_paths = ['./2차.xlsx',]



def total_excecuter(file_paths, out_path):
    teams = [['동일','영현','인갑', '광일','광일2차', '정현','진우', '태경', '승민','정훈','유성,봉명','석훈','원근','김범','도룡마을','중상']]
    exclude_sheets = ['단가기입', '전날단가','공산']

    result = extract_a_column_data(file_paths, exclude_sheets)

    result = extract_item_details(result)

    unified_data = result

    result = team_grouping(result, teams)

    classified_data = classify_and_aggregate(result)

    out_path_order = f'{out_path}/{datetime.today().month}.{datetime.today().day}주문넣어주세요.xlsx'
    save_to_excel(classified_data, out_path_order)

    out_path_porti = f'{out_path}/{datetime.today().month}.{datetime.today().day}소분총정리.xlsx'
    save_sorted_products(unified_data, out_path_porti)

total_excecuter(file_paths, './')
# 결과 출력 (필요 시 주석 해제)
#print(data_dict)


