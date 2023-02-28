import pytest

from noyau import *

def test_changer_joueur():
   assert True==True

def test_jeton():
   assert(jeton('Hardy',-1,3,1,2,grille)) == 0

@pytest.mark.parametrize("n1, n2, n3, n4",  ['Laurel', 2, 3, grille])
def test_coup_gagnant(n1,n2,n3,n4):
    assert(coup_gagnant(n1, n2, n3, n4)) == True