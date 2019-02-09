import unittest
import gift_exchange
import custom_exception


class TestSum(unittest.TestCase):

    def test_no_solution(self):
        """
        test for the scenario when there are no possible solutions
        """
        ge = gift_exchange.GiftExchange()
        ge.add_members("basant")
        ge.add_partners("basant", "singh")
        self.assertRaises(custom_exception.NoSolutionPossibleException, ge.exchange, ge._MEMBERS, ge._PARTNERS)

        ge1 = gift_exchange.GiftExchange()
        ge1.add_members("basant")
        self.assertRaises(custom_exception.NoSolutionPossibleException, ge1.exchange, ge1._MEMBERS, ge1._PARTNERS)

        ge2 = gift_exchange.GiftExchange()
        ge2.add_partners("basant", "singh")
        self.assertRaises(custom_exception.NoSolutionPossibleException, ge2.exchange, ge2._MEMBERS, ge2._PARTNERS)

    def test_valid_solution(self):
        """
        test for the scenario when solution exist
        """
        ge = gift_exchange.GiftExchange()
        ge.add_members("basant")
        ge.add_members("rani")
        solution = ge.exchange(ge._MEMBERS, ge._PARTNERS)
        self.assertEqual(sorted(solution), sorted([('basant', 'rani'), ('rani', 'basant')]))

    def test_solution_length(self):
        """
        for the scenario when solution exist,
        in that case the solution length will be
        equal to number of memebers
        """
        ge = gift_exchange.GiftExchange()
        ge.add_members("basant")
        ge.add_members("rani")
        ge.add_members("raju")
        ge.add_members("anu")
        ge.add_partners("basant", "maya")
        ge.add_partners("rani", "suleman")
        solution = ge.exchange(ge._MEMBERS, ge._PARTNERS)
        self.assertEqual(len(solution), len(ge._MEMBERS))

    def test_duplicate_member(self):
        """
        test for the scenario when duplicate members are added
        """
        ge = gift_exchange.GiftExchange()
        ge.add_members("basant")
        self.assertRaises(custom_exception.DuplicateMemberException, ge.add_members, "basant")

    def test_duplicate_partner(self):
        """
          test for the scenario when duplicate partners are added
        """
        ge = gift_exchange.GiftExchange()
        ge.add_partners("basant", "singh")
        self.assertRaises(custom_exception.DuplicatePartnerException, ge.add_partners, "basant", "basant")

    def test_valid_exchange(self):
        """
            Check than an member is rejected as a donor for their partner.
        """
        ge = gift_exchange.GiftExchange()
        ge.add_members("basant")
        ge.add_members("rani")
        ge.add_members("raju")
        ge.add_members("anu")
        ge.add_partners("basant", "maya")
        ge.add_partners("rani", "suleman")

        result = ge.valid_exchange('basant', 'maya', ge._PARTNERS)
        self.assertEqual(result, False)

        result1 = ge.valid_exchange('basant', 'rani', ge._PARTNERS)
        self.assertEqual(result1, True)

    def test_generate_edge(self):
        """
        Check if all valid list of exchanges are created
        """
        ge = gift_exchange.GiftExchange()
        ge.add_members("basant")
        ge.add_members("rani")
        ge.add_members("raju")
        ge.add_members("anu")
        ge.add_partners("basant", "maya")
        ge.add_partners("rani", "suleman")

        result = ge.generate_edges(ge._MEMBERS, ge._PARTNERS)
        self.assertEqual(sorted(result), sorted([('basant', 'rani'), ('basant', 'suleman'), ('basant', 'raju'),
                                                 ('basant', 'anu'), ('maya', 'rani'), ('maya', 'suleman'), ('maya', 'raju'),
                                                 ('maya', 'anu'), ('rani', 'basant'), ('rani', 'maya'), ('rani', 'raju'), ('rani', 'anu'),
                                                 ('suleman', 'basant'), ('suleman', 'maya'), ('suleman', 'raju'), ('suleman', 'anu'),
                                                 ('raju', 'basant'), ('raju', 'maya'), ('raju', 'rani'), ('raju', 'suleman'),
                                                 ('raju', 'anu'), ('anu', 'basant'), ('anu', 'maya'), ('anu', 'rani'), ('anu', 'suleman'),
                                                 ('anu', 'raju')]))

    def test_remove_edges(self):
        """
        check if required pair are removed from the list of pairs of exchange
        """
        ge = gift_exchange.GiftExchange()
        ran_pair = ('basant', 'rani')
        edges= [('basant', 'rani'), ('rani', 'basant'), ('rani', 'maya'), ('anu', 'basant'), ('anu', 'maya'), ('anu', 'rani')]
        result = ge.remove_edges( ran_pair, edges)
        self.assertEqual(sorted(result), sorted([('rani', 'basant'), ('rani', 'maya'), ('anu', 'basant'), ('anu', 'maya')]))



if __name__ == '__main__':
    unittest.main()
