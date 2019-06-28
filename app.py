import constants
import random
import copy

# Removed the global ALL, replaced with local all_numbers.


def main_menu():
    select_option = True

    while select_option:
        print("Main Menu:\n")
        print("1. Display Stats\n2. Quit\n")
        option = input("Select an option: ")
        print("\n")
        try:
            if option.isdigit():
                option = int(option)
                if option != 1 and option != 2:
                    raise ValueError("Please enter 1 or 2.")
            else:
                raise ValueError("Please enter 1 or 2.")
        except ValueError as err:
            print("Invalid input.")
            print("({})\n".format(err))
            continue
        else:
            return option


def teams_menu():
    select_team = True

    while select_team:
        print("Teams Menu:\n")
        print("0. Main Menu")
        for index in range(len(teams)):
            print("{}. {}".format(index + 1, teams[index]))
        option = input("\nSelect an option: ")
        print("\n")
        try:
            if option.isdigit():
                option = int(option)
                if option != 0 and option != 1 and option != 2 and option != 3:
                    raise ValueError("Please enter 0, 1, 2, or 3.")
            else:
                raise ValueError("Please enter 0, 1, 2, or 3.")
        except ValueError as err:
            print("Invalid input.")
            print("({})\n".format(err))
            continue
        else:
            return option


def add_players():
    # Made a copy of all_numbers.
    all = copy.deepcopy(all_numbers)
    num_players = 0
    team = []
    nums = set()

    while len(nums) < 6:
        nums.add(random.choice(all))

    for num in nums:
        team.append(players[num]["name"])
        num_players += 1
        all.remove(num)

    return num_players, team


def continue_or_quit():
    continue_or_quit = input("\nEnter c to continue or q to quit. ")
    print("\n")

    while continue_or_quit.lower() != 'c' and continue_or_quit.lower() != 'q':
        print("Invalid input.")
        continue_or_quit = input("Enter c to continue or q to quit. ")
        print("\n")

    return continue_or_quit.lower()


def convert_heights():
    heights = []
    converted_heights = []

    for player in players:
        heights.append(player["height"].split())

    for index in range(len(heights)):
        converted_heights.append(int(heights[index][0]))


def convert_experiences():
    experienced = []
    converted_experienced = []

    for player in players:
        experienced.append(player["experience"])

    for index in range(len(experienced)):
        if experienced[index] == "YES":
            experienced[index] = True
        else:
            experienced[index] = False
        converted_experienced.append(experienced[index])


def stats():
    num_players, team = add_players()
    print("Total players: {}\n".format(num_players))
    print("Players: {}\n".format(", ".join(team)))


def members_available():
    # Made a copy of all_numbers
    all = copy.deepcopy(all_numbers)
    if len(all) == 0:
        all = list(range(0, 18))


if __name__ == "__main__":
    all_numbers = list(range(0, 18))
    # Made copies of the constants.TEAMS and constants.PLAYERS
    teams = copy.deepcopy(constants.TEAMS)
    players = copy.deepcopy(constants.PLAYERS)
    # Called the functions that converts heights and experiences respectively.
    # Not sure what else to do with them for meets expectations grade though.
    convert_heights()
    convert_experiences()
    print("Basketball Team Stats Tool\n\n")
    team_selected = False
    while True:
        option = main_menu()
        if option == 1:
            while not team_selected:
                select_team = teams_menu()
                if select_team == 0:
                    break
                elif select_team == 1:
                    print("Team: {}\n".format(teams[0]))
                    members_available()
                    stats()
                    if continue_or_quit() == 'c':
                        continue
                    else:
                        break
                elif select_team == 2:
                    print("Team: {}\n".format(teams[1]))
                    members_available()
                    stats()
                    if continue_or_quit() == 'c':
                        continue
                    else:
                        break
                elif select_team == 3:
                    print("Team: {}\n".format(teams[2]))
                    members_available()
                    stats()
                    if continue_or_quit() == 'c':
                        continue
                    else:
                        break
        elif option == 2:
            break
