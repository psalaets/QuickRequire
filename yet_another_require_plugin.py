import sublime, sublime_plugin, re

# regex patterns
var_name_pattern = re.compile('\s*=\s*([_$a-zA-Z0-9]+)')
lower_then_upper_pattern = re.compile('([a-z])([A-Z])')

# param:    match containing 2 groups: 'a' and 'B'
# returns: 'a-b'
def bah(match):
    return match.group(1) + '-' + match.group(2).lower()

def camel_case_to_dashes(input):
    if input[0].isupper():
        input = input[0].lower() + input[1:]

    return re.sub(lower_then_upper_pattern, bah, input)

class AutoRequireModuleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            # get line cursor is on
            cursorPosition = region.begin()
            line = self.view.line(cursorPosition)
            
            # get text to the left of the cursor
            region_up_to_cursor = sublime.Region(line.begin(), cursorPosition)
            left_side = self.view.substr(region_up_to_cursor)
            
            # pull out var name on far side of '=', if any
            reversed = left_side[::-1] # flip before match to make regex easier
            match = var_name_pattern.match(reversed)
            
            if match:
                # unflip the first group and that's the var name
                variable = match.group(1)[::-1]
            
                # build the require() call
                require = 'require("%s")' % camel_case_to_dashes(variable)
            
                # put space after '=' if not there already
                if left_side[-1] == '=':
                    require = ' ' + require
                
                # write the require to view
                self.view.insert(edit, cursorPosition, require)
