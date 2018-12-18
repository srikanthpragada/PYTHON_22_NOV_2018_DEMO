import os


def print_python_files(path):
    entries = os.walk(dir)
    for dirname, dirs, files in entries:
        if dirname.find(".git") >= 0:
            continue
        names = []
        for f in files:
            if f.endswith('.py'):
                names.append(f)

        if len(names) > 0:
            print("Directory : ", dirname)
            for n in names:
                print(n)


if __name__ == '__main__':
    dir = r"e:\classroom\python\nov22\demo"
    print_python_files(dir)
