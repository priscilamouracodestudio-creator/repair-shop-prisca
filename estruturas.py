class TabelaHashOficina:
  """Tabela Hash com encadeamento"""

  def __init__(self, tamanho=7):
    self.tamanho = tamanho
    self.baldes = [[] for _ in range(tamanho)]

    def _hash(self, chave):
      #Para transformar texto/chave em um índice número usando a soma dos códigos ASCII
      return sum(ord (c) for c in str (chave)) % self.tamanho

    def inserir(self, chave, valor):
      indice = self._hash(chave)
      # se a chave já existir, atualiza o valor
      for par in self.baldes[indice]:
        if par[0] == chave:
          par[1] = valor
          return

      #Adiciona na lista  

      self.baldes[indice].append([chave, valor])

  def buscar(self, chave):
      indice = self._hash(chave)
      for par in self.baldes[indice]:
        if par[0] == chave:
          return par[1]
      return None

class MinHeapOficina:
  """Mini heap para gerir a fila de prioridade (menor número = maior urgência."""

  def __init__(self):
    self.dados = []

  def _pai(self, i):
    return (i - 1) // 2

  def _esq(self, i):
    return 2 * i + 1

  def _dir(self, i):
    return 2 * i + 2


  def _sobe(self, i):
    while i > 0:
      p = self._pai(i)
      if self.dados[i][0] < self.dados[p][0]:
        self.dados[i], self.dados[p] = self.dados[p], self.dados[i]
        i = p
      else:
        break

  def _desce(self, i):
    n = len(self.dados)
    while True:
      menor = i
      e, d = self._esq(i), self._dir(i)
      if e < n and self.dados[e][0] < self.dados[menor][0]:
        menor = e
      if d < n and self.dados[d][0] < self.dados[menor][0]:
        menor = d
      if menor == i:
        break
      self.dados[i], self.dados[menor] = self.dados[menor], self.dados[i]
      i = menor

  def inserir(self, prioridade, ordem_chegada, dados_moto):
    self.dados.append((prioridade, ordem_chegada, dados_moto))
    self._sobe(len(self.dados) - 1)

  def extrair_min(self):
    if not self.dados:
      return None


  def extrair_min(self):
    if not self.dados:
      return None
    minimo = self
    ultimo = self.dados.pop()
    if self.dados:
      self.dados[0] = ultimo
      self._desce(0)
    return minimo


class PilhaHistoricoOS:
  """Pilha (LIFO)"""

  def __init__(self):
    self.topo = None

  class NoPilha:
    def  __init__(self, acao):
      self.topo = None

  def empilhar(self, acao):
    novo = self.NoPilha(acao)
    novo.proximo = self.topo
    self.topo = novo

  def desempilhar(self):
    if self.topo is None:
      return None
    acao_removida = self.topo.acao
    self.topo = self.topo.proximo
    return acao_removida

  def vazia(self):
    return self.topo is None

        



