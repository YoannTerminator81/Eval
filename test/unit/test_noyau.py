import pytest

from noyau import *

def test_changer_joueur():
   assert True==True

def test_jeton():
   assert(jeton('Hardy',2,3,1,2,grille)) != 0

@pytest.mark.parametrize("n1, n2, n3",  [(1,2,3), (1,2,1), message])
def test_jouer(n1,n2,n3):
    assert(jouer(n1, n2, n3)) == True