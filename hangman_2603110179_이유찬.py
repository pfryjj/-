import random
# 자료 구조

#
def select_word():
    word_list = ['apple', 'banan', 'man', 'woman', 'tomato']
    return random.choice(word_list)
# 게임 로직
# 1. com이 단어 선택하여 보여주기
target_word = "MAN"
blank_char = '_'
word_screen = '_' * len(target_word)
print(">> 컴퓨터가 생각한 단어 :", target_word)

# 2. 사용자 알파벳 입력

limit_error = 7
num_error = 0
while num_error < limit_error: 
    # 사용자 알파벳 입력
    user_input = input(">> 알파벳 입력 : ").upper()

    # 3. 게임 상태 업데이트
    # 알파벳이 단어에 있으면 채워주기
    if target_word.find(user_input) == -1:
        num_error += 1 # 오답 횟수 먼저 증가
        print(f'오답 : {num_error}회')
    else: 
        for i in range(len(target_word)):
            if target_word[i] == user_input:
                # 수정한 부분: 새로 만든 문자열을 word_screen에 재할당
                word_screen = word_screen[:i] + user_input + word_screen[i+1:]
        print('정답 :', word_screen)
    # 없으면 오류 횟수 증가

    # 4. 단어를 다 맞췄으면(word_screen에 _가 없으면) 사용자 win
    if word_screen.count(blank_char) == 0:
        print('You win ~~~~ !!!')
        break

# 5. 시도횟수가 7번이 넘었으면 loose 
if num_error >= limit_error:
    print('You loose ... :', target_word)