import naver
import ask_gpt
import ask_dalle


def clothes_recommendation_app(user_input):
    # 날씨 가져오기
    daily_temperature = naver.get_minmax_temperature(user_input)

    # gpt.요구사항 전달
    recommended_clothings = ask_gpt.gpt(user_input, daily_temperature)

    # dalle.옷추천이미지 생성
    ask_dalle.dalle(user_input, recommended_clothings)
