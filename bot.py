import random

random_responses = ["정말 흥미로운데, 더 말씀해 주세요.",
                    "알겠어요. 계속 이야기해 주세요.",
                    "왜 그런 말을 하시는 거죠?",
                    "요즘 날씨 정말 이상한 것 같죠?",
                    "주제를 바꿔볼까요?",
                    "어젯밤 경기 보셨어요?"]

print("안녕하세요, 저는 마빈입니다, 간단한 로봇입니다.")
print("언제든지 '잘가'를 입력하여 이 대화를 종료할 수 있습니다.")
print("각 답변을 입력한 후 '엔터'를 누르세요.")
print("오늘은 어떻게 지내세요?")

while True:
    user_input = input("> ")
    if user_input.lower() == "잘가":
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("대화해 주셔서 감사합니다, 안녕히 가세요!")
