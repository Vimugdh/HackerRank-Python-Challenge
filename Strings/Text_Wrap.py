'''
TEXT WRAP
'''
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)


'''
textwrap.wrap(text[, width[, ...]])
Wraps the single paragraph in text (a string) so every line is at most width characters long. Returns a list of output lines, 
without final newlines.

See the TextWrapper.wrap() method for additional details on how wrap() behaves.

textwrap.fill(text[, width[, ...]])
Wraps the single paragraph in text, and returns a single string containing the wrapped paragraph. fill() is shorthand for 
"\n".join(wrap(text, ...))

'''

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)