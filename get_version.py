import os


def get_version():
    """
    read the version string from __init_.py
    """
    # get the init file path
    thispath = os.path.abspath(os.path.dirname(__file__))+"/"
    initfile = thispath + "smindex/__init__.py"

    # read the file in
    f = open(initfile, "r")
    lines = f.readlines()
    f.close()

    # search for the version
    version = "unknown"
    for item in lines:
        if "__version__" in item:
            s = item.split("=")
            version = s[-1].strip().strip('"').strip("'")
            break
    return version
