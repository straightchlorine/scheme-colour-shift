import os


def queue(path):
    for root, directory, files in os.walk(path):
        for file in files:
            print('Do you wish to process the ' + (path + file) + ' file?')
            if confirmation():
                yield path + file
            else:
                continue


def confirmation():
    answer = input()
    if answer.upper() == 'YES':
        return True
    else:
        return False
