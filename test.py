import unittest
from require_call import make_from

class aTest(unittest.TestCase):
    def test_var_name(self):
        result = make_from('var abc')
        
        self.assertEquals(result, ' = require("abc")')
    
    def test_name(self):
        result = make_from('abc')
        
        self.assertEquals(result, ' = require("abc")')
    
    def test_name_space(self):
        result = make_from('abc ')
        
        self.assertEquals(result, '= require("abc")')
    
    def test_name_spaces(self):
        result = make_from('abc    ')
        
        self.assertEquals(result, '= require("abc")')
    
    def test_camel_case_name(self):
        result = make_from('camelCaseBlah')
        
        self.assertEquals(result, ' = require("camel-case-blah")')
    
    def test_capitalized_name(self):
        result = make_from('Blah')
        
        self.assertEquals(result, ' = require("blah")')
    
    def test_just_space(self):
        result = make_from('     ')
        
        self.assertEquals(result, None)
    
    def test_empty_string(self):
        result = make_from('')
        
        self.assertEquals(result, None)
    
    def test_var_with_equals(self):
        result = make_from('var foo = ')
        
        self.assertEquals(result, None)
    
    def test_requesting_single_quotes(self):
        result = make_from('abc', 'single')
        
        self.assertEquals(result, " = require('abc')")
    
    def test_requesting_double_quotes(self):
        result = make_from('abc', 'double')
        
        self.assertEquals(result, ' = require("abc")')

if __name__ == '__main__':
    unittest.main()