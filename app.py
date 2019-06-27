import constants
import random

ALL = list(range(0, 18))


def main_menu():
    select_option = True

    while select_option:
        print("Main Menu:\n")
        print("1. Display stats\n2. Quit\n")
        option = input("Select an option: ")
        print("\n")
        try:
            if option.isdigit() is True:
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
        for index in range(len(constants.TEAMS)):
            print("{}. {}".format(index + 1, constants.TEAMS[index]))
        option = input("\nSelect a team, or enter 0 to quit to the main menu: ")
        print("\n")
        try:
            if option.isdigit() is True:
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


def teams():
    num_players = 0
    team = []
    nums = set()

    while len(nums) < 6:
        nums.add(random.choice(ALL))

    for num in nums:
        team.append(constants.PLAYERS[num]["name"])
        num_players += 1
        ALL.remove(num)

    return num_players, team


def continue_or_quit():
    continue_or_quit = input("\nEnter c to continue or q to quit. ")
    print("\n")

    while continue_or_quit.lower() != 'c' and continue_or_quit.lower() != 'q':
        print("Invalid input.")
        continue_or_quit = input("Enter c to continue or q to quit. ")
        print("\n")

    return continue_or_quit.lower()


def convert_height():
    heights = []
    converted_heights = []

    for player in constants.PLAYERS:
        heights.append(player["height"].split())

    for index in range(len(heights)):
        converted_heights.append(int(heights[index][0]))


def convert_experience():
    experienced = []
    converted_experienced = []

    for player in constants.PLAYERS:
        experienced.append(player["experience"])

    for index in range(len(experienced)):
        if experienced[index] == "YES":
            experienced[index] = True
        else:
            experienced[index] = False
        converted_experienced.append(experienced[index])


def stats():
    num_players, team = teams()
    print("Total players: {}\n".format(num_players))
    print("Players: {}\n".format(", ".join(team)))


def members_available():
    global ALL
    members_available = True

    if len(ALL) == 0:
        members_available = False

    if not members_available:
        ALL = list(range(0, 18))


if __name__ == "__main__":
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
                    print("Team: {}\n".format(constants.TEAMS[0]))
                    members_available()
                    stats()
                    if continue_or_quit() == 'c':
                        continue
                    else:
                        break
                elif select_team == 2:
                    print("Team: {}\n".format(constants.TEAMS[1]))
                    members_available()
                    stats()
                    if continue_or_quit() == 'c':
                        continue
                    else:
                        break
                elif select_team == 3:
                    print("Team: {}\n".format(constants.TEAMS[2]))
                    members_available()
                    stats()
                    if continue_or_quit() == 'c':
                        continue
                    else:
                        break
        elif option == 2:
            break
