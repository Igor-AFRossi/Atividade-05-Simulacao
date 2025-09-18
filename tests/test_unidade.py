import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    
    #Testes de entrada e saída
    def test_entrada_saida_soma(self):
        calc = Calculadora()
        resultado = calc.somar(5, 3)
        self.assertEqual(resultado, 8)
        self.assertEqual(calc.obter_ultimo_resultado(), 8)
    def test_entrada_saida_subtracao(self):
        calc = Calculadora()
        self.assertEqual(calc.subtrair(10, 4), 6)
        self.assertEqual(calc.obter_ultimo_resultado(), 6)
    def test_entrada_saida_multiplicacao(self):
        calc = Calculadora()
        self.assertEqual(calc.multiplicar(7, 6), 42)
        self.assertEqual(calc.obter_ultimo_resultado(), 42)
    def test_entrada_saida_divisao(self):
        calc = Calculadora()
        self.assertEqual(calc.dividir(20, 5), 4)
        self.assertEqual(calc.obter_ultimo_resultado(), 4)
    def test_entrada_saida_potencia(self):
        calc = Calculadora()
        self.assertEqual(calc.potencia(2, 3), 8)
        self.assertEqual(calc.obter_ultimo_resultado(), 8)

    #Testes de tipagem
    def test_tipagem_invalida(self):
        calc = Calculadora()
        with self.assertRaises(TypeError): 
            calc.somar("5", 3)
        with self.assertRaises(TypeError): 
            calc.dividir(10, None)
    def test_tipagem_todas_operacoes(self):
        calc = Calculadora()
        with self.assertRaises(TypeError): 
            calc.subtrair("a", "b")
        with self.assertRaises(TypeError): 
            calc.multiplicar(5, "x")
        with self.assertRaises(TypeError): 
            calc.potencia("base", 2)
    
    #Testes de consistência
    def test_consistencia_historico(self):
        calc = Calculadora()
        calc.somar(2, 3)
        calc.multiplicar(4, 5)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 + 3 = 5", calc.historico)
        self.assertIn("4 * 5 = 20", calc.historico)
    def test_consistencia_ultimo_resultado(self):
        calc = Calculadora()
        calc.subtrair(10, 7)
        self.assertEqual(calc.obter_ultimo_resultado(), 3)

    #Testes de inicialização
    def test_inicializacao(self):
        calc = Calculadora()
        self.assertEqual(calc.resultado, 0)
        self.assertEqual(len(calc.historico), 0)

    #Testes de modificação de dados
    def test_modificacao_historico(self):
        calc = Calculadora()
        calc.somar(1, 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)
    def test_modificacao_ultimo_resultado(self):
        calc = Calculadora()
        calc.multiplicar(2, 5)
        self.assertEqual(calc.obter_ultimo_resultado(), 10)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)

    #Testes de limite inferior
    def test_limite_inferior(self):
        calc = Calculadora()
        self.assertEqual(calc.somar(0, 5), 5)
        self.assertEqual(calc.multiplicar(-1e-10, 2), -2e-10)

    #Testes de limite superior
    def test_limite_superior(self):
        calc = Calculadora()
        self.assertEqual(calc.somar(1e10, 1e10), 2e10)
    def test_limite_superior_float(self):
        import sys
        calc = Calculadora()
        big = sys.float_info.max
        self.assertEqual(calc.somar(big, 0), big)

    #Testes de valor fora do intervalo
    def test_divisao_por_zero(self):
        calc = Calculadora ()
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)

    #Testes de fluxos
    def test_fluxos_divisao(self):
        calc = Calculadora()
        # Caminho normal
        resultado = calc.dividir(10, 2)
        self.assertEqual(resultado , 5) 
        # Caminho de erro
        with self.assertRaises(ValueError): 
            calc.dividir(10, 0)

    #Testes de mensagens de erro
    def test_mensagens_erro(self):
        calc = Calculadora ()
        try:
            calc.dividir(5, 0) 
        except ValueError as e:
            self.assertEqual(str(e), "Divisao por zero nao permitida")
