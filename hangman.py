def hangman(word):
    wrong = 0  # プレイヤー2が間違えた回数を保存
    stages = ["",
              "________        ",
              "|               ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
              ]
    rletters = list(word)  # wordの文字を1文字ずつの要素に分解してリストにする
    board = ["_"] * len(word)  # 文字列のリスト　プレイヤーに見せるヒント
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね："
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        # print("e={}".format(e))
        print("\n".join(stages[0:e]))
        print("wrong={}".format(wrong))
        print("len(stages)={}".format(len(stages)))
        if "_" not in board:
            print("貴方の勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))


hangman("cat")
