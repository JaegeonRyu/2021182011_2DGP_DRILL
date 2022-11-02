table = {
"SLEEP": {"HIT": "WAKE"},
"WAKE": {"TIMER10": "SLEEP"}
}

cur_state = "SLEEP"
next_state = table[cur_state]["HIT"]



# class Player:
#     name = "Player"
#
#     def __init__(self):
#         self.x = 100
#
#     def where(self):
#         print(self.x)
#
# player = Player()
# player.where()
#
# print(Player.name) # 클래스 변수 출력
# print(player.name) # name이라는 객체 변수가 없으면, 같은 이름의 클래스 변수가 선택
#
# Player.where(player) # 이게 원칙적인 파이썬에서 멤버 함수 호출
# player.where() # Player.where(player) 이것과 동일