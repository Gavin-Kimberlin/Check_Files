#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.8.2
#
# Author:       Gavin T. Kimberlin
#
# Purpose:      Check Files. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk

import check_files_gui

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(460,190)
        self.master.maxsize(460,190)
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")
        arg = self.master

        check_files_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
