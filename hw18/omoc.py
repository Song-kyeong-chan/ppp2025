import pygame
import sys

# 초기 설정
pygame.init()
SIZE = 600
GRID_SIZE = 25
CELL_SIZE = SIZE // GRID_SIZE
STONE_RADIUS = CELL_SIZE // 2 - 2
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BG_COLOR = (222, 184, 135)

screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("오목 by 씽쌩쏭")

# 오목판 상태
board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]  # 0: 빈칸, 1: 흑, 2: 백
turn = 1  # 1: 흑돌, 2: 백돌

# 승리 조건 검사
def check_win(x, y, color):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for dx, dy in directions:
        count = 1
        for dir in [1, -1]:
            nx, ny = x, y
            while True:
                nx += dx * dir
                ny += dy * dir
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and board[ny][nx] == color:
                    count += 1
                else:
                    break
        if count >= 5:
            return True
    return False

# 보드 그리기
def draw_board():
    screen.fill(BG_COLOR)
    for i in range(GRID_SIZE):
        pygame.draw.line(screen, BLACK,
                         (CELL_SIZE // 2, CELL_SIZE // 2 + i * CELL_SIZE),
                         (SIZE - CELL_SIZE // 2, CELL_SIZE // 2 + i * CELL_SIZE))
        pygame.draw.line(screen, BLACK,
                         (CELL_SIZE // 2 + i * CELL_SIZE, CELL_SIZE // 2),
                         (CELL_SIZE // 2 + i * CELL_SIZE, SIZE - CELL_SIZE // 2))

    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if board[y][x] == 1:
                pygame.draw.circle(screen, BLACK, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), STONE_RADIUS)
            elif board[y][x] == 2:
                pygame.draw.circle(screen, WHITE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), STONE_RADIUS)

# 게임 루프
running = True
while running:
    draw_board()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            x = mx // CELL_SIZE
            y = my // CELL_SIZE

            if board[y][x] == 0:
                board[y][x] = turn
                if check_win(x, y, turn):
                    print("플레이어 {} 승리!".format("흑" if turn == 1 else "백"))
                    pygame.time.wait(2000)
                    board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
                    turn = 1
                    continue
                turn = 3 - turn  # 1 ↔ 2 교체

pygame.quit()
sys.exit()
