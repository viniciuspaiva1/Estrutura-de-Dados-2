#Análise das complexidades de cada função

### _init_:
* Big O (O): O(n), onde n é o número de linhas no arquivo CSV. Isso ocorre devido à leitura de todas as linhas e à conversão dos preços.
* Big Theta (Θ): Θ(n), pois o processo envolve uma leitura completa do arquivo e uma operação de conversão única.
* Big Omega (Ω): Ω(n), porque a leitura e a conversão de todas as linhas são necessárias.

### get_laptop_from_id:
* Big O (O): O(n), onde n é o número de laptops na lista. Isso ocorre porque, no pior caso, a função pode precisar percorrer todas as linhas da lista para encontrar o laptop com o ID correspondente.
* Big Theta (Θ): Θ(n), pois a função deve percorrer todas as linhas em busca do laptop.
* Big Omega (Ω): Ω(1), no melhor caso, se o laptop estiver na primeira linha da lista.

### get_laptop_from_id_fast:
* Big O (O): O(1), em média, quando se usa o mapeamento ID-linha criado no construtor. É uma operação de busca direta em um dicionário.
* Big Theta (Θ): Θ(1), em média.
* Big Omega (Ω): Ω(1), em média.

### check_promotion_dollars:
* Big O (O): O(n^2), onde n é o número de laptops na lista. Isso ocorre devido ao loop aninhado, que compara todas as combinações possíveis de preços.
* Big Theta (Θ): Θ(n^2), no pior caso.
* Big Omega (Ω): Ω(1), se o laptop com o preço especificado estiver na lista.

### check_promotion_dollars_fast:
* Big O (O): O(n), onde n é o número de preços únicos. Isso ocorre porque a função verifica se o preço especificado ou a diferença entre o preço especificado e os preços existentes estão no conjunto de preços únicos.
* Big Theta (Θ): Θ(n), em média.
* Big Omega (Ω): Ω(1), se o preço especificado estiver no conjunto de preços únicos.

### find_first_laptop_more_expensive:
* Big O (O): O(n), onde n é o número de laptops na lista. Isso ocorre porque a função percorre a lista ordenada de laptops.
* Big Theta (Θ): Θ(n), no pior caso.
* Big Omega (Ω): Ω(1), se o laptop mais caro estiver na primeira posição da lista ordenada.

### find_laptop_within_price_range:
* Big O (O): O(n), onde n é o número de laptops na lista. A função percorre a lista ordenada para encontrar laptops dentro do intervalo de preço.
* Big Theta (Θ): Θ(n), no pior caso.
* Big Omega (Ω): Ω(1), se o intervalo de preço não incluir laptops na lista.

### find_laptop_with_RAM_and_storage:
* Big O (O): O(n), onde n é o número de laptops na lista. A função percorre todas as linhas para encontrar laptops com RAM e armazenamento específicos.
* Big Theta (Θ): Θ(n), no pior caso.
* Big Omega (Ω): Ω(1), se não houver laptops com as especificações dadas.

### find_laptop_within_RAM_range:
* Big O (O): O(n), onde n é o número de laptops na lista. A função percorre todas as linhas para encontrar laptops com RAM dentro do intervalo especificado.
* Big Theta (Θ): Θ(n), no pior caso.
* Big Omega (Ω): Ω(1), se não houver laptops com RAM dentro do intervalo.

### find_laptop_within_storage_range:
* Big O (O): O(n), onde n é o número de laptops na lista. A função percorre todas as linhas para encontrar laptops com armazenamento dentro do intervalo especificado.
* Big Theta (Θ): Θ(n), no pior caso.
* Big Omega (Ω): Ω(1), se não houver laptops com armazenamento dentro do intervalo.

### find_laptop_with_RAM_range_and_storage_range:
* Big O (O): O(n), onde n é o número de laptops na lista. A função percorre todas as linhas para encontrar laptops com RAM e armazenamento dentro dos intervalos especificados.
* Big Theta (Θ): Θ(n), no pior caso.
* Big Omega (Ω): Ω(1), se não houver laptops que atendam aos critérios.
