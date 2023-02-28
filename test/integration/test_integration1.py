import pytest

from noyau import *
from gui import *

def test_exemple():
   joueur=0
   i=2
   j=0
   grille=[[-1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1],
           [0, -1, -1, -1, -1, -1, -1],
           [0,  1, -1, -1, -1, -1, -1],
           [0,  1, -1, -1, -1, -1, -1],
           [0,  1, -1, -1, -1, -1, -1]]
   assert True==True

def test_gui_noyau():
    assert construire_gui('Yoann') == True