import sublime, sublime_plugin, require_call

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
            
            return require_call.make_from(left_side, quote_style())
