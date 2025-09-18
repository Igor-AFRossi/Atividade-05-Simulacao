import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.calculadora import Calculadora

class TestIntegracaoCalculadora(unittest.TestCase):
    #Teste de operações sequenciais
    def test_operacoes_sequenciais(self):
        calc = Calculadora()
        calc.somar(2, 3)
        r1 = calc.obter_ultimo_resultado()
        calc.multiplicar(r1, 4)
        r2 = calc.obter_ultimo_resultado()
        calc.dividir(r2, 2)
        self.assertEqual(calc.obter_ultimo_resultado(), 10)
        self.assertEqual(len(calc.historico), 3)

    #Teste de interface entre métodos 
    def test_integracao_historico_resultado(self):
        calc = Calculadora()
        calc.potencia(2, 3)
        calc.somar(calc.obter_ultimo_resultado(), 2)
        self.assertEqual(calc.obter_ultimo_resultado(), 10)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 ^ 3 = 8", calc.historico)
        self.assertIn("8 + 2 = 10", calc.historico)

    #Teste extra 
    def test_sequencia_com_subtracao(self):
        calc = Calculadora()
        calc.somar(10, 5)
        calc.subtrair(calc.obter_ultimo_resultado(), 3)
        self.assertEqual(calc.obter_ultimo_resultado(), 12)
        self.assertEqual(len(calc.historico), 2)
