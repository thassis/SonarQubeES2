import unittest
from unittest.mock import patch
from main import saudacao, calcular_soma, incrementar_contador, contador

# filepath: /home/thiago/Documents/projetos/sonar/SonarQubeES2/test_main.py

class TestMain(unittest.TestCase):
    def test_saudacao(self):
        with patch('builtins.print') as mocked_print:
            saudacao("Thiago")
            mocked_print.assert_called_once_with("Bem-vindo, Thiago!")

    def test_calcular_soma(self):
        numeros = [1, 2, 3, 4]
        resultado = calcular_soma(numeros)
        self.assertEqual(resultado, 10)

    @patch('builtins.input', return_value="Thiago")
    @patch('builtins.print')
    def test_saudacao_with_input(self, mocked_print, mocked_input):
        saudacao(mocked_input())
        mocked_print.assert_called_once_with("Bem-vindo, Thiago!")

if __name__ == "__main__":
    unittest.main()