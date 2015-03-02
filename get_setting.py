import sublime

def get_setting(key):
    return sublime.load_settings('quick_require.sublime-settings').get(key)