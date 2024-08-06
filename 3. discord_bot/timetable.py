# 필요한거 가져오는 식으로
import time


class LostArk_Schedule:
    def __init__(self, time='20:00', raid='발탄', difficulty='노말', leader='려리 바드', participants='', note='비고 : '):
        self.time = time  # 20:00
        self.raid = raid  # 에기르
        self.difficulty = difficulty  # 노말
        self.leader = leader  # 공대장 / 직업
        self.participants = participants  # 지원자 / 직업
        self.note = note  # 비고 :

    def __lt__(self, other):
        return self.time < other.time


class TimeTable:
    def __init__(self):
        self.days = {
            '월': [],
            '화': [],
            '수': [],
            '목': [],
            '금': [],
            '토': [],
            '일': []
        }

    def create_schedule(self, day, schedule):
        if day in self.days.keys():
            self.days[day].append(schedule)
            # 어디다가 반영해라 ->
        else:
            print("유효한 요일이 아닙니다")

    def get_schedule(self, day):
        if day in self.days:
            return sorted(self.days[day])


schedule1 = LostArk_Schedule('20:00')
schedule2 = LostArk_Schedule('18:00')
schedule3 = LostArk_Schedule('22:00')

timetable = TimeTable()
timetable.create_schedule('월', schedule1)
timetable.create_schedule('월', schedule2)
timetable.create_schedule('월', schedule3)

temp = timetable.get_schedule('월')
print(temp)
