'''
Author: Benjamin Lucas
Description: HW1 Testing triangle classification
'''

import unittest

def classify_triangle(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except Exception as e:
        return ''
    if a <= 0 or b <= 0 or c <= 0:
        return ''
    if a == b and a == c:
        return 'equilateral'
    elif a == b or a == c or b == c:
        return 'isosceles'
    elif (a*a + b*b == c*c) or (c*c + a*a == b*b) or (b*b + c*c == a*a):
        return 'right'
    else:
        return 'scalene'
    
class TestClassify(unittest.TestCase):
    def testValidInputs1(self):
        self.assertEqual(classify_triangle(3,3,3), 'equilateral')
    
    def testValidInputs2(self):
        self.assertEqual(classify_triangle(4,4,6), 'isosceles')
    
    def testValidInputs3(self):
        self.assertEqual(classify_triangle(3,4,5), 'right')
    
    def testValidInputs4(self):
        self.assertEqual(classify_triangle(9.6, 10.001, 99), 'scalene')
        
    def testValidInputs5(self):
        self.assertEqual(classify_triangle('99', '67.081', '4'), 'scalene')

    def testInvalidInputs1(self):
        self.assertEqual(classify_triangle(3,2,'c'), '')
    
    def testInvalidInputs2(self):
        self.assertEqual(classify_triangle('67a', '45', 7), '')
        
    def testInvalidInputs3(self):
        self.assertEqual(classify_triangle(-1, 0, 5), '')

if __name__ == "__main__":
    a = input('Input length of side A: ')
    b = input('Input length of side B: ')
    c = input('Input length of side C: ')
    ans = classify_triangle(a,b,c)
    if ans:
        print(f'({a}, {b}, {c}) is a {ans} triangle')
    else:
        print('Not a valid input!')

    unittest.main(exit=True)