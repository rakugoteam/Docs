# use this script before build local it locally
# normally I work on links that work for readthedocs server

import os
from tkinter import *
from tkinter.ttk import Progressbar, Label
from types import prepare_class
from typing import Literal

paths = [
        "source/topics/",
        "source/tutorials/"
    ]
md_files = []
 
# create window
class Window(Frame):

  def __init__(self, master=None):
    Frame.__init__(self, master)        
    self.master = master

    self.master.title("RakugoDocs Test Tool")
    self.master.geometry("400x100")

    self.label = Label(self, text="Click on Button to Start")
    self.label.pack(fill=X, expand=1, side=TOP)

    # Progress bar widget 
    self.progress = Progressbar(self, orient = HORIZONTAL, length=100, mode = 'determinate')
    self.progress.pack(fill=X)
    self.progress.forget()
    
    self.local_button = Button(self, text="Local", command=self.on_local)
    self.local_button.pack(fill=BOTH, expand=1)

    self.rtd_button = Button(self, text="ReadTheDocs", command=self.on_rtd)
    self.rtd_button.pack(fill=BOTH, expand=1)
  
    # widget can take all window
    self.pack(fill=BOTH, expand=1)

    # Execute Tkinter
    self.mainloop()

  def update_progress(self, value):
    self.progress['value'] = value * 100

  def preparing_files_ui(self, progress):
    p_text = "Preparing files "
    self.label["text"] = p_text + progress
    self.update_progress(0)
    self.progress.pack(fill=X, expand=1)

  def search_text_update(self, s_text):
    if "..." in self.label["text"]:
      self.label["text"] = s_text
    else:
      self.label["text"] += "."

  def on_local(self):
    self.local_button.forget()
    self.rtd_button.forget()
    self.fix_files("local")
  
  def on_rtd(self):
    self.local_button.forget()
    self.rtd_button.forget()
    self.fix_files("rtd")

  def fix_files(self, mode):
    s_text = "Search for files "
    self.label["text"] = s_text

    files = []
    for p in paths:
      self.search_text_update(s_text)
      for f in os.listdir(p):
        fp = os.path.join(p, f)
        files.append(fp)
        self.search_text_update(s_text)

    self.preparing_files_ui("1/3")
    i = 0
    l = len(files)
    for file in files:
      if ".md" in file:
        md_file = os.path.join(file)
        md_files.append(md_file)
        i += 1
        self.update_progress(i/l)
        # print(md_file)

    self.preparing_files_ui("2/3")
    i = 0
    l = len(md_files)
    files_to_change = {}
    for file in md_files:
      with open(file, "r") as f:
        lines = []
        for line in f:
          found = False
          if mode == "rtd":
            if ".html#" in line:
              line = line.replace(".html#", "/#")
              found = True
            
          if mode == "local":
            if "/#" in line:
              line = line.replace("/#", ".html#")
              found = True

          lines.append(line)
          if found:
            files_to_change[file] = lines
            print(file, len(files_to_change[file]))

      i += 1
      print("added", file)
      self.update_progress(i/l)
    
    self.preparing_files_ui("3/3")
    i = 0
    l = len(files_to_change)
    for file in files_to_change:
      with open(file, "w") as w:
        w.writelines(files_to_change[file])
      i += 1
      self.update_progress(i/l)

    self.label["text"] = "Finished"
    self.progress.forget()
    
    if mode == "local":
      self.rtd_button.pack()
    
    if mode == "rtd":
      self.local_button.pack()
    
root = Tk()
app = Window(root)