import re
from string import Template

# regex patterns
var_name_pattern = re.compile('(\s*)([_$a-zA-Z0-9]+)')
lower_then_upper_pattern = re.compile('([a-z])([A-Z])')

# param:    match containing 2 groups: 'a' and 'B'
# returns: 'a-b'
def to_dashed(match):
    return match.group(1) + '-' + match.group(2).lower()

def module_name(input):
    if input[0].isupper():
        input = input[0].lower() + input[1:]
    
    return re.sub(lower_then_upper_pattern, to_dashed, input)

def make_from(left_of_cursor, quote_style='double'):
    if quote_style == 'single':
        quote = "'"
    else:
        quote = '"'
    
    # flip before match to make regex easier
    reversed = left_of_cursor[::-1]
    match = var_name_pattern.match(reversed)
    
    if match:
        space_after_var_name = match.group(1)
        flipped_var_name = match.group(2)
        
        variable = flipped_var_name[::-1]
        module = module_name(variable)
        
        # template for the require() snippet
        require_snippet = '= require(${quote}$${1:${module}}${quote})'
        
        if space_after_var_name == '':
            require_snippet = ' ' + require_snippet
        
        return Template(require_snippet).substitute(quote=quote, module=module)
