import unittest

def MCDnum2(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a

def MCDnum4(a, b, c, d):
    gcd_ab = MCDnum2(a, b)
    gcd_abc = MCDnum2(gcd_ab, c)
    gcd_abcd = MCDnum2(gcd_abc, d)
    return gcd_abcd

class testOperaciones(unittest.TestCase):
    def test_MCDnum4(self):
        self.assertEqual(MCDnum4(24, 36, 48, 60), 12)
        self.assertEqual(MCDnum4(8, 12, 16, 24), 4)
        self.assertEqual(MCDnum4(7, 13, 29, 5), 1)

if __name__ == '__main__':
    unittest.main()
