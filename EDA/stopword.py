### news eda 에 들어가는 STOP word를 모아놓은 파일   ###


donga_stoplist = ['부고','오늘의 채널A','오늘의 운세','사설','인사','알립니다','무비줌인','칼럼','포토 에세이','인사이드＆인사이트',
'게시판','바람개비','오늘의 경기','신문과 놀자!','우병탁의 절세통통(通)','양종구의 100세 시대 건강법','프리미엄뷰','머니 컨설팅',
'책의 향기','글로벌 포커스','우병탁의 절세통통','Food&Dining','DBR/Special Report','날씨 이야기','그림책 한조각','프리미엄뷰',
'edu+book','파워리더 인터뷰','알립니다','시사일본어학원','아파트 미리보기','Tech&','영남 파워기업','company&','특별기고','정도언의 마음의 지도',
'지표로 보는 경제','광화문에서','횡설수설','시론','안영식의 스포츠&','만화 그리는 의사들', '홍지윤 요리쌤의 오늘 뭐 먹지?','HBR','왕은철의 스토리와 치유',
'기고','직장인을 위한 김호의 생존의 방식','주성하 기자의 서울과 평양 사이','애널리스트의 마켓뷰','바둑','동아광장','Love&Gift','골든걸','화제의 분양현장',
'책속의 이 한줄','토요이슈','인물동정','토요기획','토요판 커버스토리','Money&Life','기업&CEO','짧은 소설','Economic Review','신나는 공부',
'Best of Best','이슈&뷰스','오늘과 내일','고미석의 詩로 여는 주말','Feeling','사이버대학','이 사람이 읽는 법','VISIT JAPAN!',
'톡투 건강 핫클릭','한국에서살아보니','아하! 질병이야기','뉴리더','e-코리아로 가는길','징검다리','방송','전시']

khan_stoplist = ['노래와 세상','NGO 발언대','황규관의 전환의 상상력','우리말 산책',
'詩想과 세상','케이블·위성 하이라이트','TV하이라이트','여적','COP27',
'신경과학 저널클럽','김용민의 그림마당','[숨]','김지연의 미술소환','[시선]',
'사유와 성찰','세상읽기','현장에서','내일 날씨','칼럼','책과 삶','기고',
'우당탕탕 귤엔터','박상희의 구해줘! 내 맘','이진송의 아니 근데','지극히 味적인 시장',
'이종산의 장르를 읽다','새책','오늘의 날씨','부고','홍경한의 예술산책-깊이 보다'
'김월회의 행로난','이굴기의 꽃산 꽃글','장도리','생각그림','경향포토',
'도재기의 천년향기','[직설]','신시 111년 건강의료 기획','청소년책','책과 삶',
'여적','박성진의 한국군 코멘터리','생각그림','경향사람들','이명학의 내 인생의 책',
'문명, 그 길을 묻다','오늘의 운세','사회공헌 특집','서민의 과학과 사회','여적',
'알림','이택광의 왜?','경향논단','스포츠 플러스','인사','어제의 오늘','게시판',
'시민 기자석','인물로 본 2008 정치','아침을 열며','오늘의 경기','돋보기','말속의 말',
'독자의 소리','문화플라자','지금, 여기']

chosun_stoplist = ['통판광고','전면광고','신춘문예', '당선작', '일사일언', '동정', '생활한자', '리빙 포인트', '리빙포인트', 
    'hot & cold', '기업공시', '부음','플라자','편집자에게','신문은 선생님','알림','사진', '시사', '교양', '확성기', '기고', 
    '의견', '이규태', '경제 브리핑', '날씨 이야기', '문화게시판', '쇼트트랙', '취재메모', '아이스하키', '만물상', '태평로', 
    '시네마', '문화나들이 어디로 할까', '방송가', '튼튼스타', '단신', '새의자', '시시각각', '스포츠', 'TEPS', '연극리뷰', 
    '클래식', '부부의 속마음', '병원 Q & A', '여행수첩', '여행단신', '그래픽 뉴스', '오태진', '내정', '사진기사', 
    '이곳이 좋아요', '알뜰정보', '학술 소식', '조용헌', '알립니다', '호남사람들', '인사;']

hani_stoplist = ['책&생각','육퇴한 밤','강재훈의 살핌','슬기로운 기자생활','김명인 칼럼','숨&결',
'나는 역사다','오금택의 100㎝','날씨','타인의 시선','권혁웅의 오목렌즈','전우용의 현대를 만든 물건들']

joongang_stoplist = ['사진설명','신년사','문장으로 읽는 책','건강한 가족','오늘의 운세','만평','우리말 바루기','로또 복권','오늘의 날씨','사랑방',
'인사','부고','사진','채서영의 별별영어','중앙SUNDAY 카툰','책꽂이','쿠킹','분수대','시조가 있는 아침','KCSI 우수기업','분양 FOCUS',
'삶의 향기','권근영의 그림 속 얼굴','노트북을 열며','머니 브리핑','BOOK책갈피','어린이책','스포츠 중계','주말의 경기','스포츠카',
'행복한책 읽기']

chosun_col = ['z','index','0','date']
joongang_col = ['z','index','context','date']
hani_col = ['z','index','category','title','pdate']
khan_col = ['z','index','context','date']
donga_col = ['z','index', '0','date']