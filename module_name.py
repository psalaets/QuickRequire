import re, sys

if sys.version_info[0] == 3:
    from .get_setting import get_setting
else:
    from get_setting import get_setting

lower_then_upper_pattern = re.compile('([a-z])([A-Z])')

def module_name(variable_name):
    known = known_name(variable_name)
    if known:
        return known
    else:
        return guess_name(variable_name)

def known_name(variable_name):
    known_modules = get_setting('knownModulesByVariableName')
    if known_modules and variable_name in known_modules:
        return known_modules[variable_name]
    else:
        return None

# param:    match containing 2 groups: 'a' and 'B'
# returns: 'a-b'
def to_dashed(match):
    return match.group(1) + '-' + match.group(2).lower()

def guess_name(variable_name):
    if variable_name[0].isupper():
        variable_name = variable_name[0].lower() + variable_name[1:]
    
    return re.sub(lower_then_upper_pattern, to_dashed, variable_name)
