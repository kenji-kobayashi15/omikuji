import random
from unittest import result

omikuji = ["大吉", "吉", "小吉", "中吉", "凶"]  # 結果リストをまとめて定義する

# index = random.randint(0, len(omikuji) - 1)
# result = omikuji[index]  # ランダムに1つ取得するのはちょっと難しそうだ
result = random.choice(omikuji)

print(f"今日の運勢は... {result}")  # これは簡単
