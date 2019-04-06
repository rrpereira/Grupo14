# Aula 8

## Pergunta 1.1

A função createGenesisBlock foi alterada de maneira a que o timestamp represente o momento de criação do bloco e que o seu dado seja "Bloco inicial da koreCoin".Em baixo encontram-se as alterações efetuadas ao código.

```python
createGenesisBlock(){
    	var date = new Date(Date.now()).toLocaleString()
        return new Block(0,date, "Bloco inicial da koreCoin", "0");
    }
```

## Pergunta 1.2

Foi adicionado o seguinte código de maneira a adicionar alguns blocos constituídos por varias transações.

``` python
koreCoin.addBlock(new Block (4,new Date(Date.now()).toLocaleString(), {t1: 140,t2: 559,t3: 1000}));
koreCoin.addBlock(new Block (5,new Date(Date.now()).toLocaleString(), {t1: 40,t2: 2000}));
```

## Pergunta 2.1

Usando o comando `time node main.experiencia2.1.js ` 

***Dificuldade 2***

``` 
Mining block 1...
Block mined: 007abd29e589b6a35f6107095cbc8a3628b7a8ff9ac5f7a203f79b262fff077e
Mining block 2...
Block mined: 009d3e5e004957e04604a4032cc58a97f33adb6711f93bc7514de8fe4a531a37
Mining block 3...
Block mined: 004bb82a658a99fd8c9f0d40ec9e69d3a441dacb6383242659b1ff8f7b42195b

real	0m0,154s
user	0m0,169s
sys		0m0,017s
```



***Dificuldade 3***

```
time node main.experiencia2.1.js 
Mining block 1...
Block mined: 0007c25169f5256ebb80fcbb423b582a8e699a759e41abb28906295973f9de4c
Mining block 2...
Block mined: 0004af57b70136e9f4b5309f92d518b3f297168d4cf47d4f9354808daadce457
Mining block 3...
Block mined: 00075796ab77bb5289bb9a952b91047482b3348d54d915ff5e5bce28256d01fe

real	0m0,640s
user	0m0,722s
sys		0m0,039s
```



***Dificuldade 4***

```
time node main.experiencia2.1.js 
Mining block 1...
Block mined: 0000023168f87d968813b22c4dc92f60c127ff5084af8487d913d497ea7a7900
Mining block 2...
Block mined: 00008e0c291aaf728e015855328b14e651231cce209e6413503fd299e0df6c5e
Mining block 3...
Block mined: 0000fb4a126ef4c1c3c93bf2ed25e8db4c7da2ec89a46aad4f7bf092afd8b6b4

real	0m2,994s
user	0m3,158s
sys		0m0,060s
```



***Dificuldade 5***

```
Mining block 1...
Block mined: 0000023168f87d968813b22c4dc92f60c127ff5084af8487d913d497ea7a7900
Mining block 2...
Block mined: 000000b950a180294edddf4340a2d5834119a41bf89e4b2027f341f0fc02365e
Mining block 3...
Block mined: 0000088dc9c3115ee6ab7e95d2e8836f932d75d303ab451a825241acde589a58

real	0m40,163s
user	0m40,995s
sys		0m0,382s
```



A dificuldade do algoritmo esta associada ao numero de zeros de prefixo que o valor de hash gerado tem de ter para ser aceite.Deste modo á medida que a dificuldade aumenta o numero de tentativas que têm de ser efetuadas para obter um hash valido aumenta consideravelmente resultando assim num tempo de execução mais elevado.



## Pergunta 2.2

### *1-*

 O algoritmo proof of work começa por inicializar um contador incrementado 1 ao valor do ultimo proof of work e de pois vais incrementando este contador até encontrar um numero que seja simultaneamente divisível por 9 e pelo ultimo proof of work.

Em baixo é apresentada a função que define o proof of work.

```python
def proof_of_work(last_proof):
  incrementor = last_proof + 1

  while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
    incrementor += 1
    
  return incrementor
```

### *2-*

​	 Este algoritmo não é o mais adequado uma vez que não é possível definir a dificuldade do puzzel a resolver.A dificuldade do puzzel ira crescer rapidamente uma vez que quanto maior fica a blockchain maior será a dificuldade de encontrar um numero divisível por 9 e pela ultima prova,levando assim a que seja necessário um elevado poder computacional para publicar blocos quando a blockchain já é grande..Para além disso o facto do proof of work ter em conta o valor da ultima prova traz vantagens para quem publicou o ultimo bloco e permite que o calculo da prova dos blocos seguintes possa ser calculada antes destes serem publicados 