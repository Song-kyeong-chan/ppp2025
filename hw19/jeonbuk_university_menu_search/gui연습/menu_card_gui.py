import PySimpleGUI as sg

# 예시 데이터
sample_menus = [
    {"store": "스타벅스 전북대점", "menu": "아메리카노", "price": 4500},
    {"store": "김밥천국 덕진점", "menu": "떡볶이", "price": 3500},
    {"store": "홍콩반점 전북대점", "menu": "짜장면", "price": 5000}
]

# 카드 형태 UI 생성 함수, Frame: 묶음박스
def create_menu_card(menu):
    return sg.Frame(
        title=menu['store'],
        layout=[
            [sg.Text(f"메뉴: {menu['menu']}")],
            [sg.Text(f"가격: {menu['price']}원")],
            [sg.Button("상세보기", key=f"DETAIL::{menu['store']}::{menu['menu']}")]
        ],
        # 테두리 스타일 설정, sg.frame의 속성; sg.RELIEF_FLAT :: 평면, sg.RELIEF_SUNKEN::눌린느낌, sg.RELIEF_GROOVE,sg.RELIEF_RIDGE:: 홈/돌기모양
        relief=sg.RELIEF_RAISED, # sg.RELIEF_RAISED:: 테두리가 살짝 튀어나온 느낌
        element_justification='left', # 프레임 내부에 있는 요소들의 정렯방식
        pad=(5, 5) # padding , 프레임 외부 상하좌우 5px씩 여뱍
    )

# 전체 레이아웃
layout = [[create_menu_card(menu)] for menu in sample_menus]
layout += [[sg.Button("종료")]]

# 윈도우 실행
window = sg.Window("전북대 주변 메뉴 추천", layout)

while True:
    event, values = window.read() # GUI내에서 어떤 버튼을 눌렀는지 감지하는 함수
    if event in (sg.WIN_CLOSED, "종료"): # event: 버튼 "이름", values: 입력창 등에서 입력한 값들이 딕셔너리 형태로 들어감
        break
    elif event.startswith("DETAIL::"):
        _, store, menu = event.split("::")
        # sg.popup: 간단한 팝업창으로 메시지 띄움
        sg.popup(f"{store} - {menu} 상세정보 페이지입니다.")

window.close()
