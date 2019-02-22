import os
import sys
import glob
import argparse
from stdlib_list import stdlib_list

def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="path to python project with .py scripts", type=str)
    parser.add_argument("-v", "--version", help="python version in use for supplied project", type=str)
    return parser.parse_args()

def main():
    # handle command line arguements
    args = argparser()
    if args.path is None:
        args.path = os.getcwd()

    if args.verion is None:
        args.version = "{}.{}".format(sys.version_info[0], sys.version_info[1]) 

    libraries = stdlib_list(args.version) # get standard library modules
    scripts = glob.glob(os.path.join(args.path, "**", "*.py"), recursive=True)
    print("Found {0} python scripts in {1}".format(len(scripts), args.path))

    # parse scripts to find alll imported modules
    modules = []
    for script in scripts:
        with open(script) as fp:
            code = fp.readlines()
            for line in code:
                if   line[0:6] == "import":
                    modules.append(line.split(" ")[1].replace("\n", "").split(".")[0])
                elif line[0:4] == "from":
                    modules.append(line.split(" ")[1].replace("\n", "").split(".")[0])                    

    # sort through modules and pick out unique and external modules only
    modules = set(modules)
    extern_modules = [mod for mod in modules if mod not in libraries]
    print("Found {0} modules in total and {1} external modules.".format(len(modules), len(extern_modules)))
    for idx, extern_module in enumerate(extern_modules):
        print(idx, extern_module)

    module_dict = {}
    print("\nImporting external python modules...")
    # get versions of external modules
    for extern_module in extern_modules:
        mod = __import__(extern_module)
        version = mod.__version__
        module_dict[extern_module] = version
    
    # create requirements.txt file
    with open("requirements.txt", "w") as fp:
        for module, version in module_dict.items():
            fp.write("{0}=={1}\n".format(module, version))
    print("Created new requirements.txt file.")

if __name__ == '__main__':
    main()
