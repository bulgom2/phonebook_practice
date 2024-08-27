import os
import pandas as pd

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class PAM():
    def __init__(self, parent):

        # 신규/수정 레이아웃
        self.modal = Toplevel(parent)
        self.modal.title("신규/수정")
        self.modal.geometry("300x180")
        self.modal.resizable(False, False)

        self.name, self.phone, self.email = \
            StringVar(self.modal), StringVar(self.modal), StringVar(self.modal)

        self.name_lbl = Label(self.modal, text = "이  름 : ", ).grid(row = 0, column = 0, padx = 10, pady = 10)
        self.phone_lbl = Label(self.modal, text = "연락처 : ").grid(row = 1, column = 0, padx = 10, pady = 10)
        self.email_lbl = Label(self.modal, text = "E-mail : ").grid(row = 2, column = 0, padx = 10, pady = 10)
        self.username_input = Entry(self.modal, textvariable = self.name).grid(row = 0, column = 1, padx = 10, pady = 10)
        self.phone_input = Entry(self.modal, textvariable = self.phone).grid(row = 1, column = 1, padx = 10, pady = 10)
        self.email_input = Entry(self.modal, textvariable = self.email).grid(row = 2, column = 1, padx = 10, pady = 10)
        self.write_btn = Button(self.modal, text = "입력", command=self.write_info).grid(row = 3, column = 1, padx = 10, pady = 10)

        self.modal.wait_window()

    # 신규 등록/수정 메서드
    def write_info(self):
        # new_name = self.name.get()
        # new_phone = self.phone.get()
        # new_email = self.email.get()

        messagebox.showinfo("완료", "정보가 저장되었습니다.")
        self.modal.destroy()

    # def __del__(self):
    #     return self.name.get(), self.phone.get(), self.email.get()

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

