# PyQt Calculator
<img src="https://img.shields.io/badge/PYTHON3-3776AB?style=for-the-badge&logo=PYTHON&logoColor=white"> <img src="https://img.shields.io/badge/Anaconda-44A833?style=for-the-badge&logo=Anaconda&logoColor=white">

### Build a calculator using PyQt5 in Python.
- 화면 UI

① <img src="https://user-images.githubusercontent.com/69224744/147195303-32c93610-1383-43d3-b6ef-049bd447ec00.png" /> &nbsp;
② <img src="https://user-images.githubusercontent.com/69224744/147196556-4cb33e8c-3ee0-494d-a297-cfb9adbf7ec5.png" />

- [실행 파일(.exe) 다운](https://drive.google.com/drive/folders/1vZghImyiCG-NkEmZGmCOKZh0WyjPHCXP?usp=sharing)

## Windows
### Prerequisite
- PyQt5
- Qt Designer (Only for developers for editing layouts)


## Feature
- 입력한 수식 상태를 화면에 출력
- 입력 가능한 숫자의 자리수 제한 (소수점 포함 11자리)
- 연산자가 입력 되면 Backspace 기능 제한
- ZeroDivisionError 의 경우, 버튼 비활성화 기능 사용
  - 활성화 된 버튼을 입력 하면 화면 ① 상태로 복구

  ![calc-ui-3](https://user-images.githubusercontent.com/69224744/147274435-6f8ba74b-605c-4e3a-8dcf-cf6f299abe43.png)

- 실수 연산 시, 결과 값이 .0으로 끝나면 정수로 출력하도록 구현

  ![calc-ui-5](https://user-images.githubusercontent.com/69224744/147278879-d316b47b-c655-4957-9813-2ff2d09b9445.png)


## 개선 사항
- 부동 소수점 입력 시, 지수 형태로 출력
- 음수 입력 기능 추가




