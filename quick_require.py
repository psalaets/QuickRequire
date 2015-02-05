import sublime, sublime_plugin, sys

if sys.version_info[0] == 3:
    from . import require_snippet
else:
    from require_snippet import make_from

def quote_style():
    return sublime.load_settings(__name__ + '.sublime-settings').get('quote_style')

class QuickRequireCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            # get line cursor is on
            cursorPosition = region.begin()
            line = self.view.line(cursorPosition)
            
            # get text to the left of the cursor
            region_up_to_cursor = sublime.Region(line.begin(), cursorPosition)
            left_side = self.view.substr(region_up_to_cursor)
            
            output = require_snippet.make_from(left_side, quote_style())
            
            self.view.run_command('insert_snippet', {'contents': output})