from aoc import run_solver

def get_type(hand):
    unique = len(set(hand))
    hand = sorted(hand, key=lambda x: hand.count(x), reverse=True)
    if unique == 5: # high card
        return 0
    elif unique == 4: # pair
        return 1
    elif unique == 3: 
        if hand.count(hand[0]) == 2: # two pair
            return 2
        else: # three of a kind
            return 3
    elif unique == 2:
        if hand.count(hand[0]) == 3: # full house
            return 4
        else: # four of a kind
            return 5
    else: # five of a kind
        return 6

def hash(hand, type, cards):
    h = type << 28
    for i, c in enumerate(hand):
        h += cards.index(c) << (24 - i*4)
    return h

def part1(input_str: str) -> str:
    cards = "AKQJT98765432"[::-1]
    lines = input_str.strip().split("\n")
    bets = []
    for line in lines:
        hand, bid = line.split()
        bets.append((hand, int(bid), hash(hand, get_type(hand), cards)))
    bets.sort(key=lambda x: x[2])
    total = 0
    for i, bet in enumerate(bets):
        rank = i+1
        total += rank * bet[1]
    return str(total)

def get_best_type(hand, cards):
    t = get_type(hand)
    best = t
    for card in set(cards) - set("J"):
        test = hand.replace("J", card)
        new_t = get_type(test)
        if new_t > best:
            best = new_t
    return best

def part2(input_str: str) -> str:
    cards = "AKQT98765432J"[::-1]
    lines = input_str.strip().split("\n")
    bets = []
    for line in lines:
        hand, bid = line.split()
        t = get_best_type(hand, cards)
        bets.append((hand, int(bid), hash(hand, t, cards)))
    bets.sort(key=lambda x: x[2])
    total = 0
    for i, bet in enumerate(bets):
        rank = i+1
        total += rank * bet[1]
    return str(total)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
