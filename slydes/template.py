class Template:
    def default(self, title, text, height=20, width=80):
        top_symbol = '-'
        bottom_symbol = '-'
        line_symbol = '#'
        blank_space = ' '
        title_line_space = 2
        line_border_size = 4  # because '#' is 'larger' than '-'
        title_size = len(title)

        # Prints top line
        print(top_symbol * width)
        height -= 1

        # Prints blank lines before title
        for _ in range(title_line_space):
            print(line_symbol, blank_space * (width - line_border_size), line_symbol)
            height -= 1

        # Prints title
        print(
            line_symbol,
            blank_space * line_border_size,
            title,
            blank_space * (width - line_border_size - title_size - 6),
            line_symbol,
        )
        height -= 2

        # Prints text
        text_lines = text.split('\n')
        for line in text_lines:
            line_size = len(line)
            print(
                line_symbol,
                blank_space * line_border_size,
                line,
                blank_space * (width - line_border_size - line_size - 6),
                line_symbol,
            )
            height -= 1

        # Prints last blank lines
        for _ in range(height - 1):
            print(line_symbol, blank_space * (width - line_border_size), line_symbol)

        # Prints bottom line
        print(bottom_symbol * width)
