import os


def print_file(filename):
    with open(filename, "rt") as f:
        print("Filename :", filename)
        for (ln, line) in enumerate(f.readlines()):
            print(f"{ln+1:3d}:{line}", end='')


def print_python_files(path):
    entries = os.walk(dir)
    for dirname, dirs, files in entries:
        if dirname.find(".git") >= 0:
            continue
        # print("Directory : ", dirname)
        for f in files:
            if f.endswith('.py'):
                print_file(dirname + "\\" + f)


if __name__ == '__main__':
    dir = r"e:\classroom\python\nov22\demo"
    print_python_files(dir)

