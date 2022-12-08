![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=300&section=header&text=Book_Project&fontSize=90&animation=fadeIn&fontAlignY=38&desc=&descAlignY=51&descAlign=62)
<p align='center'></p>
<p align='right'>


# 프로젝트 개요
대용량의 데이터가 존재하는 필드와 분석의 가치가 있는 필드의 교집합 탐색을 위해 팀원들의 관심사를 공유하게 됨 팀원들 모두 독서를 즐기지만, 각각 선호 장르의 차이, 읽는 방식의 차이가 존재해 이에 대한 호기심을 바탕으로 국내 도서시장과 국내 소비자들을 대상으로 한 프로젝트를 기획하게 됨 

# 프로젝트의 필요성
해당 프로젝트를 통해 도서 시장에 대한 이해도를 높이며 가설검정 과정을 통해 실제로 뉴스 내 키워드 언급량과 도서 판매량의 증감이 차이가 있는지를 증명함  

# 문제정의
도서 소비자들의 여가시간 내 독서 이외의 선택지가 늘어나며 연간 독서율이 점차 우하향하는 추세 이다. 도서 시장이 이런 독서율 추세 상황에서 소비자를 확보하고, 성장을 이루기 위해서는 소비자들의 독서 문화와 그 독서 문화에 영향을 주는 요인들을 파악해야 한다.
  
# Poject Purpose of Analysis
- 도서 시장 현황 및 최근 독서 형태 현황 분석
- 소비자층 분석과 도서시장 트랜드 시각화
- 뉴스 키워드 추이와 도서 판매량 상관관계 가설 수립 및 검증
  
# Project Purpse of Development
- 배치 ELT 파이프라인 및 배포용 웹 백엔드 구현

# Team_감자탈출넘버원 팀원
- Data Engineering [#이영동](https://github.com/leeyoungdong) [#강인구](https://github.com/okok7272)  [#이진봉](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FciOs8M%2Fbtq0oa3h0xS%2FCgClHwDFFtYq1fta4dkkw0%2Fimg.jpg)
- Data Analyst [#천세희](https://github.com/Alice1304) [#박성희](https://github.com/aurorave)
  
# 기술 스택
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/Amazon S3-569A31?style=for-the-badge&logo=Amazon S3&logoColor=white"> <img src="https://img.shields.io/badge/Amazon EC2-FF9900?style=for-the-badge&logo=Amazon EC2&logoColor=white"> <img src="https://img.shields.io/badge/Apache Airflow-017CEE?style=for-the-badge&logo=Apache Airflow&logoColor=white"> <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white"> <img src="https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=Tableau&logoColor=white">

# 데이터 파이프라인 (ELT)
![image](https://user-images.githubusercontent.com/87170837/206433156-b03af7cb-52b3-40e3-865d-bf887af15b67.png)
- 도서/뉴스 데이터를 추출(Extract)해 Local My SQL에 적재(Load) 한후 원본데이터를 백업(innodb )
- 적재한 데이터를 RDS에 옮기기전 전처리와 Column을 재정의(Transform)한 후 RDS에 적재
- RDS에 적재된 데이터를 DA에서 분석 진행 후 Tableau를 사용한 BI분석 및 대시보드 생성
- RDS에 적재된 데이터는 S3스냅샷을 통해 Parquet로 2차 백업 진행
- RDS에 적재된 데이터를 통해 Django 쿼리 질의 웹 구성 및 배포
- Airflow Dag을 통한 일/ 주/ 월/ 년 단위 E/ L/ T Cronjob 진행
- Prometheus와 Grafana를 통한 데이터 작업시 컴퓨터 리소스 및 데이터 로그 시각화
  
# 데이터
# 원본 데이터 출처
![image](https://user-images.githubusercontent.com/87170837/206435454-2cee3552-334e-4e81-a36e-3528ee6e566c.png)
- 도서 베스트 셀러 데이터 - YES 24, 교보문고, 알라딘, INTERPARK (BS4 Crawling)
- 종합 뉴스 데이터 - 경향신문, 조선일보, 동아일보, 한겨례, 중앙일보 (BS4 Crawling)
- 도서 정보 데이터 - 국립중앙도서관 (API)

# Data Lake
Historical Data
![image](https://user-images.githubusercontent.com/87170837/206432241-543fc326-cb8e-4fd3-a4bf-d18804cc7bdc.png)

# Data Warehouse
Historical Data
![image](https://user-images.githubusercontent.com/87170837/206432283-2acd02c2-2594-4883-90ad-e21b832aeb10.png)

# 프로젝트 결과물
# BI(Business Intelligence) [클릭시 자세히 보기]

[![CP2](https://user-images.githubusercontent.com/87170837/206512170-dfcd39cb-c09b-461e-9e16-ecc1027509b9.png)](https://public.tableau.com/app/profile/.10992200/viz/shared/7N343HKXK)
# DJANGO

# AIRFLOW
![image](https://user-images.githubusercontent.com/87170837/206512889-c45e8ae0-635f-44ac-b916-a981a3614739.png)

![image](https://user-images.githubusercontent.com/87170837/206513196-47b40a8a-0bec-4a13-82d0-9f4696a75d82.png)

# GRAFANA

# 프로젝트 회고

# 개선점
