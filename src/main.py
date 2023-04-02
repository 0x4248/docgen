# Docgen
# A simple script to generate markdown documentation from C source code
# GitHub: https://www.github.com/awesomelewis2007/docgen

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py input_file")
        sys.exit(1)
        
    if sys.argv[1] == "-help" or sys.argv[1] == "-h":
        print("Usage: python3 main.py input_file")
        sys.exit(0)

    input_file = sys.argv[1]
    output = ""
    with open(input_file, "r") as f:
        output = f.read()
    in_comment = False
    comment_read_title = False
    param_read = False
    comment_just_read = False
    func_tile_read = False
    for line in output.splitlines():
        if line.startswith("/**"):
            in_comment = True
        elif line.startswith("*/"):
            in_comment = False
            comment_just_read = True
            func_tile_read = False
            param_read = False
        elif in_comment:
            if line.startswith(" *") and not line.startswith(" * @"):
                if not comment_read_title:
                    print("# " + line[3:])
                    comment_read_title = True
                else:
                    if not func_tile_read:
                        print("## " + line[3:])
                        func_tile_read = True
                    else:
                        print(line[3:])
            elif line.startswith(" * @"):
                if line.startswith(" * @param"):
                    if not param_read:
                        print("### Parameters")
                        param_read = True
                    print("* " + line[11:])
                elif line.startswith(" * @return"):
                    print("### Return value")
                    print(line[12:])
                elif line.startswith(" * @") and ":" in line:
                    print(line[4:]+"\n")
        elif comment_just_read:
            if line == "":
                continue
            print("```c")
            line = line.replace(" {", ";").replace("{", ";")
            print(line)
            print("```")
            comment_just_read = False
        else:
            continue
