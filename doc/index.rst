Welcome to MW4_Installer!
=========================
MW4_Installer is a general utility for installing and starting MountWizzard4 on
your computer and it comes also with an PDF documentation:

https://mworion.github.io/MW4_Installer/MW4_Installer.pdf

Before starting
---------------

To improve quality and usability any feedback is highly welcome! To maintain a
good transparency and professional work for my, please respect the following
recommendations how to feed back.

.. note:: Please report issues / bugs here:

          https://github.com/mworion/MW4_Installer/issues.

.. note:: Feature requests and discussions or for all other topics of interest
          there is a good place to start here:

          https://github.com/mworion/MW4_Installer/discussions


In case of a bug report please have a good description (maybe a screenshot if it‘s
related to GUI) and add the log file(s). Normally you just could drop the log file
(or PNG in case of a screen shot) directly to the webpage issues on GitHub. In
some cases GitHub does not accept the file format (unfortunately for example FITs
files). I this case, please zip them and drop the zipped file. This will work. If
you have multiple files, please don‘t zip them to one file! I need them separated
and zipped causes more work.

If changes are made due to a feedback, new releases will have a link to the
closed issues on GitHub.

If you on the way of installing MountWizzard4  to your windows system, please
be aware of the 32bit / 64bit limitations of ASCOM / drivers and python. If you
are using 64bit drivers (most likely with the new large scale CMOS cameras),
you need to install 64bit python as well as windows does not mix both variants
flawless.

.. warning:: I strongly recommend not using whitespace in filenames or directory
             paths. Especially in windows handling them is not straight forward
             and I hardly could do all the tests needed to ensure it's
             functionality.

.. toctree::
    :maxdepth: 2

    install/python
    install/mw4
    install/platesolvers
    install/apple_silicon
    install/rpi3
    install/rpi4_5
    config/configure
    config/commandline
    changelog/changelog
