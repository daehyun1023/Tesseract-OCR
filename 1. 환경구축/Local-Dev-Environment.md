## Local Development Environment

#### ***WSL2 (Windows Subsystem for Linux)***  
* [wsl2 설치](https://docs.microsoft.com/ko-kr/windows/wsl/install-win10)는 해당 링크를 참고하며 개발환경을 구축했습니다.  

### 1. Linux용 Windows 하위 시스템 옵션 기능 사용  
~~~
(1) PowerShell을 관리자 권한으로 열어 실행  
(2) dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart  
~~~

### 2. Windows 10 실행, 버전 2004로 업데이트, 빌드 19041 이상  
~~~
(1) Windows 로고 키 + r 누르고, winver를 입력한 뒤 Windows 버전을 확인한다.  
(2) 빌드가 19041보다 낮은 경우, 최신 Windows 버전으로 업데이트 후 재부팅  
~~~

### 3. 가상 머신 플랫폼 옵션 기능을 사용하도록 설정  
~~~
(1) PowerShell을 관리자 권한으로 열어 실행  
(2) dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart  
~~~

### 4. Ubuntu 20.04 설치  
* [Microsoft Store](https://aka.ms/wslstore)를 열고 Ubuntu 20.04를 설치  
    
### 5. 배포 버전 설정  
~~~
(1) PowerShell을 관리자 권한으로 열어 실행  
(2) 각 Linux 배포에 할당된 wsl 버전 확인하기  
(3) wsl --list --verbose  
~~~

* wsl2를 기본 아키텍처로 설정하기  
~~~
wsl --set-version Ubuntu20.04 2  
wsl --set-default-version 2  
~~~
