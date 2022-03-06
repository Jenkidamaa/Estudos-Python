from hashlib import sha256
import time
def aplicar_sha(texto):

  print(sha256(texto.encode("ascii")).hexdigest()


def minerar(n_bloco, transacoes, hash_bloco,qtd_zeros):
  nonce = 0
  while True:
    texto = str(n_bloco)+transacoes+hash_bloco+qtd_zeros+str(nonce)
    me_hash = aplicar_sha(texto)
    if me_hash.startswith("0" * qtd_zeros):
      return nonce, me_hash
    nonce += 1

n_bloco = 15 
transacoes = """ 
Lira -> Alon -> 15
"""
qtd_zeros = 4
hash_anterior = "abc"
resultado = minerar(n_bloco, transacoes, hash_anterior, qtd_zeros)
print(resultado)
