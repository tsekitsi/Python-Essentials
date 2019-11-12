# https://stackoverflow.com/questions/12332975/installing-python-module-within-code

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
