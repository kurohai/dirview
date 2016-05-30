import os


def check_file(filename, dirpath):
    filepath = os.path.join(dirpath, filename)
    if os.path.isfile(filepath):
        return filepath
    else:
        return None

def _scan_dir(dirpath):
    print 'dirpath:', dirpath
    print 'contents:', os.listdir(dirpath)
    results = list()
    for f in os.listdir(dirpath):
        if check_file(f, dirpath):
            results.append(f)
    return results

