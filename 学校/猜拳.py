import random


def get_computer_choice():
    return random.choice(['石头', '剪刀', '布'])


def determine_winner(player, computer):
    if player == computer:
        return "平局"
    elif (player == '石头' and computer == '剪刀') or \
            (player == '剪刀' and computer == '布') or \
            (player == '布' and computer == '石头'):
        return "玩家胜利"
    else:
        return "电脑胜利"


def play_game():
    player_wins = 0
    computer_wins = 0

    while player_wins < 2 and computer_wins < 2:
        player_input = input("请输入（1: 石头 / 2: 剪刀 / 3: 布）：")

        if player_input == '1':
            player_choice = '石头'
        elif player_input == '2':
            player_choice = '剪刀'
        elif player_input == '3':
            player_choice = '布'
        else:
            print("无效输入，请输入 1、2 或 3。")
            continue

        computer_choice = get_computer_choice()
        print(f"电脑出: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "玩家胜利":
            player_wins += 1
        elif result == "电脑胜利":
            computer_wins += 1

    if player_wins == 2:
        print("玩家最终胜利！")
    else:
        print("电脑最终胜利！")


play_game()
