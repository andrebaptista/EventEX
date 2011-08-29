"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from testes import estatisticas

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

        
class EstatisticasTest(TestCase):
    def test_tamanho_lista(self):
        self.assertEquals(estatisticas.tamanho_lista([1,2,3,4,5]),5)
    
    def test_tamanho_lista_quebra(self):
        self.assertEquals(estatisticas.tamanho_lista([]),0)
        
    def test_maior_numero(self):
        self.assertEquals(estatisticas.maior_numero([1,2,4,7,10,-10]),10)
        
    def test_maior_numero_quebra(self):
        self.assertEquals(estatisticas.maior_numero([-1,-2,-3,-20]),-1)
    
    def test_maior_numero_quebra2(self):
        self.assertEquals(estatisticas.maior_numero([]),0)
