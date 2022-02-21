# In order to prevent self-execution while experimenting, the
# following phrase is inserted: better_whitespace_ignore_all

# Default imports
import sublime
import sublime_plugin


# When the plugin loads, save all settings if not present already.
# It is recommended to disable the built in whitespace handling
def plugin_loaded():
    settings = sublime.load_settings("Preferences.sublime-settings")
    if not settings.has("better_whitespace_remove_whitespace_at_eol"):
        settings.set("better_whitespace_remove_whitespace_at_eol", True)
        sublime.save_settings("Preferences.sublime-settings")
    if not settings.has("better_whitespace_empty_line_at_eof"):
        settings.set("better_whitespace_empty_line_at_eof", True)
        sublime.save_settings("Preferences.sublime-settings")
    if not settings.has("better_whitespace_area_of_effect"):
        settings.set("better_whitespace_area_of_effect", "full")
        sublime.save_settings("Preferences.sublime-settings")


# If the file is not an editable text file, or it has been set to be
# ignored, skip the execution of the commands, otherwise, run the
# commands if their settings are true
class EventDump(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        if not view.encoding() or view.encoding() == "Hexadecimal" or \
            view.is_scratch() or view.find("better_whitespace_ignore_all", 0) or \
                view.settings().get('is_widget'):
            return
        if view.settings().get("better_whitespace_empty_line_at_eof", True):
            view.run_command("eof_whitespace")
        if view.settings().get("better_whitespace_remove_whitespace_at_eol", True):
            view.run_command("eol_whitespace")


# Ensure there is a singular empty line at the end of the file
class EofWhitespaceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        whitespaces = self.view.find_all(r"\s+")
        if whitespaces and whitespaces[-1].end() == self.view.size():
            self.view.erase(edit, whitespaces[-1])
        if (self.view.size() > 0):
            self.view.insert(edit, self.view.size(), "\n")


# Trim any whitespace characters form the ends of the lines, this
# includes ALL whitespace characters, even NBSP
class EolWhitespaceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.settings().get("better_whitespace_area_of_effect",
                                       "selected") != "selected"
        unsel = self.view.settings().get("better_whitespace_area_of_effect",
                                         "unselected") == "unselected"
        for whitespace in reversed(
            self.view.find_all(r"(^|(?<=\S))(?:(?![\r\n])\s)+$")
        ):
            if any([
                whitespace.intersects(self.view.line(sel))
                for sel in self.view.sel()
            ]) == sel == unsel:
                continue
            self.view.erase(edit, whitespace)


# This command will only run manually and removes empty lines,
# including whitespace-only lines
class RemoveEmptyLinesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.settings().get("better_whitespace_area_of_effect",
                                       "selected") != "selected"
        unsel = self.view.settings().get("better_whitespace_area_of_effect",
                                         "unselected") == "unselected"
        for whitespace in reversed(
            self.view.find_all(r"\s+(?=[\r\n])")
        ):
            if any([
                whitespace.intersects(self.view.line(sel))
                for sel in self.view.sel()
            ]) == sel == unsel:
                continue
            self.view.erase(edit, whitespace)
