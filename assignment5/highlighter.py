#!/usr/bin/env python3
import  sys
import glob
import re
import argparse

def color_print(text, code=5):
    start_code = "\033[{}m".format(code)
    end_code = "\033[0m"
    return start_code + text + end_code


def read_syntax(syntax):
    with open(syntax) as syntax_:
        syntax_def = syntax_.read() 
    syntax_dict = dict()
    syntax_def = syntax_def.split('\n')
    for definition in syntax_def:
        pattern, kind = definition.split(": ")
        syntax_dict[kind] = pattern.strip('"')
    return syntax_dict

def read_theme(theme):
    with open(theme) as theme_:
        theme_def = theme_.read()
    theme_dict = dict()
    theme_def = theme_def.split('\n')
    for definition in theme_def:
        kind_1, color = definition.split(': ')
        theme_dict[kind_1] = color
    return theme_dict


def color_file(syntax_dict, theme_dict, file):
    with open(file) as file_:
        line_ = file_.read()
        for key in syntax_dict.keys():
            line_ = color_string(syntax_dict[key], line_, theme_dict[key])
        print(line_)


def color_string(pattern, line_, color):
    substitute = re.search(pattern,line_)
    if substitute is not None:
        line_ = re.sub(pattern, color_print(substitute.group(), color),line_)
    return line_

if __name__ == "__main__":    
    parser = argparse.ArgumentParser()
    parser.add_argument("syntax")
    parser.add_argument("theme")
    parser.add_argument("file")
    args = parser.parse_args()
    
    print_color = color_file(read_syntax(args.syntax), read_theme(args.theme), args.file)

