#!/usr/bin/python

import json
import glob
import jinja2

d = {
    "version": "2",
}

if __name__ == '__main__':
    templates = []
    for f in glob.glob("apps/*.json"):
        print(f)
        with open(f, 'r') as fd:
            templates.append(json.load(fd))
    
    d["templates"] = templates

    with open("templates_v2.json", "w") as f:
        json.dump(d, f, indent=2)
        f.write("\n")
