import re

# regex patterns
var_name_pattern = re.compile('(\s*)(=?)(\s*)([_$a-zA-Z0-9]+)')
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
    # pull out var name on far side of '=', if any
    reversed = left_of_cursor[::-1] # flip before match to make regex easier
    
    match = var_name_pattern.match(reversed)
    
    if match:
        space_before_equals_sign = match.group(1)
        equals_sign = match.group(2)
        space_after_equals_sign = match.group(3)
        flipped_var_name = match.group(4)
        
        variable = flipped_var_name[::-1]
        
        # build the require() call
        require = 'require("%s")' % camel_case_to_dashes(variable)
        
        result_parts = []
        
        if space_before_equals_sign == '':
            result_parts.append(' ')
        
        # if there wasn't an '=', add one
        if equals_sign == '':
            result_parts.append('=')
        
        # put space after '=' if not there already
        if space_after_equals_sign == '':
            result_parts.append(' ')
        
        result_parts.append(require)
        
        return ''.join(result_parts)
