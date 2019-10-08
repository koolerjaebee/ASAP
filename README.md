# ASAP (Auto Site Alternative-login Program)
## pip list
- selenium

## install list
- chromedriver.exe

## howto

![1](.\screenshots\1.png)



작업 스케줄러 열기



![2](.\screenshots\2.PNG)



작업 만들기



![3](.\screenshots\3.PNG)



일반 탭



![4](.\screenshots\4.PNG)



트리거 탭 새로 만들기



![5](.\screenshots\5.PNG)



트리거 설정 

원하는 시간 설정 가능합니다.



![6](.\screenshots\6.PNG)



동작 탭 새로 만들기



![7](.\screenshots\7.PNG)



프로그램/스크립트 : pythonw.exe 의 디렉토리

인수 추가 : login.py 의 디렉토리



## FAQ

- '이 앱은 사용자 보호를 위해 차단되었습니다.' 라고 뜨면서 작업 스케줄러가 안열립니다.

  관리자 권한으로 cmd 실행

  'secpol.msc' 입력

  로컬 보안 정책 창에서 '보안설정 > 로컬정책 > 보안옵션' 선택

  '사용자 계정 컨트롤: 관리 승인 모드에서 모든 관리자 실행' 의 보안설정을 '사용'에서 '사용 안 함'으로 변경



## Reference

- ChromeDriver - WebDriver for Chrome https://chromedriver.chromium.org/downloads