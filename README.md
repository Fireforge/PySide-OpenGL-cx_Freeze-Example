PySide OpenGL cx_Freeze Example
======================

About
---
An experimental build setup to turn a PySide OpenGL app into a binary package.
You can use this as boilerplate to create OpenGL apps that build into executables.

Requirements
---
I recommend using the [Pyzo environment](www.pyzo.org). It contains everything needed for this code and much more, especially for scientific apps.

If you wish to run with vanilla Python, use [Python 3.3 or higher](http://www.python.org/downloads/) with the following packages

- [PySide](http://qt-project.org/wiki/PySide)
- [PyOpenGl](http://pyopengl.sourceforge.net/)
- [cx_Freeze](http://cx-freeze.sourceforge.net/)

Building
---

- **Windows:** Run `build.ps1`

Please contribute to support Linux and Mac!

**Notes:**

* `setup.py` assumes you are using the Pyzo2013c environment. If not, change the `path_base` parameter of the `include_OpenGL` function to the location of your PyOpenGL.

