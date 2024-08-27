from importlib import reload
from tkinter import *
from tkinter import messagebox
from phonebook_add_modify import Add_Modify
from phonebook_delete import Delete
from phonebook_find import Find_By_Name
from phonebook_show_all import Show_All


window = Tk()
window.title("전화번호부")
window.geometry("450x150")
window.resizable(False, False)


# 찾기 모듈 연결
def activate_pf():
    pf = Find_By_Name(window)
    pf.modal.deiconify()

# 추가/수정 모듈 연결
def activate_pam():
    pam = Add_Modify(window)
    pam.modal.deiconify()   # 모달 보이기
    # pam.modal.grab_set()    # 모달 창이 닫힐 때까지 부모 창 비활성화

# 삭제 모듈 연결
def activate_pdel():
    pdel = Delete(window)
    pdel.modal.deiconify()

# 모두 보기 모듈 연견
def activate_pso():
    pso = Show_All(window)
    pso.modal.deiconify()


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
    command=activate_pf,
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
    command=activate_pdel,
)
show_all_btn = Button(
    master=main_frame,
    text="모두 보기",
    fg="black",
    font=("Arial", 15),
    command=activate_pso,
)

main_frame.pack(pady=30)
select_menu_lbl.grid(row=0, column=0, columnspan=4,)
find_btn.grid(row=1, column=0, sticky='nesw')
add_modify_btn.grid(row=1, column=1, sticky='nesw')
delete_btn.grid(row=1, column=2, sticky='nesw')
show_all_btn.grid(row=1, column=3, sticky='nesw')



window.mainloop()