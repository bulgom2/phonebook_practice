import os
import pandas as pd

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv

class Show_All():
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

        # 모두 보기 레이아웃
        self.modal = Toplevel(parent)
        self.modal.title("전화번호 목록")
        self.modal.geometry("600x200")
        self.modal.resizable(False, False)
        self.modal.protocol('WM_DELETE_WINDOW', self.modal.withdraw())
     
        self.num_list = ttk.Treeview(self.modal, columns = ('Name', 'Phone', 'Email'), show = "headings")
        self.num_list.heading('#1', text = '이름')
        self.num_list.heading('#2', text = '전화번호')
        self.num_list.heading('#3', text = '이메일')
        self.num_list.pack()
        TableMargin = Frame(self.modal,)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        scrollbary.config(command=self.num_list.yview)
        scrollbary.pack(side=RIGHT, fill=Y)

        with open('my_phonebook.csv') as pb:
            reader = csv.DictReader(pb, delimiter=',')
            for row in reader:
                name = row['Name']
                phone = row['Phone']
                email = row['Email']
                self.num_list.insert("", 0, values=(name, phone, email))

        # self.delete_btn = Button(self.modal, text = "삭제", command=self.delete_info).grid(row = 3, column = 0, padx = 10, pady = 10)
        # self.close_btn = Button(self.modal, text="닫기", command=self.close_modal).grid(row = 3, column = 2, padx = 10, pady = 10)

        self.modal.withdraw()

    # # 찾기 메서드
    # def find_info(self):
    #     existing_name = self.name.get()

    #     found = self.df[self.df["Name"] == existing_name]
    #     if len(found):
    #         for i in found.index:
    #             row = self.df.loc[i]
    #             self.found_lbl["text"] = ("{} {} {}".format(row["Name"], row["Phone"], row["Email"]))
    #     else:
    #         self.found_lbl["text"] =(f"{existing_name}을(를) 찾을 수 없습니다.")
        
    # 창 닫기 메서드
    def close_modal(self):
        self.modal.withdraw()
        self.modal.destroy()