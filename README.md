# Remember Calculator — 기억 계산기
기본 연산 기능에 기록 저장 기능을 더한 기억 계산기입니다. 디자인은 윈도우10 기본 계산기를 참고했습니다.


<a href="https://www.python.org">
<img src="https://img.shields.io/badge/Python3+-3776AB?style=flat&logo=PYTHON&logoColor=white&link=https://www.python.org/"></a>
<a href="https://www.anaconda.com">
<img src="https://img.shields.io/badge/Anaconda-44A833?style=flat&logo=Anaconda&logoColor=white&link=https://www.anaconda.com/"></a>
<a href="https://qt-brandbook.webflow.io">
<img src="https://img.shields.io/badge/Qt-41CD52?style=flat&logo=Qt&logoColor=white&link=https://qt-brandbook.webflow.io/"></a>

#### [실행 파일(.exe) 다운](https://vo.la/qMtA3)

## UI Design
<img src="https://user-images.githubusercontent.com/69224744/150674209-dd08afc0-26e7-4b08-87c1-6faac8b4ad5e.gif" title="실행 결과" hspace="10"/>

## Windows OS based
### Prerequisite
- PyQt5
- Qt Designer (Only for developers for editing layouts)

## Feature
- 입력한 수식을 화면에 출력.
- 최근 연산은 화면 오른쪽 상단에 누적 표시.
  - 클릭 시, 해당 기록을 화면에 출력
- **내보내기 기능**으로 계산 기록을 텍스트 파일로 저장 (+22.01.23)
<img src="https://user-images.githubusercontent.com/69224744/150676796-a830d690-76a9-4cc1-8473-369edd79cedf.gif" hspace="10"/>

- 자리수 구분 단위 , 표시 (+22.01.14)
- 실수 연산 시 .0으로 끝나면 정수로 출력
- 입력 가능 숫자의 자리수를 제한 (소수점 포함 11자리)
- 연산자 입력 시, Backspace 기능 제한
- 예외 처리 시, 일부 버튼 비활성화 (ex. 0으로 나눈 경우)
  - 활성화 된 버튼을 누르면 리셋
  

## 개선 사항
- 부동 소수점 입력 시, 지수 형태로 출력
- 음수 입력 기능 필요
