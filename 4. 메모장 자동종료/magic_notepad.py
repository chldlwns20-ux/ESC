import tkinter as tk
import sys
import webbrowser

def check_text(event=None):
    # 텍스트 편집기에 입력된 모든 텍스트를 가져옵니다.
    content = text_area.get("1.0", "end-1c")
    content_lower = content.lower()
    
    # 1. '종료' 감지: 프로그램 즉시 종료
    if "종료" in content:
        root.destroy()
        sys.exit(0)
        
    # 2. '인하' 또는 'inha' 감지: 브라우저 열기
    if "인하" in content or "inha" in content_lower:
        # 인하공전 공식 홈페이지 접속
        webbrowser.open("https://www.inhatc.ac.kr")
        
        # 무한 반복 실행을 방지하기 위해 감지된 글자를 즉시 삭제
        new_content = content.replace("인하", "")
        new_content = new_content.replace("inha", "").replace("INHA", "").replace("Inha", "")
        
        text_area.delete("1.0", tk.END)
        text_area.insert("1.0", new_content)
        text_area.mark_set("insert", "end-1c")

# 메인 윈도우 생성
root = tk.Tk()
root.title("✨ 마법의 메모장 (프리미엄 에디션) ✨")
root.geometry("850x650")

# 전체 배경색 설정
root.configure(bg="#0F172A") 

# 상단 타이틀
header = tk.Label(
    root, 
    text="🌙 Magic Notepad", 
    font=("Malgun Gothic", 18, "bold", "italic"), 
    bg="#0F172A", 
    fg="#38BDF8",
    pady=15
)
header.pack()

# 프레임
text_container = tk.Frame(root, bg="#1E293B", bd=0)
text_container.pack(expand=True, fill='both', padx=40, pady=(0, 40))

# 텍스트 박스
text_area = tk.Text(
    text_container,
    font=("Malgun Gothic", 15),
    bg="#1E293B",              
    fg="#F8FAFC",              
    insertbackground="#38BDF8",
    selectbackground="#334155",
    relief="flat",             
    bd=0,                      
    padx=30,                   
    pady=30,                   
    spacing1=8,                
    spacing2=8
)
text_area.pack(expand=True, fill='both', padx=2, pady=2)

# 프로그램이 켜지면 안내 문구를 보여줍니다.
# 주의: 이 안내 문구 안에 트리거 단어들이 온전한 형태로('종료', '인하', 'inha') 들어가면 무한반복 버그 발생! 분리해서 표시해야 함.
welcome_message = """여기에 자유롭게 메모를 작성해 보세요.

비밀 기능 1: 글을 적다가 해당 단어(ㅈ+ㅗ+ㅇ+ㄹ+ㅛ)를 입력하는 순간 흔적도 없이 창이 사라집니다.✨
비밀 기능 2: 대학교 이름 앞 두 글자(ㅇ+ㅣ+ㄴ+ㅎ+ㅏ) 또는 영어(i + n + h + a 연속)를 입력하면 비밀의 문이 열립니다. 🏫
----------------------------------------------------------------------
"""
text_area.insert("1.0", welcome_message)

# 커서를 끝으로 이동
text_area.mark_set("insert", "end-1c")
text_area.focus_set()

# 감지 이벤트
text_area.bind("<KeyRelease>", check_text)

root.mainloop()
