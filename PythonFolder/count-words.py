# 単語の出現回数をカウント
# page 108
text = """
Keep on asking, and it will be given you;
keep on seeking, and you will find;
keep on knocking, and it will be opened to you;
for everyone asking receives, and everyone seeking finds,
and to everyone knocking, it will be opened.
"""

# 単語を区切る
text = text.replace(";", "")    # ;を削除
text = text.replace(",", "")    # ,を削除
text = text.replace(".", "")    # .を削除
words = text.split()    # 空白で区切ってリスト型を作成

# 単語を数える
counter = {}
for w in words:
    ws = w.lower()  # 小文字に変換
    if ws in counter:   # もし辞書型にすでにキーがあれば値を１つ追加
        counter[ws] += 1
    else:
        counter[ws] = 1     # もし辞書型にキーがなければ、値を１としてキーも登録

# 結果を表示 ３回以上出現した単語と回数を表示
for k, v in sorted(counter.items()):    # counterのキーをアルファベット順として範囲に指定
    if v >= 3:
        print(k, v)
