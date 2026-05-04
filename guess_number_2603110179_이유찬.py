# 1. 컴퓨터가 숫자를 생각한다.(1~50)
# 2. 사용자 숫자를 말한다.
# 3. 숫자가 맞으면 사용자 win
# 4. 틀리면 컴퓨터가 up, down을 알려준다.
# 5. 2~4번까지 7번 반복
# 6. 7번 내에 맞추지 못하면 computer win

import random
limit = 100

def random_number():
    print("1~limit까지의 숫자 맞추기")