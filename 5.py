#MyMagic8Ball

import random

ans1 = "참치!"
ans2 = "콘치즈!"
ans3 = "돌돔구이"
ans4 = "홍어"
ans5 = "우럭"
ans6 = "광어회!"
ans7 =  "오징어물회"
ans8 = "홍합탕"

print("MyMagic8Ball에 오신 것을 환영합니다.")

#사용자의 질문 얻기
question = input("뭘 먹을지 결정장애가 왔다면 질문을 입력하고 엔터키를 누르세요")

print("고민중...\n"*4)

#질문에 맞는 답변을 하는 일에 radint()함수 활용하기!
choice=random.randint(1,8)
if choice==1:
      answer=ans1
elif choice==2:
      answer=ans2
elif choice==3:
      answer=ans3
elif choice==4:
      answer=ans4
elif choice==5:
      answer=ans5
elif choice==6:
      answer=ans6
elif choice==7:
      answer=ans7
else:
      answer==ans8

print(answer)

input("\n\n마치려면 엔터키를 누르세요.")
