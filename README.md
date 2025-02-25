# Remember Calculator — 기억 계산기
기억 계산기는 사용자의 계산 기록을 외부로 저장할 수 있도록 구현한 계산기 응용프로그램입니다. 디자인과 기능은 윈도우에 포함된 기본 계산기를 참고했습니다.

## UI Design
<img src="https://user-images.githubusercontent.com/69224744/150674209-dd08afc0-26e7-4b08-87c1-6faac8b4ad5e.gif" title="실행 결과" hspace="10"/>

## Windows OS based
### Prerequisite
- PyQt5
- Qt Designer (Only for developers for editing layouts)

## Feature
- **가독성을 높인 사용자 중심의 UI**
  - 자릿수 구분 단위(,) 표시
  - 정수 출력 형태 지정
- **내보내기 기능**
  - 사용자의 계산 기록을 텍스트 파일로 저장 가능
- **계산 기록 활용 기능**
  - 최근 연산 결과를 내림차순 형태로 오른쪽 상단에 누적 표시
  - 이전 기록 클릭 시, 계산기 화면에 표시
- **버튼을 활용한 다양한 예외 처리 기능**
  - 연산자를 연속으로 입력할 경우, Backspace 기능을 제한
  - "0"으로 나눌 경우, "inf" 출력 후 일부 기능을 제한
<img src="https://user-images.githubusercontent.com/69224744/150676796-a830d690-76a9-4cc1-8473-369edd79cedf.gif" hspace="10"/>

## Tech Stack
<a href="https://www.python.org">
<img src="https://img.shields.io/badge/Python3+-3776AB?style=flat&logo=PYTHON&logoColor=white&link=https://www.python.org/"></a>
<a href="https://www.anaconda.com">
<img src="https://img.shields.io/badge/Anaconda-44A833?style=flat&logo=Anaconda&logoColor=white&link=https://www.anaconda.com/"></a>
<a href="https://qt-brandbook.webflow.io">
<img src="https://img.shields.io/badge/Qt-41CD52?style=flat&logo=Qt&logoColor=white&link=https://qt-brandbook.webflow.io/"></a>

## 개선 사항
- 부동 소수점 처리
- 음수 입력 기능 필요
