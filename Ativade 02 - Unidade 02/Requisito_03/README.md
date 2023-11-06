# Tabela de vizualização
|   | Qtd vértices | Qtd arestas | degree assortativity coefficient | Qtd componente conectados | Tamanho do componente gigante | Coeficiente de Clustering |
|---|--------------|-------------|----------------------------------|---------------------------|-----|---------------------------|
| Rede 'email' | 1005 | 16706 | -0.0110 | 20 | 986 | 0.3993 |
| Rede 'p2p' | 26518 | 65369 | -0.0077 | 11 | 26498 | 0.0055 |
| Rede 'facebook' | 4039 | 88234 | 0.0636 | 1 | 4039 | 0.6055 |
| Rede 'wiki' | 7115 | 100762 | -0.0831 | 24 | 7066 | 0.1409 |
| Rede 'cit' | 27770 | 352324 | -0.0303 | 143 | 27400 | 0.3120 |

* Rede 'email'
  * Este grafo é um grande sistema composto por 1005 entidades interconectadas. Ele exibe uma tendência leve para a formação de clusters e uma leve dissociação entre os vértices de diferentes graus. O grafo é dividido em 20 componentes conectados, sendo o maior deles o Componente Gigante, que contém 986 vértices.
* Rede 'p2p'
  * Este grafo é um grande sistema composto por 26518 entidades interconectadas. Ele exibe uma tendência leve para a formação de clusters, mas há uma leve dissociação entre os vértices de diferentes graus. O grafo é dividido em 11 componentes conectados, sendo o maior deles o Componente Gigante, que contém 26498 vértices.
* Rede 'facebook'
  * Este grafo é um sistema grande e densamente interconectado, com 4039 entidades que estão altamente agrupadas. Não há subgrupos isolados, pois todos os vértices fazem parte de uma única componente conectada. Além disso, o grafo exibe uma tendência para os vértices se conectarem a outros vértices com graus semelhantes.
* Rede 'wiki'
  * Este grafo é um grande sistema composto por 7115 entidades interconectadas. Ele exibe uma tendência para a formação de clusters, mas há também uma dissociação entre os vértices de diferentes graus. O grafo é dividido em 24 componentes conectados, sendo o maior deles o Componente Gigante, que contém 7062 vértices.
* Rede 'cit'
  * Este grafo é um sistema complexo com 27770 entidades interconectadas. Apesar da presença de vários componentes conectados, há um componente gigante significativo com 27400 vértices. O grafo exibe uma tendência para a formação de clusters, indicada pelo coeficiente de clustering relativamente alto, mas também mostra uma dissociação entre os vértices de diferentes graus, conforme indicado pelo coeficiente do grau de assortatividade negativo.
