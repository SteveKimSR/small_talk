from flask import Flask, jsonify, request, json
from flask_cors import CORS
import main

app = Flask('app')
CORS(app)


'''
user_input_data example
    self.region = '서울'
    self.gender = 'male'
    self.age = 25
    self.departure_time = 19  # 출발시각
    self.arrival_time = 22  # 도착시각
    self.msg = '저녁파티에 가는데 너무 눈에 띄지 않지만 단정하고 예의 있는 느낌을 주지만 동시에 최신 패션 트렌드를 반영하고, 편안함과 실용성을 모두 갖춘 스타일의 옷'
'''


class user_input_data:
    def __init__(self, d=None):
        if d is not None:
            for key, value in d.items():
                setattr(self, key, value)


@app.route('/')
def hello():
    return 'Hello BumJun!'


@app.route('/submit', methods=['POST'])
def submit():
    data = request.json

    ui = user_input_data(data)

    pictures = main.clothes_recommendation_app(ui)

    return jsonify({'status': 'success', 'data': data})


if __name__ == "__main__":
    app.run(debug=True)
