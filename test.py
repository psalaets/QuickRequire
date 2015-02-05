import unittest, sys

if sys.version_info[0] == 3:
    from . import require_snippet
    make_from = require_snippet.make_from
else:
    from require_snippet import make_from

class aTest(unittest.TestCase):
    def test_var_name(self):
        result = make_from('var abc')
        
        self.assertEquals(result, ' = require("${1:abc}")')
    
    def test_name(self):
        result = make_from('abc')
        
        self.assertEquals(result, ' = require("${1:abc}")')
    
    def test_name_space(self):
        result = make_from('abc ')
        
        self.assertEquals(result, '= require("${1:abc}")')
    
    def test_name_spaces(self):
        result = make_from('abc    ')
        
        self.assertEquals(result, '= require("${1:abc}")')
    
    def test_camel_case_name(self):
        result = make_from('camelCaseBlah')
        
        self.assertEquals(result, ' = require("${1:camel-case-blah}")')
    
    def test_capitalized_name(self):
        result = make_from('Blah')
        
        self.assertEquals(result, ' = require("${1:blah}")')
    
    def test_just_space(self):
        result = make_from('     ')
        
        self.assertEquals(result, 'require("${1:}")')
    
    def test_empty_string(self):
        result = make_from('')
        
        self.assertEquals(result, 'require("${1:}")')
    
    def test_var_with_equals(self):
        result = make_from('var foo = ')
        
        self.assertEquals(result, 'require("${1:}")')
    
    def test_requesting_single_quotes(self):
        result = make_from('abc', 'single')
        
        self.assertEquals(result, " = require('${1:abc}')")
    
    def test_requesting_double_quotes(self):
        result = make_from('abc', 'double')
        
        self.assertEquals(result, ' = require("${1:abc}")')
    
    def test_requesting_unknown_quote_style(self):
        result = make_from('abc', 'blah')
        
        self.assertEquals(result, ' = require("${1:abc}")')

if __name__ == '__main__':
    unittest.main()