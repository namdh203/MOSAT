#! /usr/bin/python3


def print_debug(info):
    with open('output.log', 'a') as f:
        print(info, file=f)
        f.close()

def print_debug(info):
    with open('output.log', 'a') as f:
        print(info, file=f)
        f.close()

def save_npc_position(info):
    with open('npc_position.log', 'a') as f:
        print(info, file=f)
        f.close()

def recoder(info):
    with open('data.log', 'a') as f:
        print(info, file=f)
        f.close()


def select(info):
    with open('select.log', 'a') as f:
        print(info, file=f)
        f.close()
