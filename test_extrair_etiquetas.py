import unittest

from extrair_etiquetas import expandir_por_quantidade, separar_por_marca


def criar_op(ordem, produto, ctrab, quantidade):
    return {
        "ordem": ordem,
        "produto": produto,
        "ctrab": ctrab,
        "quantidade": quantidade,
        "descricao": "TESTE"}


class TestSepararPorMarca(unittest.TestCase):

    def test_ctrab_ccc_vai_para_ccc(self):
        aaa, bbb, ccc = separar_por_marca([criar_op("1", "CAD1", "CCC", 1)])
        self.assertEqual(len(ccc), 1)
        self.assertEqual(len(aaa), 0)
        self.assertEqual(len(bbb), 0)

    def test_ctrab_9999_com_ric_vai_para_bbb(self):
        aaa, bbb, ccc = separar_por_marca([criar_op("1", "RIC020", "9999", 1)])
        self.assertEqual(len(bbb), 1)

    def test_ctrab_9999_sem_ric_vai_para_aaa(self):
        aaa, bbb, ccc = separar_por_marca([criar_op("1", "SOF001", "9999", 1)])
        self.assertEqual(len(aaa), 1)
        self.assertEqual(len(bbb), 0)

    def test_outros_vao_para_aaa(self):
        aaa, bbb, ccc = separar_por_marca([criar_op("1", "SOF001", "0101", 1)])
        self.assertEqual(len(aaa), 1)


class TestExpandirPorQuantidade(unittest.TestCase):

    def test_completa_a_linha_com_sobra(self):
        # 10 etiquetas + 6 de sobra = 16 (2 linhas de 8)
        resultado = expandir_por_quantidade([criar_op("1", "SOF001", "0101", 10)])
        self.assertEqual(len(resultado), 16)
        self.assertEqual(resultado[9]["sequencia"], "OP 01")
        self.assertEqual(resultado[10]["sequencia"], "OP 01 - SOBRA")

    def test_linha_cheia_nao_tem_sobra(self):
        resultado = expandir_por_quantidade([criar_op("1", "SOF001", "0101", 8)])
        self.assertEqual(len(resultado), 8)

    def test_quantidade_zero_gera_uma_etiqueta(self):
        resultado = expandir_por_quantidade([criar_op("1", "SOF001", "0101", 0)])
        etiquetas = [r for r in resultado if r["sequencia"] == "OP 01"]
        self.assertEqual(len(etiquetas), 1)

    def test_numera_as_ops(self):
        ops = [criar_op("1", "A", "0101", 8), criar_op("2", "B", "0101", 8)]
        resultado = expandir_por_quantidade(ops)
        self.assertEqual(resultado[0]["sequencia"], "OP 01")
        self.assertEqual(resultado[8]["sequencia"], "OP 02")


if __name__ == "__main__":
    unittest.main()
