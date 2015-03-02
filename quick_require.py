import sublime, sublime_plugin, sys

if sys.version_info[0] == 3:
    from .require_snippet import make_from
    from .get_setting import get_setting
else:
    from require_snippet import make_from
    from get_setting import get_setting

def quote_style():
    return get_setting('quote_style')

class QuickRequireCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            # get line cursor is on
            cursorPosition = region.begin()
            line = self.view.line(cursorPosition)
            
            # get text to the left of the cursor
            region_up_to_cursor = sublime.Region(line.begin(), cursorPosition)
            left_side = self.view.substr(region_up_to_cursor)
            
            output = make_from(left_side, quote_style())
            
            self.view.run_command('insert_snippet', {'contents': output})