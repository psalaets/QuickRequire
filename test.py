import unittest
from require_call import make_from

class aTest(unittest.TestCase):
    def test_var(self):
        result = make_from('abc')
        
        self.assertEquals(result, ' = require("abc")')
    
    def test_var_space(self):
        result = make_from('abc ')
        
        self.assertEquals(result, '= require("abc")')
    
    def test_var_spaces(self):
        result = make_from('abc    ')
        
        self.assertEquals(result, '= require("abc")')
    
    def test_camel_case_var(self):
        result = make_from('camelCaseBlah')
        
        self.assertEquals(result, ' = require("camel-case-blah")')
    
    def test_capitalized_var(self):
        result = make_from('Blah')
        
        self.assertEquals(result, ' = require("blah")')

if __name__ == '__main__':
    unittest.main()