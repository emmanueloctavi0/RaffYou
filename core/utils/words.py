

def clean_word(word):
    """'Clean' the characters for telegram message MarkdownV2"""
    chars = [ '_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    for char in chars:
        word = word.replace(char, f'\{char}')
    return word
