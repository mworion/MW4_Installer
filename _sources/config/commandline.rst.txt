Command line options
====================
InstallerMW4 supports a number of command line options to allow for automated
installation and updating of MountWizzard4. You could check them by running

.. code-block:: bash

    python startup.pyz --help   # Windows
    python3 startup.pyz --help  # Linux, MacOS


The following command line options are available:

'-c', '--clean'

Cleaning system packages from faulty installs

'-d', '--dpi'

Setting QT font DPI (+dpi = -fontsize, default=96)

'-n', '--no-start'

Running script without starting MountWizzard4

'-s', '--scale'

Setting Qt DPI scale factor (+scale = +size, default=1)

'-u', '--update'

Update MountWizzard4 to the actual release version

--update-beta'

Update MountWizzard4 to the actual beta version

--update-venv

Update the virtual environment directory to use this version of Python,
assuming Python has been upgraded in-place.

'-v', '--version'

Update MountWizzard4 to the named version