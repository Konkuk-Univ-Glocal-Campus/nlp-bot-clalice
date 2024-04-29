# import random

# # This list contains the random responses (you can add your own or translate them into your own language too)
# random_responses = ["That is quite interesting, please tell me more.",
#                     "I see. Do go on.",
#                     "Why do you say that?",
#                     "Funny weather we've been having, isn't it?",
#                     "Let's change the subject.",
#                     "Did you catch the game last night?"]

# print("Hello, I am Marvin, the simple robot.")
# print("You can end this conversation at any time by typing 'bye'")
# print("After typing each answer, press 'enter'")
# print("How are you today?")

# while True:
#     # wait for the user to enter some text
#     user_input = input("> ")
#     if user_input.lower() == "bye":
#         # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
#         break
#     else:
#         response = random.choices(random_responses)[0]
#     print(response)

# print("It was nice talking to you, goodbye!")


import random

# 이 리스트에는 랜덤 응답이 포함되어 있습니다 (원하는 대로 추가하거나 직접 번역할 수도 있습니다)
random_responses = ["정말 흥미로운데, 더 말씀해 주세요.",
                    "알겠어요. 계속 이야기해 주세요.",
                    "왜 그런 말을 하시는 거죠?",
                    "요즘 날씨 정말 이상한 것 같죠?",
                    "주제를 바꿔볼까요?",
                    "어젯밤 경기 보셨어요?"]

print("안녕하세요, 저는 Marvin이라고 합니다, 간단한 로봇입니다.")
print("언제든지 '잘가'를 입력하여 이 대화를 종료할 수 있습니다.")
print("각 답변을 입력한 후 '엔터'를 누르세요.")
print("오늘은 어떻게 지내세요?")

while True:
    # 사용자가 텍스트를 입력할 때까지 대기합니다.
    user_input = input("> ")
    if user_input.lower() == "잘가":
        # 사용자가 '잘가'를 입력하면 루프를 빠져 나옵니다.
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("대화해 주셔서 감사합니다, 안녕히 가세요!")
