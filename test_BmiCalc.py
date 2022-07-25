import unittest
from main import BMI_Calc as Bmi
import sqlite3


class TestCalcBmi(unittest.TestCase):


    def setUp(self):
        self.I1 = Bmi('TestName', 'TestFamily', 65, 190)
        self.I2 = Bmi('TestName2', 'TestFamily2', 75, 175)
        self.I3 = Bmi('TestName3', 'TestFamily3', 85, 180)
        self.I4 = Bmi('TestName3', 'TestFamily3', 95, 160)

    def test_calc_bmi(self):
        self.assertEqual(self.I1.calc_bmi(), 18.0)
        self.assertEqual(self.I2.calc_bmi(), 24.5)
        self.assertEqual(self.I3.calc_bmi(), 26.2)
        self.assertEqual(self.I4.calc_bmi(), 37.1)

    def test_Status_bmi(self):

        # test First if
        self.bmiI1 = self.I1.calc_bmi()
        msg = 'You must have weight, so maybe you need to gain some weight.\nWe recommend that you seek help from your doctor or nutritionist.'
        self.assertEqual(self.I1.Status_bmi(), msg)

        # test second if
        self.BmiI2 = self.I2.calc_bmi()
        msg = 'A BMI between 18.5 and 24.9 indicates a somewhat normal BMI and tells you that you are at an appropriate weight for your height.\nBy maintaining a healthy weight, you prevent serious risks to your health.'
        self.assertEqual(self.I2.Status_bmi(), msg)

        # third if
        self.BMiI3 = self.I3.calc_bmi()
        msg = 'A BMI between 25 and 29.9 tells you that you are slightly overweight and need to lose some weight.\nYou can consult your doctor to lose weight.'
        self.assertEqual(self.I3.Status_bmi(), msg)

        # fourth
        self.BMiI4 = self.I4.calc_bmi()
        msg = "A BMI above 30 warns you that you are overweight. If you don't lose weight, your health will definitely be at risk. Be sure to talk to your doctor or nutritionist and start dieting."
        self.assertEqual(self.I4.Status_bmi(), msg)



if __name__ == '__main__':
    unittest.main()
