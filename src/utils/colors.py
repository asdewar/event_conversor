class Colors:
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    default = '\033[0m'


def blue(text):
    print(Colors.blue + text + Colors.default)


def green(text):
    print(Colors.green + text + Colors.default)


def yellow(text):
    print(Colors.yellow + text + Colors.default)


def red(text):
    print(Colors.red + text + Colors.default)
