from external_buy_list import *

name_correction = {

'머위' : '머위나물',
'방풍' : '방풍나물',
'브로컬리' : '브로콜리',
'느타리특' : 'A느타리',
'봉지깻잎' : '깻잎',
'알베기' : '알배기',
'알베기상' : '알배기상',
'알베기일반' : '알배기',
'알베기특' : '알배기특',
'알비트' : '비트',
'영양' : '영양부추',
'특청경채' : '청경채특',
'큰순' : '깻순큰순',
'새송이400그램' : '400새송이',
'B표고' : 'B표고버섯',
'B급표고버섯' : 'B표고버섯',
'B급표고' : 'B표고버섯',
'A표고' : 'A표고버섯',
'표고' : '표고버섯',
'엄지' : '엄지새송이',
'칼밥' : '칼밥새송이',
'콩알' : '콩알새송이',
'총알' : '콩알새송이',
'팽이' : '팽이버섯',
'팽이상' : '팽이버섯상',
'화고버섯' : '화고표고',
'특새송이' : '새송이특',
'3키로도토리묵' : '3kg도토리묵',
'3키로청포묵' : '3kg청포묵',
'가오두부3키로' : '3kg가오두부',
'3키로가오두부' : '3kg가오두부',
'꽈리' : '꽈리고추',
'꽈리상' : '꽈리고추상',
'노란파프리카' : '노파프리카',
'노랑파프리카' : '노파프리카',
'노파' : '노파프리카',
'도토리묵3키로' : '3kg도토리묵',
'5키로도토리묵' : '5kg도토리묵',
'수성찜콩' : '수성찜콩나물',
'찜콩' : '찜콩나물',
'숙주' : '숙주나물',
'청양' : '청양고추',
'피망' : '청피망',
'홍파' : '홍파프리카',
'국산햇양파' : '국산양파',
'수입햇양파' : '수입양파',
'찜고구마' : '찜용고구마',
'고구마찜' : '찜용고구마',
'튀김고구마' : '튀김용고구마',
'검정배추' : '배추검정끈',
'배추검정' : '배추검정끈',
'1.8두부' : '1.8kg초방두부',
'1.8kg두부' : '1.8kg초방두부',
'1.8가오두부' : '1.8kg가오두부',
'1.8키로가오두부' : '1.8kg가오두부',
'찹찹이깻잎' : '찹찹이',
'주키니' : '쥬키니',
'상추순' : '쫑상추',
'홍청양' : '홍청양고추',
'냉동간마늘' : '천우 냉동다진마늘',
'냉동 간마늘' : '천우 냉동다진마늘',
'천우 냉동간마늘' : '천우 냉동다진마늘',
'무우순' : '무순',
'청풍쌀20kg' : '청풍쌀',
'청풍명월쌀' : '청풍쌀',
'청풍명월쌀20kg' : '청풍쌀',
'특느타리' : 'A느타리',
'느타리A' : 'A느타리',
'부추B' : 'B부추',
'가오맛두부' : '가오 맛두부',
'가화청국장' : '가화 청국장',
'만가닥' : '갈색만가닥',
'갈색만가닥버섯' : '갈색만가닥',
'흰색만가닥버섯' : '흰색만가닥',
'고추잎' : '고춧잎',
'국내산50% 세우리김치' : '국내산50% 세우리김치',
'국내산50%세우리김치' : '국내산50% 세우리김치',
'국산바지락' : '국산 바지락',
'국내산바지락' : '국산 바지락',
'국내산 바지락' : '국산 바지락',
'수입 바지락' : '중국산 바지락',
'수입바지락' : '중국산 바지락',
'중국바지락' : '중국산 바지락',
'중국 바지락' : '중국산 바지락',
'중국산바지락5kg' : '중국산 바지락(5kg)',
'국산100% 세우리김치' : '국산100% 세우리김치',
'국산100%세우리김치' : '국산100% 세우리김치',
'궁채' : '뚱채',
'냉동고등어' : '냉동 고등어',
'냉동굴' : '냉동 굴',
'냉동배추시래기' : '냉동 배추시래기',
'냉동무청시래기' : '냉동 무청시래기',
'브라질닭정육' : '냉동 브라질닭정육',
'브라질 닭정육' : '냉동 브라질닭정육',
'냉동우렁이' : '냉동 우렁이',
'냉동쭈꾸미' : '냉동 쭈꾸미',
'냉동청양슬라이스' : '냉동 청양슬라이스',
'노바시' : '노바시새우',
'롯데미림' : '롯데 미림',
'멜론' : '메론',
'백목이' : '백목이버섯',
'목이' : '건목이버섯',
'한잎목이' : '한잎목이버섯',
'햇살슬라이스단무지' : '햇살 슬라이스단무지',
'햇살반달단무지' : '햇살 반달단무지',
'하나깍둑단무지' : '하나 깍둑단무지',
'부자농산기피들깨가루' : '부자농산 기피들깨가루',
'부자농산깨소금' : '부자농산 깨소금',
'부자농산들깨가루' : '부자농산 들깨가루',
'부자농산볶음참깨' : '부자농산 볶음참깨',
'부자농산기피들깨가루1kg' : '부자농산 기피들깨가루',
'부자농산깨소금1kg' : '부자농산 깨소금',
'부자농산들깨가루1kg' : '부자농산 들깨가루',
'부자농산볶음참깨1kg' : '부자농산 볶음참깨',
'비름' : '비름나물',
'새송이파지' : '파지새송이',
'샤인머스켓' : '샤인머스캣',
'신부산 사각오뎅': '신부산 사각어묵',
'신부산오뎅' : '신부산 사각어묵',
'신부산어묵' : '신부산 사각어묵',
'신선애맛김치' : '신선애 맛김치',
'아삭이고추' : '아삭이',
'아삭이고추상' : '아삭이상',
'아삭이고추특' : '아삭이특',
'알타리무' : '알타리',
'양념깻잎지4키로' : '양념깻잎지(4kg)',
'양념깻잎지4kg' : '양념깻잎지(4kg)',
'에코팽이' : '에코팽이버섯',
'절단꽃게2L' : '절단꽃게(2L)',
'절단꽃게L' : '절단꽃게(L)',
'절단꽃게3L' : '절단꽃게(3L)',
'절단꽃게S' : '절단꽃게(S)',
'정갓김치' : '정 갓김치',
'정김치' : '정 김치',
'정맛김치' : '정 맛김치',
'정백김치' : '정 백김치',
'정슬라이스김치' : '정 슬라이스김치',
'정쪽파김치' : '정 쪽파김치',
'쥬키니호박' : '쥬키니',
'주키니호박' : '쥬키니',
'토마토1호' : '토마토(1호)',
'토마토2호' : '토마토(2호)',
'통로매인' : '통로메인',
'쥬스용케일' : '케일(쥬스용)',
'꺳잎' : '깻잎',
'단미나리' : '미나리',
'무' : '무우',
'쌈배추' : '알배기',
'깻잎순' : '깻순',
'농민떡볶이떡2.5kg' : '농민 떡볶이떡(2.5kg)',
'세척당근' : '당근',
'세척 당근' : '당근',
'한밭숙주' : '숙주나물',
'한밭숙주(5000)' : '숙주나물',
'콩나물(4000)' : '콩나물',
'숙주나물(5000)' : '숙주나물',
'숙주(5000)' : '숙주나물',
'깐배추' : '깐배추',
'깐양배추' : '깐양배추',
'A배추' : '배추',
'생매추리알' : '생메추리알',
'염장곰피벌크' : '염장곰피(10kg,벌크)',
'시골집 청국장' : '시골집 청국장(1kg)',
'마나리' : '미나리',
'간쪽파' : '깐쪽파',
'거지' : '가지',
'간실파' : '깐실파',
'켐벨포도' :'캠벨포도',
'켐밸포도' :'캠벨포도',
'캠벨포도' :'캠벨포도',
'깐양파B' : 'B깐양파',
'양배추2번' : '양배추(2번)',
'2번양배추' : '양배추(2번)',
'팽이벗서' : '팽이버섯',
'흙생강' : '국산생강',
'깐족파' : '깐쪽파',
'소만르' : '소마늘',
'흙족파' : '흙쪽파',
'반석두푸' : '반석두부'
}

brakets_correction = {
    '배추(중상가)' : '배추',
    '배추(중상가격)' : '배추',
    '깐양파(중상가)' : '깐양파',
    '깐양파(중상가격)' : '깐양파',
    '깐양배추(큰거)' : '깐양배추',
    '깐배추(큰거)' : '깐배추',
}

unit_correction = {
    'k':'키로',
    'kg':'키로',
    'b':'박스',
    'box':'박스',
    'g':'그램',
    'ea':'개',
    '봉지':'봉',
}

unit_quan_correction = {

    '100그램' : '0.1키로',
    '200그램' : '0.2키로',
    '300그램' : '0.3키로',
    '400그램' : '0.4키로',
    '500그램' : '0.5키로',
    '600그램' : '0.6키로',
    '700그램' : '0.7키로',
    '800그램' : '0.8키로',
    '900그램' : '0.9키로', 
    '1근' : '0.5키로',

}

# 특정 품목명의 단위를 통일
name_unit_matching = {
    '관대파' : {
        '단' : '관',
    },
    '850두부' : {
        '팩' : '모',
        '개' : '모',
    },
    '3kg도토리묵' : {
        '판' : '팩',
    },
    '5kg도토리묵' : {
        '팩' : '판'
    },
    '자숙연근채' : {
        '봉' : '팩',
        '키로' : '팩',
    },
    '염장연근채' : {
        '봉' : '팩',
    },
    '자숙고사리' : {
        '봉' : '팩',
        '키로' : '팩',
    },
    '고사리' : {
        '봉' : '팩',
        '키로' : '팩',
    },
    '시골집 청국장(1kg)' : {
        '개' : '팩',
    },
    '400새송이' : {
        '개' : '팩',
        '봉' : '팩',
    },
    '연두부' : {
        '개' : '팩',
    },
    '청풍쌀' : {
        '포대' : '포',
    },
    '이장쌀' : {
        '포대' : '포',
    },
    '반석두부' : {
        '판' : '팩',
    },
    '단호박' : {
        '개' : '통',
    },
    '무우' : {
        '개' : '통',
    },

}

# 단위가 개일 경우 변경
gae_unit_matching = {
    '통' : ['라디치오', '양배추', '배추', '적채', '알배기', '비트', '알비트', '양상추', '무우'],
    '봉' : ['팽이버섯', '깻잎'],
    '모' : ['850두부'],
    '팩' : ['무순', '400새송이'],
}

# 합산에서 제외할 품목명과 단위
no_add_product_by_unit = {
    '콩나물' : '키로',
    '숙주나물' : '키로',
    'A간마늘' : '키로',
    'B간마늘' : '키로',
    '간생강' : '키로',
    '깐마늘꼭지제거' : '키로',
    '깐생강' : '키로',
    '소마늘' : '키로',
    '중마늘' : '키로',
    '850두부' : '모',
    '풋고추' : '키로',
    '홍청양고추' : '키로',
    '깐대파' : '키로',
    'A느타리' : '박스',
    '연두부' : '팩',
    '장마' : '키로',
}

portion_rule315 = {
    '라디치오': {
        '박스': '22번(엽채류)_박스',
        '개': '22번(엽채류)_소분',
        '통': '22번(엽채류)_소분',
    },
    '마늘쫑': {
        '박스': '22번(엽채류)_박스',
        '단': '22번(엽채류)_소분',
        '키로': '22번(엽채류)_소분',
    },
    '샐러리': {
        '박스': '22번(엽채류)_박스',
        '단': '22번(엽채류)_소분',
        '그램': '22번(엽채류)_소분',
        '키로': '22번(엽채류)_소분',
    },
    '얼갈이': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
        '단' : '127번(깐쪽파)',
    },
    '열무': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
        '단' : '127번(깐쪽파)',
    },
    '케일': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '적근대': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '적상추': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '통로메인': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '꽃상추': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '근대': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '청경채': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '브로콜리': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
        '개': '22번(엽채류)_소분',
    },
    '아욱': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '청상추': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '고춧잎': {
        '박스': '22번(엽채류)_박스',
    },
    '시금치': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
        '단': '22번(엽채류)_소분',
    },
    '미나리': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
        '단': '22번(엽채류)_소분',
    },
    'B미나리': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '비타민': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '참나물': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '깻잎': {
        '박스': '22번(엽채류)_박스',
        '봉': '22번(엽채류)_소분',
        '키로': '22번(엽채류)_소분',
    },
    '깻순': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '쑥갓': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '청경채특': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '청경채상': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '치커리': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '방풍': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '방풍나물': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '특청경채': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '취나물': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '비름나물': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '적채': {
        '개': '22번(엽채류)_소분',
        '통': '22번(엽채류)_소분',
        '키로': '22번(엽채류)_소분',
    },
    '양상추': {
        '개': '22번(엽채류)_소분',
        '통': '22번(엽채류)_소분',
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '수입양상추': {
        '개': '22번(엽채류)_소분',
        '통': '22번(엽채류)_소분',
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '알비트': {
        '박스': '22번(엽채류)_박스',
        '통' : '22번(엽채류)_박스',
        '개' : '22번(엽채류)_박스',
    },
    '비트': {
        '박스': '22번(엽채류)_박스',
        '통' : '22번(엽채류)_박스',
        '개' : '22번(엽채류)_박스',
    },
    '청겨자': {
        '박스': '22번(엽채류)_박스',
    },
    '적치커리': {
        '박스': '22번(엽채류)_박스',
    },
    '로즈': {
        '박스': '22번(엽채류)_박스',
    },
    '쫑상추': {
        '박스': '22번(엽채류)_박스',
    },
    '당귀': {
        '박스': '22번(엽채류)_박스',
    },
    '봉지깻잎': {
        '박스': '22번(엽채류)_박스',
    },
    '쌈추': {
        '박스': '22번(엽채류)_박스',
    },
    '깻순큰순': {
        '박스': '22번(엽채류)_박스',
    },
    '큰순': {
        '박스': '22번(엽채류)_박스',
    },
    '찹찹이': {
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '알베기일반': {
        '박스': '22번(엽채류)_박스',
    },
    '머위나물': {
        '박스': '22번(엽채류)_박스',
    },
    '머위': {
        '박스': '22번(엽채류)_박스',
    },
    '알배기특': {
        '박스': '22번(엽채류)_박스',
    },
    '알배기상': {
        '박스': '22번(엽채류)_박스',
    },
    '알배기': {
        '통': '22번(엽채류)_소분',
        '개': '22번(엽채류)_소분',
        '박스': '22번(엽채류)_박스',
        '키로': '22번(엽채류)_소분',
    },
    '고수': {
        '단': '22번(엽채류)_소분',
    },
    '적겨자': {
        '키로': '22번(엽채류)_소분',
        '박스': '22번(엽채류)_박스',
    },
    '파슬리': {
        '키로': '22번(엽채류)_소분',
    },
    '무순': {
        '팩': '22번(엽채류)_소분',
    },
    '어린잎대': {
        '팩': '22번(엽채류)_소분',
    },
    '어린잎소': {
        '팩': '22번(엽채류)_소분',
    },
    '새싹대': {
        '팩': '22번(엽채류)_소분',
    },
    '새싹소': {
        '팩': '22번(엽채류)_소분',
    },
    '무순대': {
        '팩': '22번(엽채류)_소분',
    },
    '엽순': {
        '키로': '22번(엽채류)_소분',
    },
    '모현청경채': {
        '키로': '22번(엽채류)_소분',
    },
    '깐양상추': {
        '키로': '22번(엽채류)_소분',
    },
    '영양부추': {
        '단': '22번(엽채류)_소분',
    },
    '영양': {
        '단': '22번(엽채류)_소분',
    },
    '로메인': {
        '키로': '22번(엽채류)_소분',
    },
}

portion_rule209 = {
    '새송이': {
        '봉': '209번(버섯류)_박스',
        '키로': '209번(버섯류)_소분',
    },
    '느타리': {
        '박스': '209번(버섯류)_박스',
        '키로': '209번(버섯류)_소분',
    },
    '느타리상': {
        '박스': '209번(버섯류)_박스',
    },
    '새송이버섯': {
        '봉': '209번(버섯류)_박스',
        '키로': '209번(버섯류)_소분',
    },
    '양송이': {
        '박스': '209번(버섯류)_박스',
        '키로': '209번(버섯류)_소분',
    },
    'B양송이': {
        '박스': '209번(버섯류)_박스',
        '키로': '209번(버섯류)_소분',
    },
    'A양송이': {
        '박스': '209번(버섯류)_박스',
        '키로': '209번(버섯류)_소분',
    },
    'B표고버섯': {
        '박스': '209번(버섯류)_박스',
        '키로': '209번(버섯류)_소분',
    },
    '맛타리': {
        '박스': '209번(버섯류)_박스',
        '팩': '209번(버섯류)_소분',
    },
    '흑타리': {
        '박스': '209번(버섯류)_박스',
        '팩': '209번(버섯류)_소분',
    },
    '팽이': {
        '박스': '209번(버섯류)_박스',
        '개': '209번(버섯류)_박스',
        '봉': '209번(버섯류)_박스',
        '키로': '209번(버섯류)_박스',
    },
    '팽이버섯': {
        '박스': '209번(버섯류)_박스',
        '개': '209번(버섯류)_박스',
        '봉': '209번(버섯류)_박스',
        '키로': '209번(버섯류)_박스',
    },
    '팽이버섯상': {
        '박스': '209번(버섯류)_박스',
    },
    '병팽이': {
        '박스': '209번(버섯류)_박스',
    },
    '에코팽이버섯': {
        '박스': '209번(버섯류)_박스',
    },
    '갈색만가닥': {
        '박스': '209번(버섯류)_박스',
        '팩': '209번(버섯류)_소분',
    },
    '흰색만가닥': {
        '박스': '209번(버섯류)_박스',
        '팩': '209번(버섯류)_소분',
    },
    '만가닥벌크': {
        '박스': '209번(버섯류)_박스',
    },
    '느타리특': {
        '박스': '209번(버섯류)_박스',
        '키로': '209번(버섯류)_소분',
    },
    'A느타리': {
        '박스': '209번(버섯류)_박스',
        '키로': '209번(버섯류)_소분',
    },
    '표고버섯': {
        '키로': '209번(버섯류)_소분',
    },
    'A표고버섯': {
        '키로': '209번(버섯류)_소분',
    },
    '콩알': {
        '봉': '209번(버섯류)_소분',
        '키로': '209번(버섯류)_소분',
    },
    '엄지': {
        '봉': '209번(버섯류)_소분',
        '키로': '209번(버섯류)_소분',
    },
    'B표고': {
        '키로': '209번(버섯류)_소분',
    },
    '콩알새송이': {
        '봉': '209번(버섯류)_소분',
        '키로': '209번(버섯류)_소분',
    },
    '화고표고': {
        '키로': '209번(버섯류)_소분',
    },
    '특새송이': {
        '봉': '209번(버섯류)_소분',
    },
    '새송이특': {
        '봉': '209번(버섯류)_소분',
    },
    '새송이상': {
        '봉': '209번(버섯류)_소분',
    },
    '칼밥새송이': {
        '봉': '209번(버섯류)_소분',
        '키로': '209번(버섯류)_소분',
    },
    '엄지새송이': {
        '봉': '209번(버섯류)_소분',
        '키로': '209번(버섯류)_소분',
    },
    '파지새송이': {
        '박스': '209번(버섯류)_소분',
        '키로': '209번(버섯류)_소분',
        '봉': '209번(버섯류)_소분',
    },
    '화고버섯': {
        '키로': '209번(버섯류)_소분',
    },
    '400새송이': {
        '팩': '209번(버섯류)_소분',
        '박스': '209번(버섯류)_박스',
        '봉': '209번(버섯류)_소분',
    },
    '새송이400그램': {
        '박스': '209번(버섯류)_소분',
    },
}



food_em = [
    '푸드이엠 도삭면',
    '푸드이엠 샤오롱바오',
    '푸드이엠 중화면',
    '푸드이엠 고기만두소',
    '푸드이엠 김치만두소',
    '푸드이엠 멘보샤',
    '푸드이엠 냉면',
    '홍피망',
    '푸드이엠 하가우',
    '푸드이엠 F',
    '푸드이엠 G',
    '푸드이엠 H',
    '푸드이엠 건궁채',
    '푸드이엠 고춧가루(굵은)',
    '푸드이엠 고춧가루(김치용)',
    '푸드이엠 고춧가루(장용)',
    '푸드이엠 고춧가루(짬뽕용)',
    '푸드이엠 고춧가루(청양,장용)',
    '푸드이엠 고춧가루(청양고운)',
    '푸드이엠 굵은고춧가루',
    '푸드이엠 단무지',

]



classification_rule = {
    '22번(엽채류)' : ['쫑상추','알배기상','통로메인', '영양부추','쌈추', '청경채상','수입양상추','고춧잎', '깻순',	'아욱',	'얼갈이',	'치커리',	'B미나리','미나리',	'브로콜리',	'청경채',	'당귀','고수',	'라디치오',	'청상추',	'시금치',	'적겨자',	'근대',	'참나물',	'꽃상추',	'파슬리',	'비타민',	'적상추',	'쑥갓',	'케일',	'적근대',	'마늘쫑',	'무순',	'어린잎대',	'어린잎소',	'새싹대',	'새싹소',	'무순대', '열무',	'샐러리',	'엽순',	'깻잎',	'모현청경채',	'방풍',	'방풍나물',	'깐양상추',	'특청경채',	'청경채특',	'영양',	'로메인',	'취나물',	'로즈',	'비름나물',	'알베기',	'알베기특',	'알베기상',	'적채',	'양상추', '비트',	'알비트',	'청겨자',	'적치커리',	'봉지깻잎',	'깻순큰순',	'큰순',	'찹찹이',	'알베기일반',	'머위나물',	'머위',	'알배기특',	'알배기'],
    '209번(버섯류)' : ['흑타리','A느타리','팽이버섯상','새송이상','파지새송이', '만가닥벌크','느타리상','맛타리',	'새송이',	'팽이',	'느타리',	'에코팽이버섯','팽이버섯',	'병팽이',	'갈색만가닥',	'느타리특',	'화고표고',	'새송이버섯',	'양송이',	'B양송이',	'A양송이',	'B표고버섯',	'표고버섯',	'A표고버섯',	'콩알',	'엄지',	'B표고',	'콩알새송이',	'특새송이',	'새송이특',	'칼밥새송이',	'엄지새송이',	'화고버섯',	'갈색만가닥',	'흰색만가닥','400새송이',	'새송이400그램'],
    '240번(숙주,나물)' :	['시골집 청국장(1kg)', '3kg가오두부', '한밭콩나물','크린콩나물', '청포묵소','청포묵', '두절콩나물','뚱채', '3kg청포묵','5kg도토리묵',  '3kg도토리묵','순두부',	'콩나물',	'숙주',	'채도라지',	'도토리묵3키로',	'연두부',		'850두부',	'장마','마','시래기',	'건뚱채',	'가오두부3키로',	'찜콩나물',	'청국장소',	'건취나물',	'건무말랭이',	'삼채',	'3키로도토리묵',	'3키로청포묵',	'수성숙주',	'통연근',	'자숙시래기',	'무말랭이',	'숙주나물',	'토박이숙주','수성콩나물',	'토박이콩나물',	'매일콩나물',	'수성찜콩'	],																		
    '165번(고추,피망)' :	['라임','아삭이상', '아삭이특','청양고추상', '꽈리고추상','홍청양고추', '꽈리고추',	'꽈리',	'청양고추',	'청양',	'아삭이', '청피망특', '청피망상',	'홍고추',	'청피망',	'피망',	'홍파프리카',	'홍파',	'노파프리카',	'노파',	'노란파프리카',	'풋고추'	],																																	
    '33번(가지,오이)' :	['국산단호박','가시오이', '가지',	'오이',	'호박',	'쥬키니특', '쥬키니상', '쥬키니',	'노각',	'청오이',	'애호박상',	'청오이특',	'백오이상','백오이',	'청오이상',	'단호박',	'애호박특',	'애호박',	'가지상',	'백오이특',	'가지특',	'풋호박'	],																														
    '특수야채' :	['타임', '루꼴라','와일드루꼴라', '애플민트', '차이브',	'시소',	'쏘렐',	'딜',	'식용꽃',	'국화',	'노무라',	'레디쉬',	'민트',	'로즈마리',	'바질',		'이태리파슬리'	],																																		
    '127번(깐쪽파)' :	['초롱무','흙쪽파소','깐실파','실파', '쪽파',	'깐쪽파',	'알타리',	'깐쪽파소',	'단얼갈이',	'단열무',	'흙쪽파'	],																																								
    '과일' :	['체리','청포도', '캠벨포도', '토종토마토', '자두','아오리사과', '참외','스테비아방울', '샤인머스캣','블루베리', '부사사과', '반숙토마토', '메론', '홍자몽', '거봉', '수박','방울토마토',	'토마토',	'사과',	'배',	'오렌지',	'대추방울토마토','복숭아', '백도복숭아', '천도복숭아',	'파인애플',	'키위',	'골드키위',	'그린키위',	'아보카도',	'레드자몽','자몽',	'바나나',	'완숙토마토', '완숙토마토1호',	'귤',	'팩방울토마토',	'포도',	'제수용',	'사과제수용',	'1호방울토마토',	'2호방울토마토',	'3호방울토마토',	'4호방울토마토',	'5호방울토마토',	'1호토마토',	'2호토마토',	'3호토마토',	'4호토마토',	'5호토마토'	],																		
    '부추' :	['부추',	'부추소', 'B부추'	],																																													
    '가게' :	['A간마늘',	'B간마늘',	'깐마늘꼭지제거', '깐생강','소마늘',	'간생강',	'중마늘'	],																																			
    '계란' :	['대란',	'중란',	'특란',	'왕란', '생메추리알'	],		
    '314번' : ['염장곰피(10kg,벌크)', '꼬시래기', '우엉채',  '쌈다시마']		,																																							
    '사입' :	external_buy,
    '푸드이엠' :	food_em,
    '현황보고' : ['양배추4구','깐대파','관대파', '무',	'배추',	'양배추', '무우','무12과','배추검정끈', '배추파란끈','대파','양파3키로','깐양파','깐양파',	'BC깐양파','깐양배추',	'B깐양파',	'A깐양파','양파대',	'양파중',	'양파소',],																					
    '상관없는거' :	['국산생강',	'고구마','수입생강', '당근','세척당근',	'국산햇양파',	'대마늘','국산양파','수입양파','양파',		'감자',	'고구마왕',	'고구마찜',		'알감자',	'감자10키로',		'레몬',		'반석두부',	'반석순두부',	'자숙연근',	'염장연근',	'고사리',	'쌀',	'이장쌀',	'청풍명월',	'자숙연근채',	'염장연근채',	'적양파',	'청풍쌀',	'흙당근',	'감자왕특',	'감자왕왕',	'자숙고사리',	'깐메추리알',		'찜고구마',	'수입햇양파'	]
}


total_portion_rule = {
    '165번(고추,피망)' : [
        {'품목': '꽈리고추', '단위': '키로'},
        {'품목': '노파프리카', '단위': '키로'},
        {'품목': '노파프리카', '단위': '개'},
        {'품목': '아삭이', '단위': '키로'},
        {'품목': '아삭이', '단위': '개'},
        {'품목': '청양고추', '단위': '키로'},
        {'품목': '청피망', '단위': '키로'},
        {'품목': '청피망', '단위': '개'},
        {'품목': '홍고추', '단위': '키로'},
        {'품목': '홍파프리카', '단위': '키로'},
        {'품목': '홍파프리카', '단위': '개'},
        {'품목': '홍피망', '단위': '키로'},
        {'품목': '홍피망', '단위': '개'},
        {'품목': '꽈리고추', '단위': '봉'},
        {'품목': '노파프리카', '단위': '봉'},
        {'품목': '아삭이', '단위': '봉'},
        {'품목': '청양고추', '단위': '봉'},
        {'품목': '청피망', '단위': '봉'},
        {'품목': '홍고추', '단위': '봉'},
        {'품목': '홍파프리카', '단위': '봉'},
        {'품목': '홍피망', '단위': '봉'},
    ],
    '33번(오이,호박,가지)' : [
        {'품목': '가지', '단위': '키로'},
        {'품목': '가지', '단위': '개'},
        {'품목': '단호박', '단위': '키로'},
        {'품목': '단호박', '단위': '개'},
        {'품목': '백오이', '단위': '키로'},
        {'품목': '백오이', '단위': '개'},
        {'품목': '애호박', '단위': '키로'},
        {'품목': '애호박', '단위': '개'},
        {'품목': '쥬키니', '단위': '키로'},
        {'품목': '쥬키니', '단위': '개'},
        {'품목': '청오이', '단위': '키로'},
        {'품목': '청오이', '단위': '개'},
        {'품목': '가지', '단위': '봉'},
        {'품목': '단호박', '단위': '봉'},
        {'품목': '백오이', '단위': '봉'},
        {'품목': '애호박', '단위': '봉'},
        {'품목': '쥬키니', '단위': '봉'},
        {'품목': '청오이', '단위': '봉'},
    ],
    '자체상품' : [
        {'품목': '당근', '단위': '키로'},
        {'품목': '당근', '단위': '개'},
        {'품목': '레몬', '단위': '키로'},
        {'품목': '레몬', '단위': '개'},
        {'품목': '오렌지', '단위': '키로'},
        {'품목': '오렌지', '단위': '개'},
        {'품목': '수입생강', '단위': '키로'},
        {'품목': '국산생강', '단위': '키로'},
        {'품목': '대마늘', '단위': '키로'},
        {'품목': '감자', '단위': '키로'},
        {'품목': '감자', '단위': '개'},
        {'품목': '고구마', '단위': '키로'},
        {'품목': '고구마', '단위': '개'},
        {'품목': '고구마왕', '단위': '키로'},
        {'품목': '고구마왕', '단위': '개'},
        {'품목': '찜고구마', '단위': '키로'},
        {'품목': '찜고구마', '단위': '개'},
        {'품목': '비트', '단위': '키로'},
        {'품목': '비트', '단위': '개'},
        {'품목': '염장연근채', '단위': '팩'},
        {'품목': '자숙연근채', '단위': '팩'},
        {'품목': '데친연근채', '단위': '팩'},
        {'품목': '자숙시래기', '단위': '팩'},
        {'품목': '시래기', '단위': '팩'},
        {'품목': '깐메추리알', '단위': '봉'},
        {'품목': '자숙고사리', '단위': '팩'},
        {'품목': '자숙고사리', '단위': '봉'},
        {'품목': '자숙고사리', '단위': '키로'},
        {'품목': '고사리', '단위': '팩'},
        {'품목': '고사리', '단위': '봉'},
        {'품목': '고사리', '단위': '키로'},
        {'품목': '팽이버섯', '단위': '봉'},
        {'품목': '팽이버섯', '단위': '키로'},
        {'품목': '적채', '단위': '키로'},
        {'품목': '적채', '단위': '개'},
        {'품목': '적채', '단위': '통'},
        {'품목': '비트', '단위': '통'},
        {'품목': '비트', '단위': '개'},
        {'품목': '단호박', '단위': '통'},
        {'품목': '단호박', '단위': '개'},
        {'품목': '반석두부', '단위': '팩'},
        {'품목': '수미감자', '단위': '키로'},
        {'품목': '감자왕왕', '단위': '키로'},
        {'품목': '대파', '단위': '봉'},
        {'품목': '당근', '단위': '봉'},
        {'품목': '레몬', '단위': '봉'},
        {'품목': '오렌지', '단위': '봉'},
        {'품목': '수입생강', '단위': '봉'},
        {'품목': '국산생강', '단위': '봉'},
        {'품목': '대마늘', '단위': '봉'},
        {'품목': '감자', '단위': '봉'},
        {'품목': '고구마', '단위': '봉'},
        {'품목': '고구마왕', '단위': '봉'},
        {'품목': '찜고구마', '단위': '봉'},
        {'품목': '적채', '단위': '봉'},
        {'품목': '비트', '단위': '봉'},
        {'품목': '단호박', '단위': '봉'},
        {'품목': '감자왕왕', '단위': '봉'},
        {'품목': '1.8kg초방두부', '단위': '팩'},
        {'품목': '흙당근', '단위': '키로'},
        {'품목': '순두부', '단위': '개'},
        {'품목': '순두부', '단위': '봉'},
        {'품목': '순두부', '단위': '팩'},
        {'품목': '풋고추', '단위': '키로'},
        {'품목': '연두부', '단위': '팩'},
        {'품목': '연두부', '단위': '개'},
        {'품목': '깐양상추', '단위': '키로'},
        {'품목': '자숙연근채', '단위': '키로'},
        {'품목': '자숙연근채', '단위': '팩'},
        {'품목': '자숙무청시래기', '단위': '팩'},
        {'품목': '자숙무청시래기', '단위': '키로'},
        {'품목': '숙주나물', '단위': '키로'},
        {'품목': '콩나물', '단위': '키로'},
        {'품목': '라임', '단위': '키로'},
        {'품목': '라임', '단위': '개'},
        {'품목': '자숙토란대', '단위': '팩'},
        {'품목': '방울토마토', '단위': '키로'},
        {'품목': '방울토마토(1호)', '단위': '키로'},
        {'품목': '깐쪽파', '단위': '키로'},
        {'품목': '깐쪽파', '단위': '단'},
        {'품목': '흙쪽파', '단위': '키로'},
        {'품목': '흙쪽파', '단위': '단'},
        {'품목': '쪽파', '단위': '단'},
        {'품목': '쪽파', '단위': '키로'},
        {'품목': '깐쪽파소', '단위': '단'},
        {'품목': '흙쪽파소', '단위': '단'},
        {'품목': '쪽파소', '단위': '단'},
    ],
    '엽채류' : [
        {'품목': '고수', '단위': '단'},
        {'품목': '라디치오', '단위': '통'},
        {'품목': '마늘쫑', '단위': '단'},
        {'품목': '마늘쫑', '단위': '키로'},
        {'품목': '무순', '단위': '팩'},
        {'품목': '미나리', '단위': '키로'},
        {'품목': '미나리', '단위': '단'},
        {'품목': '비타민', '단위': '키로'},
        {'품목': '새싹대', '단위': '팩'},
        {'품목': '새싹소', '단위': '팩'},
        {'품목': '쑥갓', '단위': '키로'},
        {'품목': '어린잎대', '단위': '팩'},
        {'품목': '어린잎소', '단위': '팩'},
        {'품목': '얼갈이', '단위': '키로'},
        {'품목': '양상추', '단위': '개'},
        {'품목': '양상추', '단위': '키로'},
        {'품목': '영양부추', '단위': '단'},
        {'품목': '영양부추', '단위': '키로'},
        {'품목': '적근대', '단위': '키로'},
        {'품목': '적상추', '단위': '키로'},
        {'품목': '참나물', '단위': '키로'},
        {'품목': '청경채', '단위': '키로'},
        {'품목': '청경채특', '단위': '키로'},
        {'품목': '청상추', '단위': '키로'},
        {'품목': '꽃상추', '단위': '키로'},
        {'품목': '치커리', '단위': '키로'},
        {'품목': '파슬리', '단위': '키로'},
        {'품목': '쫑상추', '단위': '키로'},
        {'품목': '깻잎', '단위': '봉'},
        {'품목': '깻잎', '단위': '키로'},
        {'품목': '시금치', '단위': '키로'},
        {'품목': '단시금치', '단위': '단'},
        {'품목': '열무', '단위': '키로'},
        {'품목': '깻순', '단위': '키로'},
        {'품목': '깻순큰순', '단위': '키로'},
        {'품목': '근대', '단위': '키로'},
        {'품목': '아욱', '단위': '키로'},
        {'품목': '알배기', '단위': '키로'},
        {'품목': '알배기', '단위': '통'},
        {'품목': '알배기', '단위': '개'},
        {'품목': '머위나물', '단위': '키로'},
        {'품목': '취나물', '단위': '키로'},
        {'품목': '비름나물', '단위': '키로'},
        {'품목': '고춧잎', '단위': '키로'},
        {'품목': '샐러리', '단위': '단'},
        {'품목': '샐러리', '단위': '키로'},
        {'품목': '케일', '단위': '키로'},
        {'품목': '적겨자', '단위': '키로'},
        {'품목': '적치커리', '단위': '키로'},
        {'품목': '통로메인', '단위': '키로'},
        {'품목': '로즈', '단위': '키로'},
        {'품목': '겨자', '단위': '키로'},
        {'품목': '뉴그린', '단위': '키로'},
        {'품목': '브로콜리', '단위': '키로'},
        {'품목': '브로콜리', '단위': '개'},
        {'품목': '양상추', '단위': '통'},
        {'품목': '고수', '단위': '봉'},
        {'품목': '라디치오', '단위': '봉'},
        {'품목': '마늘쫑', '단위': '봉'},
        {'품목': '미나리', '단위': '봉'},
        {'품목': '비타민', '단위': '봉'},
        {'품목': '쑥갓', '단위': '봉'},
        {'품목': '얼갈이', '단위': '봉'},
        {'품목': '양상추', '단위': '봉'},
        {'품목': '영양부추', '단위': '봉'},
        {'품목': '적근대', '단위': '봉'},
        {'품목': '적상추', '단위': '봉'},
        {'품목': '참나물', '단위': '봉'},
        {'품목': '청경채', '단위': '봉'},
        {'품목': '청상추', '단위': '봉'},
        {'품목': '꽃상추', '단위': '봉'},
        {'품목': '치커리', '단위': '봉'},
        {'품목': '파슬리', '단위': '봉'},
        {'품목': '쫑상추', '단위': '봉'},
        {'품목': '시금치', '단위': '봉'},
        {'품목': '열무', '단위': '봉'},
        {'품목': '깻순', '단위': '봉'},
        {'품목': '근대', '단위': '봉'},
        {'품목': '아욱', '단위': '봉'},
        {'품목': '알배기', '단위': '봉'},
        {'품목': '머위나물', '단위': '봉'},
        {'품목': '취나물', '단위': '봉'},
        {'품목': '비름나물', '단위': '봉'},
        {'품목': '고춧잎', '단위': '봉'},
        {'품목': '샐러리', '단위': '봉'},
        {'품목': '케일', '단위': '봉'},
        {'품목': '적겨자', '단위': '봉'},
        {'품목': '적치커리', '단위': '봉'},
        {'품목': '통로메인', '단위': '봉'},
        {'품목': '로즈', '단위': '봉'},
        {'품목': '겨자', '단위': '봉'},
        {'품목': '뉴그린', '단위': '봉'},
        {'품목': '브로콜리', '단위': '봉'},
        {'품목': '모현청경채', '단위': '키로'},
        {'품목': '엽순', '단위': '키로'},
        {'품목': '봄동', '단위': '키로'},
        {'품목': '세발나물', '단위': '키로'},
    ],
    '큰놈들' : [
        {'품목': '적양파', '단위': '키로'},
        {'품목': '국산양파', '단위': '망'},
        {'품목': '수입양파', '단위': '망'},
        {'품목': '양배추', '단위': '망'},
        {'품목': '배추', '단위': '망'},
        {'품목': '관대파', '단위': '관'},
        {'품목': '깐대파', '단위': '키로'},
        {'품목': '양배추(2번)', '단위': '망'},
        {'품목': '무우', '단위': '박스'},
        {'품목': '대란', '단위': '판'},
        {'품목': '대파', '단위': '키로'},
        {'품목': '대파', '단위': '단'},
        {'품목': '양배추', '단위': '봉'},
        {'품목': '배추', '단위': '봉'},
        {'품목': '깐양배추', '단위': '봉'},
        {'품목': '깐배추', '단위': '봉'},
        {'품목': '양배추', '단위': '키로'},
        {'품목': '양배추', '단위': '통'},
        {'품목': '배추', '단위': '키로'},
        {'품목': '배추', '단위': '통'},
        {'품목': '통배추', '단위': '키로'},
        {'품목': '통배추', '단위': '통'},
        {'품목': '배추검정끈', '단위': '망'},
        {'품목': '깐양배추', '단위': '키로'},
        {'품목': '깐양배추', '단위': '망'},
        {'품목': '깐양배추', '단위': '통'},
        {'품목': '깐배추', '단위': '키로'},
        {'품목': '깐배추', '단위': '망'},
        {'품목': '깐배추', '단위': '통'},
        {'품목': '청풍햅쌀(서산)', '단위': '포'},
        {'품목': '청풍햅쌀', '단위': '포'},
        {'품목': '이장햅쌀', '단위': '포'},
        {'품목': '청풍쌀', '단위': '포'},
        {'품목': '이장쌀', '단위': '포'},
        {'품목': '양파', '단위': '키로'},
        {'품목': '양파', '단위': '개'},
        {'품목': 'B깐양파', '단위': '키로'},
        {'품목': '깐양파', '단위': '키로'},
        {'품목': '깐양파', '단위': '개'},
        {'품목': '깐양파', '단위': '봉'},
        {'품목': '양파', '단위': '봉'},
        {'품목': '무우', '단위': '키로'},
        {'품목': '무우', '단위': '통'},
        {'품목': '무우', '단위': '봉'},
    ] 
}

sep_rule = {
    '청양고추' : '키로',
    '대파' : ['단','키로'],
    '청오이' : ['개','키로'],
    '대란' : '판',
    '양상추' : '통',
    '대마늘' : '키로',
    '팽이버섯' : '봉',
    '레몬' : '개',
    '무우' : '통',
    '깻잎' : '봉',
}

태그_순서 = ['165번(고추,피망)', '33번(오이,호박,가지)', '엽채류', '자체상품', '큰놈들', '박스모음', '나머지']