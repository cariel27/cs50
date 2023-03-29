import csv

with open("slivers_deck.csv") as deck:
    csv_reader = csv.reader(deck)
    deck = []
    size = 0
    for row in csv_reader:
        if 'Quantity' not in row:
            size += int(row[0])
            for x in range(int(row[0])):
                deck.append(row[1])

    assert len(deck) == 58
    print(f"Deck Size {size}")
    print(f"Deck: \n")
