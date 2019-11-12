# https://stackoverflow.com/questions/12332975/installing-python-module-within-code
# How to deal with problematic module installation: https://stackoverflow.com/questions/54715835/numpy-is-installed-but-still-getting-error#answer-57631417

import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

def uninstall(package):
    if hasattr(pip, 'main'):
        pip.main(['uninstall', package])
    else:
        pip._internal.main(['uninstall', package])

# Example
if __name__ == '__main__':
    install('numpy')
