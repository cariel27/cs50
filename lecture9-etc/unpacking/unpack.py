def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print("**List UNPACKING**")
print(total(*coins), "Knuts")
print(total(galleons=100, sickles=50, knuts=25), "Knuts")

print("**Dictionary UNPACKING**")
coins_dic = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**coins_dic), "Knuts")
