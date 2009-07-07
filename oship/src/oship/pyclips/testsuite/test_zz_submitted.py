# test_submitted.py

"""revision $Id: test_zz_submitted.py 325 2007-04-05 22:50:33Z Franz $

TESTS:
COOL rule execution coherence on SYMBOL

"""


class ctc_Submitted(ctestcase):
    """tests submitted by users"""

    def ctf_Submitted01(self):
        """Testing: COOL rule execution coherence on SYMBOL"""
        for x in self.envdict.keys():
            e = self.envdict[x]
            e.Clear()
            e.Reset()
            C = e.BuildClass("C", "(is-a USER)(slot a1)")
            c = C.BuildInstance("c")
            c.Slots['a1'] = clips.Symbol("HELLO")
            r = e.BuildRule(
                "r1",
                """(object (is-a C) (a1 ?a1&HELLO))""",
                """(assert (success))"""
                )
            e.Run()
            f = e.InitialFact()
            while f.Next():
                f = f.Next()
            self.assertEqual(f.Relation, clips.Symbol("success"))


    def ctf_Submitted02(self):
        """Testing: COOL rule execution coherence on STRING"""
        for x in self.envdict.keys():
            e = self.envdict[x]
            e.Clear()
            e.Reset()
            C = e.BuildClass("C", "(is-a USER)(slot a1)")
            c = C.BuildInstance("c")
            c.Slots['a1'] = clips.String("HELLO")
            r = e.BuildRule(
                "r1",
                """
                    (object (is-a C) (a1 ?a1))
                    (test (eq (str-compare  ?a1 "HELLO") 0))
                """,
                """(assert (success))"""
                )
            e.Run()
            f = e.InitialFact()
            while f.Next():
                f = f.Next()
            self.assertEqual(f.Relation, clips.Symbol("success"))


    def ctf_Submitted03(self):
        """Testing: multiple environment consistency"""
        env1 = clips.Environment()
        env2 = clips.Environment()
        t1 = env1.BuildTemplate("t1", "(slot s1)")
        t2 = env2.BuildTemplate("t2", "(slot s2)")
        f1 = t1.BuildFact()
        f2 = t2.BuildFact()
        f1.Slots["s1"] = "1"
        f2.Slots["s2"] = "2"
        env1.Reset()
        env2.Reset()
        f1.Assert()
        f2.Assert()
        self.assertEqual(f1.Index, f2.Index)
        self.assertEqual(f1.Slots["s1"], clips.String("1"))
        self.assertEqual(f2.Slots["s2"], clips.String("2"))
        


# end.
