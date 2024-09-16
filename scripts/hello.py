#!/usr/bin/env python3
from dev_aberto import hello

if __name__ == '__main__':
    date, name = hello()
    print(_('Last commit made in:'), date, _(' by'), name)
