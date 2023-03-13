# Biblioteca-Criptografia

A biblioteca Cryptolibrary, é um modo criado por nós que permite criptografar e descriptografar mensagens usando uma cifra de substituição simples além de incluir funções para codificar e decodificar mensagens.

## Como usar:

Para utilizar o programa, basta seguir os passos abaixo:

1. Instale o Python 3.8 ou superior;

2. Instale a biblioteca Numpy;
```pip install numpy```

3. Instale a biblioteca cryptolibrary;
```pip install cryptolibrary```

4. Para facilitar, basta instalar os requirements.txt, que contém todas as bibliotecas necessárias para o funcionamento do programa.
```pip install -r requirements.txt```

Após instalar as bibliotecas, basta olhar o arquivo main.py e verificar o funcionamento de cada uma, que já apresenta um exemplo pronta para utilização.

## Funções:

### Função para_one_hot(mensagem):
Essa função recebe uma mensagem como entrada e codifica esta para uma matriz em cada caracter é representado em um vetor diferente da própria matriz.

### Função para_string(matriz_one_hot):
Essa função recebe uma matriz codificada como entrada em formato one_hot e decodifica para uma mensagem.

### Função cifrar(mensagem, matriz_permutacao):
Essa função recebe uma mensagem e uma matriz de permutação, retornando uma mensagem decifrada a partir da matriz recebida.

### Função de_cifrar(mensagem_cifrada, matriz_permutacao):
Essa função recebe uma mensagem cifrada e uma matriz de permutação, retornando a mensagem decifrada.

### Função enigma(mensagem, matriz_permutacao, matriz_permutacao_auxiliar):
Essa função recebe uma mensagem, uma matriz de permutação e uma matriz de permutação auxiliar, retornando uma mensagem cifrada.

### Função de_enigma(mensagem_cifrada, matriz_permutacao, matriz_permutacao_auxiliar):
Essa função recebe uma mensagem cifrada, uma matriz de permutação e uma matriz de permutação auxiliar, retornando a mensagem decifrada.


