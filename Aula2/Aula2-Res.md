## P1.1


Com a execução destes comandos verificamos que quando utilizado o /dev/random para um numero reduzido de bytes,32 e 64,a geração é imediata enquanto que para um numero mais elevado de bytes, 1024, o tempo para a geração é bastante elevado,isto deve-se ao facto de o /dev/random bloquear até obter a entropia necessária para geração de um numero pseudo-aleatório.
    
Quando utilizado o /dev/urandom a geração do numero pseudo-aleatório é imediata independentemente do numero de bytes uma vez que não bloqueia ate obter entropia necessária, no entanto o resultado contem uma entropia menor do que o numero pseudo- aleatório gerando usando o /dev/random.
    
    
## P1.2

Após instalar o haveged a execução do comando   /dev/random foi imediata, uma vez que o haveged é um deamon que auxilia na coleta de entropia,sendo que quando não existe entropia suficiente para gerar o numero pseudo-aleatório o deamon irá escrever em /dev/random fornecendo os bits pseudo aleatórios necessários para a geração.
No caso do comando /dev/urandom a geração do numero é imediata como anteriormente.

## P1.3

 1 - O output deste programa apenas contem letras e dígitos uma vez que a a função generateSecret() gera uma string aleatória com recurso a string.ascii_letter e string.digits que apenas contem letras e dígitos

 2 - Para não limitar o output a letras e dígitos a função a generateSecret() deve ser alterada para utilizar base64,sendo assim a função bas64.b64encode() deve ser aplicada ao resultado obtido em utils.generateRandomData(secretLength).
  
## P2.1

A - Para a geração do segredo partilhado foi utilizado o seguinte comando *python createSharedSecret-app.py 8 5 1 key.pem* e de seguida inserida a passphare da chave e o segredo "Agora temos um segredo extremamente confidencial".


B - Para que seja possível recuperar o segredo podem ser utilizados os comandos *python recoverSecretFromComponents-app.py 5 1 key.crt* que recupera o segredo a partir de alguns dos intervenientes,defendidos inicialmente como 5(quorum).Ou utilizando o comando  *python recoverSecretAllFromComponents-app.py 8 1 key.crt* que recupera o segredo a partir de todos os intervenientes.
O comando recoverSecretAllFromComponents deve ser utilizado quando o nivel de segurança associado ao segredo é elevado,uma vez que serão necessarios todos os intervenientes para descoficar o segredo.



## P3.1

A empresa deveria utilizar o esquema de Authenticated Encryption Encrypt-then-Mac que garante a integridade e autenticidade do texto limpo bem como do criptograma.Outra opção seria utilizar modes de operaçao de algumas cifras que oferecem garantias confidencialidade,integridade e autenticidade como é o caso do Galois Counter Mode (GCM) do AES.
Em baixo mostramos o algoritmo que utiliza o esquema Encrypt-and-Mac utilizando as funçoes defenidas pela API.Foi também defenida uma funçao auxiliar get_day_key(day) que recebe um dia do ano no formato "ano.mes.dia" e retorna a chave gerada para esse dia.

```python
def encrypt (message, etiqueta):
    ciphertext = cifragem(mensagem)
    key = get_day_key(today)
    mac = hmac(key,cyphertext)
    obj = {'mess' :ciphertext ,
		'MAC' :mac,
		‘tag’ :etiqueta ,
		’date’:today}
    return obj
        
def decrypt(ciphertext,mac,etiqueta,date):
    key= get_day_key(date)
    if(hmac(key,ciphertext)==mac):
     mes = decifragem(ciphertext,key)
	 return mes
    else:
      print("Authentication Failed")
```

## P4.1

As Entidades de Certificação que foram designadas ao nosso grupo foi a Dirección General de la Policía e a  Fábrica Nacional de Moneda y Timbre.Estas entidades utilizam os seguintes algoritmos e tamanhos de chave:   

 	Dirección General de la Policía
 	Signature Algorithm: sha256WithRSAEncryption
 	Public Key Algorithm: rsaEncryption
     Public-Key: 4096 bit


 	Fábrica Nacional de Moneda y Timbre
 	Signature Algorithm: sha256WithRSAEncryption
 	Public Key Algorithm: rsaEncryption
     Public-Key: 3072 bit

Os tamanhos de chaves utilizados por ambas as entidades são adequados para um futuro próximo,no entanto a longo prazo o tamanho de chave utilizado no RSA poderá ter de ser alterado até um máximo de 15360 bits que segundo o NIST contem o mesmo nível de segurança que uma chave simétrica de 256 bits.
Os algoritmos de assinatura também deverão ser substituídos por Sha-512 para garantir um nível de segurança aceitável a longo prazo.
