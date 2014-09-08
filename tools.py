#!/usr/bin/env python3

import os
import re
import env_vars

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

def real_done(path):

    if_done = True

    if not os.path.exists(os.path.join(path, 'wrfbdy_d01')):
        if_done = False

    for dom in range(1, env_vars.MAX_DOM+1):
        if not os.path.exists(os.path.join(path, 'wrfinput_d0' + str(dom))):
            if_done = False

    return if_done

def wrf_done(path, end_time):

    if_done = True

    for dom in range(1, env_vars.MAX_DOM+1):
        if not os.path.exists(os.path.join(path, 'wrfout_d0' + str(dom) + '_' + end_time)):
            if_done = False

    return if_done

def gsi_done(path):

    if_done = True

    if not os.path.exists(os.path.join(path, 'wrf_inout')):
        if_done = False

    return if_done
