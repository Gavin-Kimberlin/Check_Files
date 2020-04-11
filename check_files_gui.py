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
import check_files_main

def load_gui(self):
    self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Browse...')
    self.btn_browse1.grid(row=0,column=0,padx=(25,0),pady=(45,10),sticky=W)
    
    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Browse...')
    self.btn_browse2.grid(row=1,column=0,padx=(25,0),pady=(5,10),sticky=W)

    self.check_for_files = tk.Button(self.master,width=12,height=2,text='Check for files...')
    self.check_for_files.grid(row=2,column=0,padx=(25,0),pady=(5,10),sticky=W)

    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program')
    self.btn_close.grid(row=2,column=1,padx=(225,0),pady=(5,10),sticky=E)

    self.txt_browse1 = tk.Entry(self.master,text='')
    self.txt_browse1.grid(row=0,column=1,rowspan=1,columnspan=1,padx=(25,0),pady=(45,10),sticky=N+E+W)

    self.txt_browse2 = tk.Entry(self.master,text='')
    self.txt_browse2.grid(row=1,column=1,rowspan=1,columnspan=1,padx=(25,0),pady=(5,10),sticky=N+E+W)


if __name__ == "__main__":
    pass
