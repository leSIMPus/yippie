import random

def deal_card():
    return random.randint(2, 11)

def calc_score(hand):
    return sum(hand)

def show_hands(player, dealer, reveal_dealer=False):
    print(f"\nТвои карты: {player} | Сумма: {calc_score(player)}")
    if reveal_dealer:
        print(f"Карты дилера: {dealer} | Сумма: {calc_score(dealer)}")
    else:
        print(f"Первая карта дилера: {dealer[0]}")

def game():
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    game_over = False

    show_hands(player_hand, dealer_hand)

    while True:
        choice = input("\nХочешь взять карту? (Да/Нет): ").capitalize()
        if choice == "Да":
            player_hand.append(deal_card())
            show_hands(player_hand, dealer_hand)
            if calc_score(player_hand) > 21:
                print("\nПеребор. Вы проиграли.")
                game_over = True
                break
        else:
            break

    if not game_over:
        print("\nХод дилера...")
        while calc_score(dealer_hand) < 17:
            dealer_hand.append(deal_card())

        show_hands(player_hand, dealer_hand, reveal_dealer=True)

        player_score = calc_score(player_hand)
        dealer_score = calc_score(dealer_hand)

        if dealer_score > 21:
            print("\nУ дилера перебор. Вы выиграли.")
        elif dealer_score == player_score:
            print("\nНичья.")
        elif player_score > dealer_score:
            print("\nВы ближе к 21. Вы выиграли")
        else:
            print("\nДилер выиграл.")

while True:
        game()
        again = input("Хотите сыграть снова? (Да/Нет): ").capitalize()
        if again != "Да":
            print("До новых встреч.")
            break