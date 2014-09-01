#!/usr/bin/env python3

import os
import re

def pick_value(input_file, keyword):

    if not os.path.exists(input_file):
        raise NameError('Input file not found!')

    else:
        fi = open(input_file, 'r')
        text = fi.read()
        pattern = re.compile(re.escape(keyword) + r'\s*=\s*(\d+)', re.IGNORECASE)
        result = pattern.search(text)
        if result != None:
            picked_value = result.group(1)
        else:
            raise NameError('Cannot find your keyword!')

        fi.close()

    return picked_value
