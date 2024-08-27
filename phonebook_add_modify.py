import os
import pandas as pd

from tkinter import *
from tkinter import messagebox

class Add_Modify():
    def __init__(self, parent):
        # 전화번호 저장 처리
        phonebook_filename = "my_phonebook.csv"
        self.phonebook_file_path = os.path.join(os.path.dirname(__file__), phonebook_filename)

        self.df = pd.DataFrame(columns=["Name", "Phone", "Email"])

        if os.path.isfile(self.phonebook_file_path):
            # 저장 파일이 있을 경우 읽어서 초기화
            self.df = pd.read_csv(self.phonebook_file_path)
        else:
            print("새로운 연락처 저장소를 생성하였습니다.")
            self.df.to_csv(self.phonebook_file_path, index=False)    

        # 신규/수정 레이아웃
        self.modal = Toplevel(parent)
        self.modal.title("신규/수정")
        self.modal.geometry("300x180")
        self.modal.resizable(False, False)
        self.modal.protocol('WM_DELETE_WINDOW', self.close_modal)

        self.name, self.phone, self.email = \
            StringVar(self.modal), StringVar(self.modal), StringVar(self.modal)

        self.name_lbl = Label(self.modal, text = "이  름 : ", ).grid(row = 0, column = 0, padx = 10, pady = 10)
        self.phone_lbl = Label(self.modal, text = "연락처 : ").grid(row = 1, column = 0, padx = 10, pady = 10)
        self.email_lbl = Label(self.modal, text = "E-mail : ").grid(row = 2, column = 0, padx = 10, pady = 10)
        self.name_input = Entry(self.modal, textvariable = self.name)
        self.name_input.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.phone_input = Entry(self.modal, textvariable = self.phone)
        self.phone_input.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.email_input = Entry(self.modal, textvariable = self.email)
        self.email_input.grid(row = 2, column = 1, padx = 10, pady = 10)
        self.write_btn = Button(self.modal, text = "입력", command=self.write_info).grid(row = 3, column = 1, padx = 10, pady = 10)
        self.modal.focus_set()
        self.name_input.focus_set()

        self.modal.withdraw()

    # 신규 등록/수정 메서드
    def write_info(self):
        new_name = self.name.get()
        new_phone = self.phone.get()
        new_email = self.email.get()

        found = self.df[self.df["Name"] == new_name]
        if len(found):
            for i in found.index:
                self.df.loc[i] = {"Name": new_name, "Phone": new_phone, "Email": new_email}
        else:
            self.df.loc[len(self.df.index)] = {"Name": new_name, "Phone": new_phone, "Email": new_email}

        # 변경 사항 저장
        self.modal.lift()
        self.df.to_csv(self.phonebook_file_path, index=False)
        messagebox.showinfo(parent=self.modal, title="완료", message="정보가 저장되었습니다.")
        self.modal.withdraw()
        self.name_input.delete(0, END)
        self.phone_input.delete(0, END)
        self.email_input.delete(0, END)
    
    # 창 닫기 메서드
    def close_modal(self):
        self.modal.withdraw()
        self.name_input.delete(0, END)
        self.phone_input.delete(0, END)
        self.email_input.delete(0, END)

    

    # def get_focus(self):

    # def open_pam_modal(parent, name, phone, email):

    #     # # 신규/수정 레이아웃
    #     # modal = Toplevel(parent)
    #     # modal.title("신규/수정")
    #     # modal.geometry("300x180")
    #     # modal.resizable(False, False)

    #     # name_lbl = Label(modal, text = "이  름 : ", ).grid(row = 0, column = 0, padx = 10, pady = 10)
    #     # phone_lbl = Label(modal, text = "연락처 : ").grid(row = 1, column = 0, padx = 10, pady = 10)
    #     # email_lbl = Label(modal, text = "E-mail : ").grid(row = 2, column = 0, padx = 10, pady = 10)
    #     # username_input = Entry(modal, textvariable = name).grid(row = 0, column = 1, padx = 10, pady = 10)
    #     # phone_input = Entry(modal, textvariable = phone).grid(row = 1, column = 1, padx = 10, pady = 10)
    #     # email_input = Entry(modal, textvariable = email).grid(row = 2, column = 1, padx = 10, pady = 10)
    #     # write_btn = Button(modal, text = "입력", command=write_info).grid(row = 3, column = 1, padx = 10, pady = 10)

    #     modal.transient(parent)  # 부모 창 위에 표시
    #     modal.grab_set()         # 모달 창이 닫힐 때까지 부모 창 비활성화
    #     # parent.wait_window(modal)  # 모달 창이 닫힐 때까지 대기

