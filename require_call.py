import re

# regex patterns
var_name_pattern = re.compile('(\s*)([_$a-zA-Z0-9]+)')
lower_then_upper_pattern = re.compile('([a-z])([A-Z])')

# param:    match containing 2 groups: 'a' and 'B'
# returns: 'a-b'
def bah(match):
    return match.group(1) + '-' + match.group(2).lower()

def camel_case_to_dashes(input):
    if input[0].isupper():
        input = input[0].lower() + input[1:]
    
    return re.sub(lower_then_upper_pattern, bah, input)

def make_from(left_of_cursor):
    # flip before match to make regex easier
    reversed = left_of_cursor[::-1]
    match = var_name_pattern.match(reversed)
    
    if match:
        space_after_var_name = match.group(1)
        flipped_var_name = match.group(2)
        
        variable = flipped_var_name[::-1]
        
        # build the require() expression
        require = '= require("%s")' % camel_case_to_dashes(variable)
        
        if space_after_var_name == '':
            require = ' ' + require
        
        return require
