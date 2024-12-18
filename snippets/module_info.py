#!/usr/bin/env python3

import subprocess
import json
import os

cluster = os.getenv('CLUSTER')
mp = os.getenv('MODULEPATH')

def get_spider():

    ret = subprocess.run([f'module load lmod; spider -o jsonSoftwarePage {mp}'], shell=True, encoding='utf-8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    module_list = json.loads(ret.stdout)

    module_list.sort(key=lambda x: x['package'])

    return module_list


def make_table(module_list):
    module_table = ''

    module_table += f'=== \"{cluster}\"\n'
    module_table += f'    ## Modules available on the {cluster} cluster.\n'
    module_table += f'    \n'
    module_table += f'    |Package|Versions|\n    |---|---|\n'

    for m in module_list:
        try:
            module_table += f'    |{m["package"]}|{",".join([v["versionName"] for v in m["versions"]])}|\n'
        except KeyError:
            pass

    return(module_table)


if __name__ == "__main__":

# Capture and parse the output
    ml = get_spider()
    t = make_table(ml)
    print(t)

