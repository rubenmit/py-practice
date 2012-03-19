# scope
# each function will has a new scope, loacl veriable

def combine(parameter):
    print parameter + external

def combine2(parameter):
    'handle the case the loacl and global scope have the same variable'
    print parameter + globals()['parameter']

external = 'berry'
combine('Shrub') # 'Shrubberry'

parameter = 'berry'
combine('Shrub') # 'Shrubberry'
