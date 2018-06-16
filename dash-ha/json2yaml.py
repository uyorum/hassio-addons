#!/usr/bin/env python
import json
import yaml
import sys

def main(argv=None):
    if argv is None:
        argv = sys.argv;
    json_filename = argv[1]
    yaml_filename = argv[2]
    with open(json_filename, "r") as json_file:
        json_data = json.load(json_file)

    with open(yaml_filename, "w+") as yaml_file:
        yaml.dump(json_data, yaml_file, default_flow_style=False)

if __name__ == "__main__":
    sys.exit(main())
