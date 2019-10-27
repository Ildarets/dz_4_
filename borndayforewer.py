def game(answer_gamer, true_answer, answer):
    while answer_gamer != true_answer:
        print("Не верно!")
        answer_gamer = input(answer)
    print("Верно!")