#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re # これを消してmusician.pyの方だけに置きたい

class Note:

  SHARP = ["♯"]
  FLAT  = ["♭"]

  def __init__(self, name):
    self.name = name

  def is_sharp(self):
    pattern = r"♯"
    result = re.search(pattern, self.name)
    if result:
      return True
    else:
      return False

  def is_flat(self):
    pattern = r"♭"
    result = re.search(pattern, self.name)
    if result:
      return True
    else:
      return False

  def getName(self):
    return self.name

  def setName(self, name):
    self.name = name
