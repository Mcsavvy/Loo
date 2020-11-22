"""Create Command Line interfaces for functions"""
import shelve
import os
import sys
import glob
import getpass 
import Loo as this_file_i_wrote
from importlib import reload

Name = getpass.getuser()
the_loo = {}

with shelve.open('bin') as db:
    pass

class Loo:
    def __init__(self):
        pass
    class bind:
        def __init__(self, function):
            self.function = function
        
        
        def withcmd(self, flag):
            self.flag = flag 
            the_loo[self.flag]=self.function
            print(the_loo)
        
    def loop(self):
        while True:
            prompt = input(f'{Name}@LOO:$ ')
            if prompt in the_loo.keys():
                command = the_loo[prompt]
                try:
                    exec(command)
                    continue
                except:
                    e = sys.exc_info()[0]
                    print(e)
                    print(f'\n{prompt} removed from commands')
                    del the_loo[prompt]
                    continue
            elif prompt in ['-c', '-code']:
                with open('Loo.py', 'a+') as file:
                    while True:
                        line = input('$')
                        if line.endswith('$'):
                            break
                        file.write(f'\n{line}')
                reload(this_file_i_wrote)
                bind = str(input('$ Bind >>>'))
                cmd = str(input('$ With >>>'))
                try:
                    the_loo[cmd] = f'this_file_i_wrote.{bind}'
                    print('Bound!')
                    continue
                except:
                    e = sys.exc_info()[0]
                    print(e)
                    continue
            elif prompt in ['-v', '-view']:
                for key, value in the_loo.items():
                    print(key, value)
                continue
            elif prompt in ['-end', '-e']:
                break
            elif prompt in  ['-bind', '-b']:
                bind = str(input('$ Bind >>>'))
                cmd = str(input('$ With >>>'))
                the_loo[cmd] = bind
                print('Bound!')
                continue
            elif prompt in ['-help', '-h']:
                if len(the_loo.keys()) < 1:
                    print('You don\'t have any commands\n\tUse \'-bind\' or \'-b\' to add new command')
                else:
                    print(f'{Name}, your commands are:')
                    for e,i in enumerate(the_loo.keys()):
                        print(f'\t{e+1}.{i}')
            else:
                print('Invalid command\n\tUse \'-help\' or \'-h\' to view your commands')