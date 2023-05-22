#!/usr/bin/python3
# a command processor lets user control the prompt for the interactive session

import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    # Set the initial prompt for user input
    prompt = 'prompt: '
    # Displayed when the command processor starts
    intro = "Simple command processor example."

    # Header displayed before documented commands
    doc_header = 'doc_header'
    # Header displayed before miscellaneous help topics
    misc_header = 'misc_header'
    # Header displayed before undocumented commands
    undoc_header = 'undoc_header'

    # Character used to draw a ruler line in help output
    ruler = '*'

    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ': '  # Change the prompt to the given value

    def do_EOF(self, line):
        return True  # Signal the end of the command processor

if __name__ == '__main__':
    HelloWorld().cmdloop()  # Start the command processor loop

