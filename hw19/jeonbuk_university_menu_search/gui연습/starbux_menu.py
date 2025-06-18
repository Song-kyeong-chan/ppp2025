import PySimpleGUI as sg
import os
from PIL import Image # PySimpleGUI는 내부적으로 Pillow(PIL)를 사용해서 이미지 처리
import io # io 쓰는 이유: PySimpleGUI에 이미지 넘길때 실제 파일 없이 메모리상에서 넘겨줌 => 메모리 기반 이미지

# 스타벅스 메뉴 샘플
menus = [
    {"store": "스타벅스 전북대점", "menu": "아이스 카페 아메리카노", "price": 4500},
    {"store": "스타벅스 전북대점", "menu": "카페 라떼", "price": 5000},
    {"store": "스타벅스 전북대점", "menu": "카라멜 마키아또", "price": 5700},
    {"store": "스타벅스 전북대점", "menu": "자바 칩 프라푸치노", "price": 6100},
    {"store": "스타벅스 전북대점", "menu": "딸기 딜라이트 요거트 블렌디드", "price": 5900},
]

# 이미지 처리 함수
def load_image(menu_name):
    filename = menu_name.replace(' ','')
    path = os.path.join("images", f"{filename}.jpg")
    try:
        img = Image.open(path).resize((100,100))
        bio = io.BytesIO()
        img.save(bio, format = "PNG") # PNG 형식으로 bio에 이미지 저장
        return sg.Image(data = bio.getvalue(), size = (100,100))
    except:
        return sg.Text("이미지 오류", size= (14,1), justification='center')

# 메뉴 카드 생성 함수
def create_menu_card(menu):
    image_elem = load_image(menu["menu"])
    return sg.Frame(
        title=menu["menu"],
        title_location= 'n', # n: 상단가운데 정렬, s: 하단 가운데 정렬, w: 왼쪽가운데, e: 오른쪽가운데 정렬
        layout=[
            [image_elem],
            [sg.Text(f"가격: {menu['price']}원", justification="center")],
            [sg.Button("상세보기", key=f"DETAIL::{menu['store']}::{menu['menu']}")]
        ],
        relief=sg.RELIEF_FLAT,
        element_justification='center',
        pad=(5, 5)
    )

# 전체 레이아웃 구성 (카드를 2개씩 가로 배치)
def generate_card_layout(filtered_menus):
    layout = []
    row = []
    for i, menu in enumerate(filtered_menus):
        row.append(create_menu_card(menu))
        if len(row) == 2 or i == len(filtered_menus) - 1 :
            layout.append(row)
            row = []
    return layout


def run_window(filtered_menus,query):
    layout = [
        [sg.Text(f"{query}에 대한 검색결과")],
        [sg.Push(),sg.Column(generate_card_layout(filtered_menus)),sg.Push()],
        [sg.Button("뒤로가기"),sg.Button("종료")]
    ]
    window = sg.Window(f"{query}에 대한 결과", layout)
    
    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED,"종료"):
            break
        elif event == "뒤로가기":
            window.close()
            start_window(menus)
            return
        elif event.startswith("DETAIL::"):
            _, store, menu = event.split("::")
            sg.popup(f"{store}의\n{menu} 메뉴 상세정보입니다.")
    window.close()
    
def start_window(menus):
    card_layout = generate_card_layout(menus)
    layout = [
        [sg.Text("메뉴 검색:"), sg.Input(key = "-QUERY-"), sg.Button("검색")],
        [sg.Push(),sg.Column(card_layout, key= "-CARDS-"),sg.Push()], # Column(): 내부에 다른 요소들을 수직 또는 수평으로 묶는 레이아웃 박스, [[Frame, Frame],[Frame, Frame]]
        [sg.Button("종료")]
    
    ]

    # 창 생성
    window = sg.Window("스타벅스 메뉴 검색", layout)

    # 이벤트 루프
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "종료"):
            break
        elif event == "검색":
            query = values["-QUERY-"]
            query_strip = query.strip()
            filtered = [m for m in menus if query_strip in m["menu"]]
            window.close()
            run_window(filtered,query)
        elif event.startswith("DETAIL::"):
            _, store, menu = event.split("::")
            sg.popup(f"{store}의\n{menu} 메뉴 상세정보입니다.")

    window.close()
    
start_window(menus)

