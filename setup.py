import sys, os
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

def include_OpenGL():
    path_base = "C:\\pyzo2013c\\Lib\\site-packages\\OpenGL"
    skip_count = len(path_base) 
    zip_includes = [(path_base, "OpenGL")]
    for root, sub_folders, files in os.walk(path_base):
        for file_in_root in files:
            zip_includes.append(
                    ("{}".format(os.path.join(root, file_in_root)),
                     "{}".format(os.path.join("OpenGL", root[skip_count+1:], file_in_root))
                    ) 
            )      
    return zip_includes

options = {
    'build_exe': {
#         'packages': '' ,
#         'includes': '', 
#         'excludes': '',
        'zip_includes': include_OpenGL(),
        'icon': 'hellogl.ico',
    }
}

executables = [
    Executable('hellogl.py', base=base)
]

setup(name='hellogl',
      version='0.1',
      description='PySide port of the opengl/hellogl example from Qt v4.x',
      options=options,
      executables=executables
      )