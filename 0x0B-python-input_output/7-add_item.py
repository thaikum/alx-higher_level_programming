#!/usr/bin/python3
"""
adds all arguments to a list and saves them to json
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    old_list = load_from_json_file('add_item.json')
    old_list += sys.argv[1:]
    save_to_json_file(old_list, 'add_item.json')
except Exception as e:
    save_to_json_file(sys.argv[1:], 'add_item.json')
