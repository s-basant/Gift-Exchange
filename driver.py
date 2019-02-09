import gift_exchange


def print_solution(solution):
    print("**** Gift Exchange List ****")
    if len(solution) != 0:
        for item in solution:
            print(item[0] + " -> " + item[1])
    else:
        print("No solution found")


def main():
    ge = gift_exchange.GiftExchange()
    print("Enter your name and your partner's name")
    while True:
        name = input("Member Name: ")
        if name == "":
            break
        ge.add_members(name)
        partner = input("Partner Name:")
        if partner != "":
            ge.add_partners(name, partner)

    solution = ge.exchange(ge._MEMBERS, ge._PARTNERS)
    print_solution(solution)


if __name__ == '__main__':
    main()
