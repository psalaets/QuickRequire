import re

if sys.version_info[0] == 3:
    from .get_setting import get_setting
else:
    from get_setting import get_setting

lower_then_upper_pattern = re.compile('([a-z])([A-Z])')

def module_name(variable_name):
    known = known_name(variable_name)
    if known:
        return known
    else
        return guess_name(variable_name)

def known_name(variable_name):
    return get_setting('knownModulesByVariableName')[variable_name]

def guess_name(variable_name):
    if variable_name[0].isupper():
        variable_name = variable_name[0].lower() + variable_name[1:]
    
    return re.sub(lower_then_upper_pattern, to_dashed, var_name)
