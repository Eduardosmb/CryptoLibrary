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

## Como Funciona:
   Cripotagrafar:
   
      1. Primeiramente é transformada a palavra desejada para o metodo one hot, ou seja, a palavra desejada passa a ser representada por uma matriz onde cada linha representa uma letra e cada coluna uma posição. 
      Ou seja:
      
                  M(i,j) = []
                  onde i = letra, j = posição
      
      2. Logo após, multiplicamos a matriz M por uma matriz "P", que nada mais é do que a permutação da matriz identidade. Isso possui a finalidade de embaralhar as linhas e colunas da matriz original:
                  
                  PM
      
      3. Por fim, para que nossa criptografia de fato vire um enigma com um bom grau de dificuldade, utilizamos uma segunda matriz "E" (uma outra permutação da matriz identidade):
      
                  (E^n)PM
                  onde n corresponde a j.
                  
       
       Dessa forma, acabamos por criptografar nossa palavra inicial.
   
   Decriptografar:
   
      1. Primeiramente é transformada a palavra desejada para o metodo one hot, ou seja, a palavra desejada passa a ser representada por uma matriz onde cada linha representa uma letra e cada coluna uma posição. 
      Ou seja:
      
                  M(i,j) = []
                  onde i = letra, j = posição
      
      2. Logo após, multiplicamos a matriz M pela inversa da matriz "P", que nada mais é do que a permutação da matriz identidade. Isso com a finalidade de desembaralhar as linhas e colunas da matriz original:
                  
                  (P^-1)M
      
      3. Por fim, para que nosso enigma seja resolvido, utilizamos uma segunda matriz "E" (uma outra permutação da matriz identidade):
      
                  ((E^-1)^n)PM
                  onde n corresponde a j.
                  
       Dessa forma, acabamos por decriptografar nosso enigma, obtendo a mensagem inicial.


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


