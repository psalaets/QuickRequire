import unittest
from require_call import make_from

class Test(unittest.TestCase):
    def test_var_space_equals(self):
        result = make_from('abc =')
        
        self.assertEquals(result, ' require("abc")')
    
    def test_var_space_equals_space(self):
        result = make_from('abc = ')
        
        self.assertEquals(result, 'require("abc")')
    
    def test_var_space_equals_spaces(self):
        result = make_from('abc =    ')
        
        self.assertEquals(result, 'require("abc")')
    
    def test_var_spaces_equals_spaces(self):
        result = make_from('abc    =    ')
        
        self.assertEquals(result, 'require("abc")')
    
    def test_var_space(self):
        result = make_from('abc ')
        
        self.assertEquals(result, '= require("abc")')
    
    def test_var(self):
        result = make_from('abc')
        
        self.assertEquals(result, ' = require("abc")')


if __name__ == '__main__':
    unittest.main()