# -*- coding: utf-8 -*-
import note

def test_sharp_note():
  sharp_note = note.Note("A#")
  assert sharp_note.is_sharp(), True

  sharp_note.setName("A♯")
  assert sharp_note.is_sharp(), True

