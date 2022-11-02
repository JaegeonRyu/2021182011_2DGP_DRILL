from pico2d import *

# 이벤트 정의
RD, LD, RU, LU, TIMER = range(5)  # 0, 1, 2, 3

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYUP, SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT) : LU,
}

class SLEEP:
    # @staticmethod -> self 안만들어짐
    def enter(self, event):
        print('ENTER SLEEP')
        self.dir = 0
        pass

    def exit(self):
        print('EXIT SLEEP')
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8
        pass

    def draw(self):
        if self.face_dir == 1: # 오른쪽을 바라보고 있는 상태
            self.image.composite_draw(self.frame * 100, 300, 100, 100,
                                        3.141592/2, '',
                                        self.x - 25, self.y - 25, 100, 100)
        else:
            self.image.composite_draw(self.frame * 100, 200, 100, 100,
                                        -3.141592/2, '',
                                        self.x + 25, self.y - 25, 100, 100)
        pass

# 클래스를 이용해 상태 구현
class IDLE:
    # @staticmethod -> self 안만들어짐
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0
        #타이머 설정
        self.timer = 1000
        pass

    def exit(self):
        print('EXIT IDLE')
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0: # 시간 경과 시
            # 이벤트 발생 TIMER
            #self.q.insert(0, TIMER) # 객체 지향 프로그래밍에 위배, q를 직접 엑세스 하고 있으니까...
            self.add_event(TIMER)
        pass

    def draw(self):
        if self.face_dir == 1: # 오른쪽을 바라보고 있는 상태
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        pass

class RUN:
    #@staticmethod -> self 안만들어짐
    def enter(self, event):
        print('ENTER RUN')
        #self.dir 결정해야함
        if event == RD: self.dir += 1
        elif event == LD: self.dir -= 1
        elif event == RU: self.dir -= 1
        elif event == LU: self.dir += 1
        pass

    def exit(self):
        print('EXIT RUN')
        # run을 나가서, idle로 갈떄 run의 방향을 알려줘야함
        self.face.dir = self.dir
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x ,800)
        pass

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        pass

next_state = {
    SLEEP: {RU: RUN, LD: RUN, RD: RUN,LU: RUN, SLEEP: SLEEP},
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP},
    RUN: {RU: IDLE, LU: IDLE, LD: IDLE, RD: IDLE}
}

class Boy:

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event): # 소년 스스로 이벤트를 처리할수 있게
        # event 는 키 이벤트, 내부 RD 등으로 변환
        if (event.type, event.key ) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event) # 변환된 내부 이벤트를 큐에 추가)

        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.q: # 큐에 뭔가 들어 있다면
            event = self.q.pop() # 이벤트 가져와
            self.cur_state.exit() # 현재 상태를 나가고
            self.cur_state = next_state[self.cur_state][event] # 다음 상태 계산
            self.cur_state.enter(self, event)

        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)

        # if self.dir == -1:
        #     self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        # elif self.dir == 1:
        #     self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        # else:
        #     if self.face_dir == 1:
        #         self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        #     else:
        #         self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
