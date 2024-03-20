#   _____                                       _____               _             
#  | ____|_  ___ __   ___ _ __  ___  ___  ___  |_   _| __ __ _  ___| | _____ _ __ 
#  |  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \/ __|   | || '__/ _` |/ __| |/ / _ \ '__|
#  | |___ >  <| |_) |  __/ | | \__ \  __/\__ \   | || | | (_| | (__|   <  __/ |   
#  |_____/_/\_\ .__/ \___|_| |_|___/\___||___/   |_||_|  \__,_|\___|_|\_\___|_|   
#             |_|                                                                 

#
# Uzdevums:
# Uzrakstīt programmu, kas ļauj
# - ievadīt izdevumus: nosaukumu, summu un kategoriju
# - atspoguļot uz ekrāna visus izdevumus
# - iespēja atlasīt 10 lielākus izdevumus
# - iespēja atlasīt 10 mazākus izdevumus
# - iespēja apskatīt vidējo izdevumu summu
# [!] Programmai jaglabā izdevumu stāvokli kad programma ir izslēgta palaista no jauna
#

expenses = []


# load expenses from expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Python read JSON file)
pass

while True:
    command = input("\nChoose command:")
    if command == "1":
        izd_nos = str(input("Ievadiet izdevuma nosaukumu"))
        izd_sum = str(input("Ievadiet izdevuma summu"))
        izd_kat = str(input("Ievadiet izdevuma kategoriju"))
        x = {
        "nosaukums": izd_nos,
        "summa": izd_sum,
        "kategorija": izd_kat,
        }
        expenses.append(x)
        pass
    if command == "2":
        print(izd_nos, izd_sum, izd_kat)
        pass
    if command == "3":
          def sorting(izd_liel):

            return int(izd_liel["summa"])

    expenses.sort(key = sorting, reverse = True)
    
    print(expenses[0:10])
    pass
    if command == "4":
        def sorting(izd_maz):

            return int(izd_maz["summa"])

    expenses.sort(key = sorting)
    
    print(expenses[0:10])
    pass
if command == "5": 

    if command == "e":
        print("Exiting...")
        break

# save expenses to expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Writing JSON to a file in Python)
pass
