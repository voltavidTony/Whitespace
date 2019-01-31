# Better Whitespace

## Cleanup your file on save with this plugin
Sublime 3 includes the options to trim whitespace at EOL and ensure an empty line at EOF, however, these don't always provide desired results. Therefore I have created this plugin to improve their behavior and called it 'Better Whitespace'.

## Features
This plugin features three useful commands, three settings, and one override snippet to control them all.

### Commands:
  - Ensure a singular empty new line at EOF
  - Remove empty lines
  - Trim whitespace at EOL

These commands are pretty much self explanatory. They can be manually executed via the command palette, and the command to remove empty lines is also found in Sublime's menu: Tools > Better Whitespace. By default, the commands to trim whitespace at EOL and ensure a singular empty new line at EOF run automatically when the user saves a file. The command to remove empty lines only runs manually.

### Settings:
  - Area of effect
  - Ensure empty line at EOF
  - Remove whitespace at EOL

These settings toggle/alter the commands' on-save execution. Their default values are found in the user settings file. From Sublime's menu: Tools > Better Whitespace, they can be changed for each opened file individually. These view specific settings are not saved and reset for every file opened. the two settings 'Ensure empty line at EOF' and 'Remove whitespace at EOL' control whether or not their commands will run when the file is saved.

Area of effect is a string setting. It has three recognized values (any unrecognized value is treated as "full"):
  - full
  - selected
  - unselected

When set to "full", then the entire document is edited by the comands. When set to "selected", any part of the document that **is _not_** selected is ignored. When set to "unselected", then any part of the document that **is** selected is ignored.

### Override Snippet:
  - Ignore all override

This override will prevent the commands from automatically running when the user saves, reguardless of what the settings indicate. It will however not prevent manual execution of the commands. Insert this snippet from the snippet palette, or by typing `bwsia` and pressing tab. (The plugin file itself includes this, since I didn't want the plugin to self-execute when I was still developing it.)

## Installation
This plugin is accessible via Package Control.
