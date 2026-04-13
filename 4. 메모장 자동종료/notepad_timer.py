import subprocess
import time

def run_and_close_notepad():
    try:
        # 메모장 실행
        subprocess.Popen("notepad.exe")
        
        # 5초 대기
        time.sleep(5)
        
        # 윈도우 10/11 환경에서는 메모장이 백그라운드 탭 기반 앱으로 실행될 수 있어 PID로 종료되지 않을 수 있습니다.
        # 강제로 'notepad.exe' 프로세스를 찾아 모두 절전/종료 시킵니다.
        subprocess.run(["taskkill", "/F", "/IM", "notepad.exe", "/T"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        pass

if __name__ == "__main__":
    run_and_close_notepad()
