import os
import pandas as pd
from tkinter import *
from tkinter import messagebox
from phonebook_msgbox import PAM


def activate_pam():
    result = PAM(window)
    new_name, new_phone, new_email = result.name.get(), result.phone.get(), result.email.get()
    del result # 소거
    found = df[df["Name"] == new_name]
    if len(found):
        for i in found.index:
            df.loc[i] = {"Name": new_name, "Phone": new_phone, "Email": new_email}
    else:
        df.loc[len(df.index)] = {"Name": new_name, "Phone": new_phone, "Email": new_email}

    df.to_csv(phonebook_file_path, index=False)

window = Tk()
window.title("전화번호부")
window.geometry("450x150")
window.resizable(False, False)


# 전화번호 저장 처리
phonebook_filename = "my_phonebook.csv"
phonebook_file_path = os.path.join(os.path.dirname(__file__), phonebook_filename)

df = pd.DataFrame(columns=["Name", "Phone", "Email"])

if os.path.isfile(phonebook_file_path):
    # 저장 파일이 있을 경우 읽어서 초기화
    df = pd.read_csv(phonebook_file_path)
else:
    print("새로운 연락처 저장소를 생성하였습니다.")
    df.to_csv(phonebook_file_path, index=False)

# 메인화면 창닫기 메서드
def funcClose():
    resp = messagebox.askokcancel("종료", "종료하시겠습니까?")
    if resp == 1:
        window.destroy()
    else:
        pass

window.protocol('WM_DELETE_WINDOW', funcClose)

# 신규/수정 열기 메서드

# 메인 화면 구성
main_frame = Frame(master=window)
select_menu_lbl = Label(main_frame, text="원하는 메뉴를 선택하세요", justify=CENTER, font=("Arial", 25))

# 메인 버튼
find_btn = Button(
    master=main_frame,
    text="찾기",
    fg="black",
    font=("Arial", 15),
    # command=pam.write_info,
)

add_modify_btn = Button(
    master=main_frame,
    text="추가/변경",
    fg="black",
    font=("Arial", 15),
    command=activate_pam,
)

delete_btn = Button(
    master=main_frame,
    text="삭제",
    fg="black",
    font=("Arial", 15),
    # command=enter_pressed,
)
show_all_btn = Button(
    master=main_frame,
    text="모두 보기",
    fg="black",
    font=("Arial", 15),
    # command=enter_pressed,
)

main_frame.pack(pady=30)
select_menu_lbl.grid(row=0, column=0, columnspan=4,)
find_btn.grid(row=1, column=0, sticky='nesw')
add_modify_btn.grid(row=1, column=1, sticky='nesw')
delete_btn.grid(row=1, column=2, sticky='nesw')
show_all_btn.grid(row=1, column=3, sticky='nesw')



window.mainloop()