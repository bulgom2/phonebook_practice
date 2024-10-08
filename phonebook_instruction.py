# 내부 자료구조는 pandas
import os
import pandas as pd



def main_menu() -> int:
    """사용자의 입력을 받아서 검증하고 적절하다면 정수로 반환합니다."""
    while user_input := input("(1) 찾기 (2) 추가/변경 (3) 삭제 (4) 모두 보기 (5) 종료 : "):
        if user_input in ("1", "2", "3", "4", "5"):
            return int(user_input)
        else:
            print("잘못된 명령입니다.")


def show_all():
    """모든 데이터 출력"""
    if not len(df.index):
        print("현재 등록된 연락처가 없습니다.")
    else:
        # for row in df.itertuples():
        #     print("{} {} {}".format(row.Name, row.Phone, row.Email))
        print(df)
        # for i in df.index:
        #     row = df.loc[i]
        #     print(f'{row["Name"]} {row["Phone"]} {row["Email"]}')


def find_person():
    """이름을 입력받고 그 이름으로 찾아서 해당 데이터 출력"""
    user_input = input("이름을 입력해주세요 : ")
    found = df[df["Name"] == user_input]
    if len(found.index):
        for i in found.index:
            row = df.loc[i]
            print("{} {} {}".format(row["Name"], row["Phone"], row["Email"]))
    else:
        print(f'"{user_input}"를 찾지 못했습니다.')


def update_person():
    """사람 추가 또는 수정
    사용자로부터 이름, 전화번호, 이메일을 입력받아서
    이미 있는 이름이면 업데이트를 하고
    없는 이름이면 새로 추가
    """
    name = input("이름을 입력해주세요 : ")
    phone = input("전화번호를 입력해주세요 : ")
    email = input("이메일을 입력해주세요 : ")
    found = df[df["Name"] == name]
    if len(found):  # 이미 존재하는 사람일 경우
        for i in found.index:
            df.loc[i] = {"Name": name, "Phone": phone, "Email": email}
    else:  # 새로운 사람 등록
        df.loc[len(df.index)] = {"Name": name, "Phone": phone, "Email": email}


def delete_person():
    """이름을 입력받아서 데이터 삭제"""
    user_input = input("이름을 입력해주세요 : ")
    found = df[df["Name"] == user_input]
    if len(found):
        df.drop(found.index, inplace=True)
    else:
        print(f'"{user_input}"를 찾지 못했습니다.')


if __name__ == "__main__":
    # 프로그램 실행의 시작
    # 시작할 때 저장파일이 존재하면 읽어들여서 데이터 초기화
    # 메인메뉴에서 사용자 입력을 받은 후에 알맞게 기능 수행
    # 종료할 때 데이터 저장

    
    # 전화번호부 저장용 파일 변수
    phonebook_filename = "my_phonebook.csv"
    phonebook_file_path = os.path.join(os.path.dirname(__file__), phonebook_filename)
    
    # 전화번호부 저장용 DataFrame (전역변수)
    df = pd.DataFrame(columns=["Name", "Phone", "Email"])

    if os.path.isfile(phonebook_file_path):
        # 저장 파일이 있을 경우 읽어서 초기화
        df = pd.read_csv(phonebook_file_path)
    else:
        print("새로운 연락처 저장소를 생성하였습니다.")
        df.to_csv(phonebook_file_path, index=False)    

    # main_menu()로 받아온 사용자의 입력에 따라 함수 호출
    while (selected := main_menu()) != 5:  # 5는 종료 메뉴
        if selected == 1:
            find_person()
        elif selected == 2:
            update_person()
        elif selected == 3:
            delete_person()
        elif selected == 4:
            show_all()
    else:
        # 종료하기 전 파일로 데이터 저장
        df.to_csv(phonebook_file_path, index=False)
        print("종료합니다.")

