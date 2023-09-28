from pico2d import *

open_canvas()

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('run_pachirisu.png')

running = True
x = 100  # 초기 x 좌표
y = 250  # 초기 y 좌표
frame = 0  # 변수 초기화

dir_x = 0  # x 방향 이동 변수
dir_y = 0  # y 방향 이동 변수

# 이전 좌우 반전 상태를 저장할 변수
prev_flip = False

# 화면 너비와 높이
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1024

# 캐릭터 이미지의 폭과 높이
character_width = 100
character_height = 100

def handle_events():
    global running, dir_x, dir_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1  # 오른쪽
            elif event.key == SDLK_LEFT:
                dir_x -= 1  # 왼쪽
            elif event.key == SDLK_UP:
                dir_y += 1  # 위
            elif event.key == SDLK_DOWN:
                dir_y -= 1  # 아래
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1  # 이동 방향 반전
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    # 캐릭터 이미지를 좌우로 반전하여 그리기
    if dir_x != 0:  # 이동 중일 때
        if dir_x > 0:  # 오른쪽 이동
            flip = False
        else:  # 왼쪽 이동 (좌우 반전)
            flip = True
        prev_flip = flip
    else:  # 이동 중이 아닐 때 이전 상태 유지
        flip = prev_flip

    if flip:  # 좌우 반전 상태에 따라 이미지 그리기
        character.clip_composite_draw(frame * 100, 0, 100, 100, 0, 'h', x, y, 120, 120)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x, y, 120, 120)

    update_canvas()
    handle_events()
    if not running:
        break

    # x 방향 이동
    if dir_x > 0:  # 오른쪽 이동
        if x + dir_x * 5 + character_width // 2 <= SCREEN_WIDTH:
            x += dir_x * 5
    elif dir_x < 0:  # 왼쪽 이동
        if x + dir_x * 5 - character_width // 2 >= 0:
            x += dir_x * 5

    # y 방향 이동
    if dir_y > 0:  # 위로 이동
        if y + dir_y * 5 + character_height // 2 <= SCREEN_HEIGHT:
            y += dir_y * 5
    elif dir_y < 0:  # 아래로 이동
        if y + dir_y * 5 - character_height // 2 >= 0:
            y += dir_y * 5

    frame = (frame + 1) % 16
    delay(0.1)

    if not running:
        break

close_canvas()
