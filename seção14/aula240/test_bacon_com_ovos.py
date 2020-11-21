# Unittest #2 com TDD
"""
TDD - Test driver development - (Desenvolvimento dirigido a testes)

Red
Parte 01 - Criar teste e ver falhar

Green
Parte 02 - Criar o código e ver o teste passar

Refactor
Parte 03 - Melhorar meu código
"""

import unittest
from seção14.aula240.bacon_com_ovos import bacon_com_ovos


class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_assertionerro_se_n_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('')

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida, msg=f'"{entrada}" não retornou "{saida}".')

    def test_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_não_for_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7, 8)
        saida = 'Passar fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida, msg=f'"{entrada}" não retornou "{saida}".')

    def test_bacon_com_ovos_deve_retornar_bacon_se_entrada__for_multiplo_somente_de_3(self):
        entradas = (3, 6, 9, 12, 18, 21)
        saida = 'Bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida, msg=f'"{entrada}" não retornou "{saida}".')

    def test_bacon_com_ovos_deve_retornar_ovos_se_entrada__for_multiplo_somente_de_5(self):
        entradas = (5, 10, 20, 25, 35)
        saida = 'Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida, msg=f'"{entrada}" não retornou "{saida}".')


if __name__ == '__main__':
    unittest(verbose=True)
