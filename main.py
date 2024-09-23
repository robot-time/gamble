import random, time, math, os

from sys import stdout

from colorama import Fore, init

init(autoreset=True)

money = 100

menu_seen = False

rGamble = "no"

rRoulette = 0

user = input("who are you? ")

achievement = [
  "LOCKED",
  "LOCKED",
  "LOCKED",
  "LOCKED",
  "LOCKED",
  "LOCKED",
  "LOCKED",
  "LOCKED",
  "LOCKED",
  "LOCKED",
  "LOCKED",
  "LOCKED",
  "LOCKED",
]

unlucky_gerat = 0

lucky_gerat = 0

debt = 0

bet_speed = None

legal_action = 0


def main_menu():

  global menu_seen, money, debt, start_time

  if menu_seen == False:

    print(Fore.CYAN + "\nWelcome to the casino!")

    load()

    menu_seen = True

  elif debt != 0:

    if money <= 0:

      os.remove(user + ".txt")

      print(Fore.RED + "\nyou lose\n\n")

      quit()

    else:

      elapsed_time = time.time() - start_time

      if elapsed_time > 30:

        start_time = time.time()

        debt += math.ceil(debt / 10)

  else:

    print(Fore.CYAN + "\nWelcome back!")

  save()

  if (user.lower() == "gerat" or user.lower() == "lucky gerat"
      or user.lower() == "unlucky gerat") and achievement[5] != "UNLOCKED":

    achievement[5] = "UNLOCKED"

    print(Fore.YELLOW + "\nAchievement unlocked: Ascension! ")

    money += 400

  print("\nYou have " + str(money) + "$")

  while True:

    print("\n1. GAMBLE")

    print("2. ROULETTE")

    print("3. ACHIEVEMENTS")

    print("4. BANK")

    print("5. QUIZ (unfinished)")

    print("6. LEAVE")

    mChoice = str(input("\nWhat would you like to do? ")).lower()

    if "1" in mChoice or "gamble" in mChoice:

      gambling()

    elif "2" in mChoice or "roulette" in mChoice:

      if achievement[6] == "UNLOCKED":

        roulette()

      else:

        print(Fore.RED + "\nRoulette must be unlocked! ")

    elif "3" in mChoice or "achievements" in mChoice:

      achievements()

    elif "4" in mChoice or "bank" in mChoice:

      bank()

    elif "5" in mChoice or "quiz" in mChoice:

      challenge_fee = str(input("Pay the 250$ fee to play the quiz? ")).lower()

      if challenge_fee == "yes":

        money -= 250

        save()

        if achievement[8] != "UNLOCKED":

          print(Fore.YELLOW + "\nAchievement Unlocked: Quiz Time! ")

          achievement[8] = "UNLOCKED"

        challenge()

    elif "6" in mChoice or "leave" in mChoice:

      save()

      quit()

    else:

      print("\nshut up", user)

      continue


def gambling():

  global money, rGamble, unlucky_gerat, lucky_gerat, debt, start_time, legal_action

  print("\nenter 'leave' into the bet amount to go back to menu")

  while True:

    if (achievement[1] == "IN PROGRESS"
        and money == 250) and achievement[1] != "UNLOCKED":

      achievement[1] = "UNLOCKED"

      print(Fore.YELLOW + "\nAchievement unlocked : Saved! ")

    elif money == 1:

      achievement[1] = "IN PROGRESS"

    if money >= 1500 and achievement[6] != "UNLOCKED":

      achievement[6] = "UNLOCKED"

      print(Fore.YELLOW + "\nAchievement unlocked: Spin the Wheel!")

    if money <= 0:

      print("\n0$")

      print(Fore.RED + "\nbroke")

      main_menu()

    if achievement[0] != "UNLOCKED" and money >= 1000:

      print(Fore.YELLOW + "\nAchievement unlocked : Rapidgamble!")

      print(Fore.GREEN + "\nuse code rapidgamble to activate")

      achievement[0] = "UNLOCKED"

    print("\n" + str(money) + "$")

    while True:

      if rGamble == "no":

        gamble = input("\nBet how much? ")

        if gamble.lower() == "leave":

          main_menu()

        if gamble.lower() != "rapidgamble":

          try:

            gamble = int(gamble)

            if gamble > money or gamble <= 0:

              raise ValueError

            else:

              break

          except ValueError:

            print("\nshut up", user)

            continue

        if gamble.lower() == "rapidgamble" and achievement[0] == "UNLOCKED":

          rGamble = input("\nWould you like to enable RapidGamble? ").lower()

          if rGamble == "yes":

            while True:

              try:

                rAmount = int(input("\nHow much should it bet each time? "))

                rDelay = int(input("Delay between each bet? "))

                rTimes = int(input("How many times should it bet? "))

                if rAmount > 0 and rAmount <= money and rDelay >= 0 and rTimes > 0:

                  gamble = rAmount

                  break

                else:

                  raise ValueError

              except ValueError:

                print("\nshut up", user)

                continue

          elif rGamble == "no":

            continue

          else:

            print("\nshut up", user)

            rGamble = "no"

            continue

        elif gamble >= 500 and achievement[4] != "UNLOCKED":

          achievement[4] = "UNLOCKED"

          print(Fore.YELLOW + "\nAchievement unlocked: High Roller!")

      elif rGamble == "yes":

        break

    chance = random.randint(1, 10)

    if rGamble == "yes":

      time.sleep(rDelay)

      rTimes -= 1

      if rTimes == 0:

        rGamble = "no"

    if chance <= 7:

      print(Fore.RED + "\nLose")

      money -= gamble

      if achievement[3] != "UNLOCKED":

        lucky_gerat = 0

        achievement[3] = "LOCKED"

      unlucky_gerat += 1

      if unlucky_gerat == 10 and achievement[2] != "UNLOCKED":

        achievement[2] = "UNLOCKED"

        print(Fore.YELLOW + "\nAchievement unlocked: Unlucky Gerat! ")

      elif unlucky_gerat > 0 and achievement[2] != "UNLOCKED":

        achievement[2] = "IN PROGRESS"

    elif chance == 10:

      print(Fore.MAGENTA + "\nBig win")

      money += (gamble * 3)

      if achievement[2] != "UNLOCKED":

        unlucky_gerat = 0

        achievement[2] = "LOCKED"

      lucky_gerat += 1

      if lucky_gerat == 5 and achievement[3] != "UNLOCKED":

        achievement[3] = "UNLOCKED"

        print(Fore.YELLOW + "\nAchievement unlocked: Lucky Gerat!")

      elif lucky_gerat > 0 and achievement[3] != "UNLOCKED":

        achievement[3] = "IN PROGRESS"

    else:

      print(Fore.GREEN + "\nWin")

      if achievement[2] != "UNLOCKED":

        unlucky_gerat = 0

        achievement[2] = "LOCKED"

      money += (gamble * 2)

      lucky_gerat += 1

      if lucky_gerat == 5 and achievement[3] != "UNLOCKED":

        achievement[3] = "UNLOCKED"

        print(Fore.YELLOW + "\nAchievement unlocked: Lucky Gerat!")

      elif lucky_gerat > 0 and achievement[3] != "UNLOCKED":

        achievement[3] = "IN PROGRESS"

    if debt != 0:

      elapsed_time = time.time() - start_time

      legal_action += 1

      if legal_action == 50:

        print(Fore.RED + "\nWarning: Debt must be repaid within 50 gambles! ")

      elif legal_action == 100:

        legal_action = 0

        print(Fore.RED + "\nDebt not paid. You have been sued for", (debt * 5),
              "$")

        money -= debt * 5

      elif legal_action == 75:

        print(Fore.RED + "\nWarning: Debt must be repaid within 25 gambles! ")

      elif legal_action == 90:

        print(Fore.RED + "\nWarning: Debt must be repaid within 10 gambles! ")

      elif legal_action > 90:

        print(Fore.RED + "\nWarning: Debt must be repaid within " +
              str(100 - legal_action) + " gambles! ")

      if elapsed_time > 30:

        start_time = time.time()

        debt += math.ceil(debt / 10)

    save()


def roulette():

  global money, rRoulette, gamble, bet_speed, legal_action, debt

  print(Fore.RED + "\nnote: most achievements are unavailable in roulette")

  while True:

    if money <= 0:

      print(Fore.RED + "Broke")

      main_menu()

    end_time = time.time()

    if bet_speed != None:

      if (end_time - bet_speed) < 3 and achievement[7] != "UNLOCKED":

        achievement[7] = "UNLOCKED"

        print(Fore.YELLOW + "\nAchievement unlocked: Time Effiency!")

        print(Fore.GREEN + "\nUse code 'rapidroulette' to activate it")

    print("\n" + str(money) + "$")

    while True:

      if rRoulette != 2:

        gamble = input("\nBet how much? ")

        if gamble.lower() == "leave":

          main_menu()

        elif gamble.lower() == "rapidroulette":

          print(Fore.GREEN + "\nRapidRoulette Activated! ")

          rRoulette = 1

          continue

        else:

          try:

            gamble = int(gamble)

            if gamble > money or gamble <= 0:

              raise ValueError

          except ValueError:

            print("\nshut up", user)

            continue

        bet_speed = time.time()

        while True:

          gamble_type = input("\nBet on a number or a colour? ").lower()

          if gamble_type == "colour":

            colour = input("\nWhat colour? (Red or Black) ").lower()

            number = None

            if colour != "black" and colour != "red":

              print("\nshut up", user)

              continue

            else:

              if rRoulette == 1:

                rRoulette = 2

                try:

                  rDelay = int(input("Delay between each bet? "))

                  rTimes = int(input("How many times should it bet? "))

                  if rDelay >= 0 and rTimes > 0:

                    break

                  else:

                    raise ValueError

                except ValueError:

                  print("\nshut up", user)

                  continue

              else:

                break

          elif gamble_type == "number":

            number = input("\nWhat number? (0 - 36) ")

            colour = None

            try:

              number = int(number)

              if number > 36 or number < 0:

                raise ValueError

              else:

                if rRoulette == 1:

                  rRoulette = 2

                  try:

                    rDelay = int(input("Delay between each bet? "))

                    rTimes = int(input("How many times should it bet? "))

                    if rDelay >= 0 and rTimes > 0:

                      break

                    else:

                      raise ValueError

                  except ValueError:

                    print("shut up", user)

                else:

                  break

            except ValueError:

              print("\nshut up", user)

              continue

          else:

            print("\nshut up", user)

            continue

        break

      else:

        break

    chance = random.randint(0, 36)

    if rRoulette == 2:

      time.sleep(rDelay)

      rTimes -= 1

      if rTimes == 0:

        rRoulette = 0

    if chance == 0:

      print("\nThe ball landed on 0 (green)!")

      if number == 0:

        print(Fore.GREEN + "\nWin!")

        money += gamble * 35

      else:

        print(Fore.RED + "\nLose")

        money -= gamble

    elif chance % 2 == 0:

      print("\nThe ball landed on", chance, "(black)!")

      if colour == "black":

        money += gamble * 2

        print(Fore.GREEN + "\nWin!")

      elif number == chance:

        money += gamble * 35

        print(Fore.MAGENTA + "\nBig win!")

      else:

        print(Fore.RED + "\nLose")

        money -= gamble

    else:

      print("\nThe ball landed on", chance, "(red)!")

      if colour == "red":

        money += gamble * 2

        print(Fore.GREEN + "\nWin!")

      elif number == chance:

        money += gamble * 35

        print(Fore.MAGENTA + "\nBig win!")

      else:

        print(Fore.RED + "\nLose")

        money -= gamble

    if debt != 0:

      legal_action += 1

      if legal_action == 50:

        print(Fore.RED + "\nWarning: Debt must be repaid within 50 gambles! ")

      elif legal_action == 100:

        legal_action = 0

        print(Fore.RED + "\nDebt not paid. You have been sued for", (debt * 5),
              "$")

        money -= debt * 5

      elif legal_action == 75:

        print(Fore.RED + "\nWarning: Debt must be repaid within 25 gambles! ")

      elif legal_action == 90:

        print(Fore.RED + "\nWarning: Debt must be repaid within 10 gambles! ")

      elif legal_action > 90:

        print(Fore.RED + "\nWarning: Debt must be repaid within " +
              str(100 - legal_action) + " gambles! ")

      elapsed_time = time.time() - start_time

      if elapsed_time > 30:

        start_time = time.time()

        debt += math.ceil(debt / 10)

    save()


def challenge():

  dash_amount = 15

  dashes = True

  print(
    Fore.GREEN +
    "\nAnswer all questions correctly within the time limit to unlock Roulette! \n"
  )

  while dashes:

    dashes = "-" * dash_amount

    stdout.write("\r" + " " * 16 + "|" + "\r|" + "-" * dash_amount)

    stdout.flush()

    time.sleep(1)

    dash_amount -= 1

  print(Fore.RED + "\n\nRan out of time")

  if achievement[9] != "UNLOCKED":

    print(Fore.YELLOW + "\nAchievement Unlocked: So Close! ")

    achievement[9] = "UNLOCKED"


def achievements():

  print("ACHIEVEMENTS:")

  if achievement == [
      "UNLOCKED", "UNLOCKED", "UNLOCKED", "UNLOCKED", "UNLOCKED", "UNLOCKED",
      "UNLOCKED", "UNLOCKED", "UNLOCKED", "UNLOCKED", "UNLOCKED", "UNLOCKED",
      "LOCKED"
  ]:

    achievement[12] = "UNLOCKED"

    print(Fore.YELLOW + "Achievement unlocked: Completionist!")

  print("\nSuperspeed : Unlock Rapidgamble! (" + achievement[0] + ")")

  print("\nSaved : Go from 1$ to 250$! (" + achievement[1] + ")")

  print("\nUnlucky Gerat: Get a bad luck streak! (" + achievement[2] + ")")

  print("\nLucky Gerat: Get a good luck streak! (" + achievement[3] + ")")

  print("\nHigh Roller: Bet more than 500$ at a single time! (" +
        achievement[4] + ")")

  print("\nAscension: Become the one and only. (" + achievement[5] + ")")

  print("\nSpin the Wheel : Unlock Roulette! (" + achievement[6] + ")")

  print("\nTime Efficiency: Unlock RapidRoulette! (" + achievement[7] + ")")

  print("\nQuiz Time: Play the quiz for the first time! (" + achievement[8] +
        ")")

  print("\nSo Close: Come close to winning the quiz! (" + achievement[9] + ")")

  print("\nBanking on Success: Take out your first loan! (" + achievement[10] +
        ")")

  print("\nDebts Paid: Pay back all of your loans! (" + achievement[11] + ")")

  print("\nCompletionist: Complete every achievement! (" + achievement[12] +
        ")")


def save():

  try:

    data = [
      user, "\n",
      str(money), "\n",
      str(achievement), "\n",
      str(debt), "\n",
      str(legal_action)
    ]

    with open(user + ".txt", "w+") as file:

      file.writelines(data)

  except FileNotFoundError:

    with open(user + ".txt", "w") as file:

      print("\nFile created successfully")

      save()


def load():

  global money, achievement, user, debt, start_time, legal_action

  try:

    with open(user + ".txt", "r+") as file:

      if user.lower() == file.readline().strip().lower():

        print("\nFile loaded successfully! ")

        try:

          money = int(file.readline().strip())

          achievement = eval(file.readline().strip())

          debt = int(file.readline().strip())

          legal_action = int(file.readline().strip())

          if debt != 0:

            start_time = time.time()

        except ValueError:

          print("file data invalid")

  except FileNotFoundError:

    with open(user + ".txt", "w") as file:

      print("\nfile created")

      save()

  except OSError:

    print("\ninvalid username")

    user = input("\nWho are you? ")

    load()


def bank():

  global money, debt, start_time

  if debt == 0:

    loan = input("\nWould you like to take out a loan? ").lower()

    if "yes" in loan.lower():

      loan = input("\nHow much do you want to take out (Up to 500$)? ")

      try:

        loan = int(loan)

        if loan <= 0 or loan > 500:

          raise ValueError

        else:

          money += loan

          debt = loan

          print(Fore.YELLOW + "\nTook out " + str(loan) + "$ successfully!")

          print(Fore.RED + "\nPay the loan back within 100 gambles.")

          if achievement[11] != "UNLOCKED":

            print(Fore.YELLOW + "\nAchievement Unlocked: Banking on Success! ")

            achievement[11] = "UNLOCKED"

          start_time = time.time()

          save()

      except ValueError:

        print("\nshut up", user)

        bank()

    else:

      main_menu()

  else:

    loan = input("\nWould you like to pay back your loan? ").lower()

    if "yes" in loan.lower():

      loan = input("\nHow much do you want to pay back (Up to " + str(debt) +
                   ")? ")

      try:

        loan = int(loan)

        if loan > debt or loan <= 0:

          raise ValueError

        else:

          money -= loan

          debt -= loan

          print(Fore.YELLOW + "\nPayed back " + str(loan) + "$ successfully!")

          if debt == 0:

            if achievement[10] != "UNLOCKED":

              print(Fore.YELLOW + "\nAchievement Unlocked: Debts Paid! ")

              achievement[10] = "UNLOCKED"

          save()

      except ValueError:

        print("\nshut up", user)

        bank()

    else:

      main_menu()


main_menu()
