#!/usr/bin/env python3
import env_vars
import os
import subprocess

def run(args):
    print("Start running WPS...")
    print("Task:", args.task)

    make_new_run()

    if args.task == "make_namelist":
        make_namelist(args)

    elif args.task == "geogrid":
        os.chdir(env_vars.WORK_ROOT)
        subprocess.call("./geogrid.exe", shell=True)

    elif args.task == "ungrib":
        os.chdir(env_vars.WORK_ROOT)
        subprocess.call("./ungrib.exe", shell=True)

    elif args.task == "metgrid":
        os.chdir(env_vars.WORK_ROOT)
        subprocess.call("./metgrid.exe", shell=True)


def make_new_run():

    os.chdir(env_vars.WPS_ROOT)

    if not os.path.exists(env_vars.RUN_NAME):
        os.mkdir(env_vars.RUN_NAME)
    #curDir = os.getcwd()
    #print(curDir)

    env_vars.WORK_ROOT = os.path.join(env_vars.WPS_ROOT, env_vars.RUN_NAME)
    print("WORK_ROOT:", env_vars.WORK_ROOT)

    os.chdir(env_vars.WORK_ROOT)

    tmp_dirs = [
            "geogrid",
            "metgrid",
            ]
    for tmp_dir in tmp_dirs:
        if not os.path.lexists(tmp_dir):
            os.mkdir(tmp_dir)

    cmds = [
    "ln -sf " + env_vars.WPS_ROOT + "/geogrid/src/geogrid.exe .",
    "ln -sf " + env_vars.WPS_ROOT + "/geogrid/GEOGRID.TBL.ARW ./geogrid/GEOGRID.TBL",
    "ln -sf " + env_vars.WPS_ROOT + "/link_grib.csh .",
    "ln -sf " + env_vars.WPS_ROOT + "/ungrib/src/ungrib.exe .",
    "ln -sf " + env_vars.WPS_ROOT + "/ungrib/Variable_Tables/Vtable.GFS Vtable",
    "ln -sf " + env_vars.WPS_ROOT + "/metgrid/METGRID.TBL.ARW ./metgrid/METGRID.TBL",
    "ln -sf " + env_vars.WPS_ROOT + "/metgrid/src/metgrid.exe .",
    ]
    for cmd in cmds:
        subprocess.call(cmd, shell=True)



def make_namelist(args):
    pass
