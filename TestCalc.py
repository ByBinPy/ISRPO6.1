import unittest
from Calc import calc
class TestsCalc(unittest.TestCase):
    
    def test_sum(self):

        self.assertEqual(calc("+",0,0),0)
        
        self.assertEqual(calc("+",110000000,10101010010),10211010010)

        self.assertEqual(calc("+",0,0),0)

        self.assertEqual(calc("+",40,10),50)
        
    def test_raz(self):
        self.assertEqual(calc("-",1,1),0)

        self.assertEqual(calc("-",-50,50),-100)

        self.assertEqual(calc("-",100,1),99)

    def test_proiz(self):
        
        self.assertEqual(calc("*",1,1),1)
        
        self.assertEqual(calc("*",4254555885,6888888855588),29309162621652840535380)
        
    def test_dele(self):
        
        self.assertEqual(calc("/",1,0),None)
        
        self.assertEqual(calc("/",1,1),1)
        
if __name__ == "__main__":
    unittest.main()
    
