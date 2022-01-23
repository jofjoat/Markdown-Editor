markdown = []  # empty list to save the markdown code


def help_():
    print("""Available formatters: plain bold italic 
    header link inline-code ordered-list unordered-list new-line
    Special commands: !help !done""")  # displays help instructions to the user


# individual functions the formatters
def plain(plain_text):
    return plain_text


def bold(bold_text):
    return f'**{bold_text}**'


def italic(italic_text):
    return f'*{italic_text}*'


def inline_code(inline_text):
    return f'`{inline_text}`'


def link(link_label, link_url):
    return f'[{link_label}]({link_url})'


def header():
    while True:
        level = int(input('Level: '))
        if 1 <= level <= 6:
            header_text = input('Text: ')
            return f"{'#' * level} {header_text}{new_line()}"
        else:
            print('The level should be within the range of 1 to 6')


def new_line():
    return '\n'


def list_formatters(ordered=True):  # Default argument
    while True:
        rows = int(input('Number of rows: '))
        if rows <= 0:
            print('The number of rows should be greater than zero')
        else:
            for row in range(1, rows + 1):  # Iterate over the number of rows
                list_text = input(f'Row #{row}: ')

                # save the list according to type, ordered/unordered
                if ordered:
                    ordered_word = f'{row}. {list_text}{new_line()}'
                    markdown.append(ordered_word)
                else:
                    unordered_word = f'* {list_text}{new_line()}'
                    markdown.append(unordered_word)
            break


available_formatters = ['plain', 'bold', 'italic',
                        'header', 'link', 'inline-code',
                        'new-line', 'ordered-list', 'unordered-list']

while True:
    user_input = input('Choose a formatter: ')
    if user_input == '!help':
        help_()
    elif user_input == '!done':
        # upon exit, save the result in a file
        # file called output.md
        with open('output.md', 'w') as file:
            for line in markdown:
                file.write(line)
            file.close()
        break
    elif user_input in available_formatters:
        if user_input == 'plain':
            text = input('Text: ')
            markdown.append(plain(text))
        if user_input == 'bold':
            text = input('Text: ')
            markdown.append(bold(text))
        if user_input == 'italic':
            text = input('Text: ')
            markdown.append(italic(text))
        if user_input == 'inline-code':
            text = input('Text: ')
            markdown.append(inline_code(text))
        if user_input == 'link':
            label = input('Label: ')
            URL = input('URL: ')
            markdown.append(link(label, URL))
        if user_input == 'header':
            markdown.append(header())
        if user_input == 'new-line':
            markdown.append(new_line())
        if user_input == 'ordered-list':
            list_formatters()
        if user_input == 'unordered-list':
            list_formatters(ordered=False)
        print("".join(markdown))
    else:
        print('Unknown formatting type or command')
