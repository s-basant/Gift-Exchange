import random

import Constant
import custom_exception


class GiftExchange:

    def __init__(self):
        """Initialize the members and their partners."""
        self._MEMBERS = []
        self._PARTNERS = []

    def add_members(self, member):
        """
        Add a gift exchanger.
        :param member: name of the person to be added
        :return: no return
        """
        if member in self._MEMBERS:
            raise custom_exception.DuplicateMemberException(member)
        self._MEMBERS.append(member)

    def add_partners(self, member, partner):
        """
        Add a member and member's partner in list of members
        and then add to the list of partners.
        :param member: name of the person to be added
        :param partner: person's partner name
        :return: no return
        """

        self.add_members(partner)
        if member == partner:
            raise custom_exception.DuplicatePartnerException("member", (member, partner))
        self._PARTNERS.append((member, partner))

    def valid_exchange(self, taker, giver, couples):
        """
        implements rules
        - one can’t draw your own name
        - one can’t draw the name of your partner if you have one
        :param taker: person name who takes the gift
        :param giver: person name who gives the gift
        :param couples: list of partners who should not recieve each other gift
        :return: boolean value if the exchange is valid
        """
        if giver == taker:
            return False
        for first, second in couples:
            if (giver == first) and (taker == second) or (taker == first) and (giver == second):
                return False
        return True

    def generate_edges(self, member, couple):
        """
         Method generates all legal pair of exchanges
        :param member: list of member
        :param couple: list of partners
        :return: list of pairs which are valid for exchange
        """
        edges = []
        for element in member:
            other_nodes = member.copy()
            other_nodes.remove(element)
            for element1 in other_nodes:
                valid = self.valid_exchange(element, element1, couple)
                if valid:
                    edges.append((element, element1))
        return edges

    def remove_edges(self, ran_pair, edges):
        """
        Method removes non desirable pair

        :param ran_pair: a tuple
        :param edges: all possible edges
        :return: updated edge after removing edge associated with ran_pair
        """
        edges = [i for i in edges if i[1] != ran_pair[1]]
        edges = [i for i in edges if i[0] != ran_pair[0]]
        return edges

    def exchange(self, member, couple):
        """
        Method generates a solution

        :param member: list of members
        :param couple: list of partners
        :return: possible solution if exits else return no solution
        """

        edges = self.generate_edges(member, couple)
        solution = []
        count = 0
        """ iterate over valid exchange pairs until a solution with all valid pair is found """
        while len(solution) != len(member):
            if len(edges) != 0:
                ran_pair = random.choice(edges)
                if len(solution) == 0 or ran_pair not in solution:
                    solution.append(ran_pair)
                    edges = self.remove_edges(ran_pair, edges)
            else:
                edges = self.generate_edges(member, couple)
                solution = []
            count = count + 1
            """
            For the case where the solution is not found even in 100 attempts,
            the process is terminated with no possible solution
            """

            if count > Constant.MAX_ATTEMPT:
                print(count)
                raise custom_exception.NoSolutionPossibleException()
        return solution
