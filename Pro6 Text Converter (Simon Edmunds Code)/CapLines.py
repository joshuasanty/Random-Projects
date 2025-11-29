import pyperclip

def capitalize_line_starts(text: str) -> str:
    lines = text.split('\n')
    new_lines = []

    for line in lines:
        if line:
            new_lines.append(line[0].upper() + line[1:])
        else:
            new_lines.append(line)

    return '\n'.join(new_lines)


if __name__ == "__main__":
    input_text = """
every knee will bow
to bless Your name

every tongue confess
that You are King

all for Your glory
all for Your glory

every tear will soon
be wiped away

every longing heart
will see Your face

all for Your glory
all for Your name

You are God Jesus
Majesty

You are life Jesus
saving Me

You are King Jesus

all will see that
You are God

every knee will bow
to bless Your name

every tongue confess
that You are King

all for Your glory
all for Your name

You are God Jesus
Majesty

You are life Jesus
saving Me

You are King, Jesus

all will see that
You are God

death could not keep You

the grave could not 
hold You

You are alive
You are alive

death could not keep You

the grave could not 
hold You

You are alive
You are alive

You are God Jesus
Majesty

You are life Jesus
saving Me

You are King Jesus
all will see that

You are God Jesus
Majesty

You are life Jesus
saving Me

You are King Jesus

all will see that
You are God

"""

    output_text = capitalize_line_starts(input_text)
    pyperclip.copy(output_text)   # <-- copies to clipboard automatically
    print("Output copied to clipboard!")
