print("생기부 강점 분석 프로그램")

major = input("희망 학과 입력: ")
activity = input("생기부 활동 입력: ")

strength = []
weakness = []

if "프로젝트" in activity:
    strength.append("실전 문제 해결 역량")

if "탐구" in activity:
    strength.append("학업 탐구 역량")

if "발표" not in activity:
    weakness.append("발표 및 의사소통 경험 부족")

print("\n[분석 결과]")

print("\n강점:")
for s in strength:
    print("-", s)

print("\n보완점:")
for w in weakness:
    print("-", w)
