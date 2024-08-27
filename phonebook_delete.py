import os
import pandas as pd

from tkinter import *
from tkinter import messagebox

class Delete():
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

        # 삭제 레이아웃
        self.modal = Toplevel(parent)
        self.modal.title("전화번호 삭제")
        self.modal.geometry("300x180")
        self.modal.resizable(False, False)
        self.modal.protocol('WM_DELETE_WINDOW', self.close_modal)
        # self.modal.attributes('-topmost', 'true')    # 윈도우 최상위로 올리기
     
        self.name = StringVar(self.modal)

        self.name_lbl = Label(self.modal, text = "이  름 : ", ).grid(row = 0, column = 0, padx = 10, pady = 10)
        self.name_input = Entry(self.modal, textvariable = self.name)
        self.name_input.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.name_input.bind("<Return>", lambda _: self.delete_info())
        self.modal.focus_set()
        self.name_input.focus_set()
        # self.delete_btn = Button(self.modal, text = "삭제", command=self.delete_info).grid(row = 3, column = 0, padx = 10, pady = 10)
        # self.close_btn = Button(self.modal, text="닫기", command=self.close_modal).grid(row = 3, column = 2, padx = 10, pady = 10) 
        self.modal.withdraw()

    # 삭제 메서드
    def delete_info(self):
        existing_name = self.name.get()

        found = self.df[self.df["Name"] == existing_name]
        if len(found):
            self.df.drop(found.index, inplace=True)
            self.df.to_csv(self.phonebook_file_path, index=False)
            messagebox.showinfo(parent=self.modal, title="삭제 완료", message=f'"{existing_name}"을/를 삭제하였습니다.')
            self.name_input.delete(0, END)
            self.modal.lift()
        else:
            messagebox.showwarning(parent=self.modal, title="오류", message=f'"{existing_name}"을/를 찾지 못했습니다.')
        
        
    # 창 닫기 메서드
    def close_modal(self):
        self.modal.withdraw()
        self.name_input.delete(0, END)