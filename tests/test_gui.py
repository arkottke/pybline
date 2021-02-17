#!/usr/bin/env python3

from pybline.gui import ApplicationWindow


def test_application_window(qtbot):
    # Just draw the application and quit
    aw = ApplicationWindow()
    aw.show()
