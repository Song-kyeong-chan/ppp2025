import PySimpleGUI as sg

# 팝업 레이아웃
layout = [
    [sg.Text("작업을 진행하시겠습니까?")],
    [sg.Button("확인"), sg.Button("취소"), sg.Button("도움말")]
]

# 팝업 창 생성 (modal=True → 다른 창 눌러도 못 건드리게 막음)
window = sg.Window("사용자 선택", layout, modal=True)

# 이벤트 처리
while True:
    event, _ = window.read()
    if event in (sg.WINDOW_CLOSED, "취소"):
        sg.popup("작업이 취소되었습니다.")
        break
    elif event == "확인":
        sg.popup("작업이 진행됩니다!")
        break
    elif event == "도움말":
        sg.popup("도움말: 이 버튼은 작업을 진행하거나 취소할 수 있습니다.")

window.close()
