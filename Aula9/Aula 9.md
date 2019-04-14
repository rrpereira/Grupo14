
# Aula 9

## Pergunta 1.1

### *1-*

Qualquer software desenvolvido contem em media entre 5 e 50 bugs por cada 1000 linhas de código (SLOC),para estimar o numero de bug presentes no software iremos considerar que software normal contem 50 bugs/1000 SLOC e software desenvolvido com métodos rigorosos contem apenas 5 bugs/1000 SLOC

+ O **Facebook** é um software considerado normal sendo que em 62 milhões de  SLOC devera conter cerca de  3 milhões e 100 mil bugs .

+ O **software de automóveis** é normalmente desenvolvido com métodos rigorosos sendo que em 100 milhões de SLOC contem cerca de  500 mil bugs.

+ O **Linux 3.1**,sendo que é um sistema operativo foi desenvolvido com métodos rigorosos logo em 15 milhões de SLOC contem  75 mil bugs

+ Os **serviços Internet da Google** são considerados software normal sendo que em 2000 milhões de SLOC contem cerca de  100 milhões de  bugs

### *2-*

Não é possível saber quantos dos bugs serão vulnerabilidades,uma vez que o numero de bugs não esta diretamente relacionado com o numero de vulnerabilidades.

## Pergunta 1.2

#### Vulnerabilidades de Projeto	

 * **Improper Input Validation** acontece quando uma aplicação não valida ou valida incorretamente dados de input o que pode afetar a control flow e data flow do programa.Para resolver esta vulnerabilidade deve ser implementada uma política rigorosa de validação de input.

   

 * **Storing Passwords in a Recoverable Format** Esta vulnerabilidade permite que sejam efetuados ataques de reutilização de password,se um administrador de sistema conseguir recuperar a password de um utilizador pode depois utilizá-la em outras contas do utilizador.Para evitar esta vulnerabilidade deve ser guardado um hash da password, a partir do qual a password não pode ser recuperada e a validação do utilizador efetuada comparando o hash da password inserida com a hash guardada. 		

#### Vulnerabilidades de Codificação

 + **Missing Check for Certificate Revocation after Initial Check** Esta vulnerabilidade ocorre quando o software não verifica o estado de revogação de um certificado após a verificação inicial,isto possibilita que o software efetue operações com elevados privilégios utilizando o certificado mesmo depois de este ser revogado.Para evitar esta vulnerabilidade o estado de revogação do certificado deve ser verificado antes de efetuar qualquer operação.

   

 + **Execution with Unnecessary Privileges**  Esta vulnerabilidade ocorre quando o software executa operações com um nível de privilégios mais elevado do que o necessário, o que possibilita a existência de outras vulnerabilidades uma vez que quando o software é executado com elevado nível de privilegio as verificações de segurança normalmente efetuadas pelo sistema operativo podem não ser efetuadas.Para evitar esta vulnerabilidade o software devera  ter  apenas o nível mínimo de privilégios necessários para as operações que tem de efetuar.

#### Vulnerabilidades operacionais

+ **Information Exposure Through an Error Message**  Esta vulnerabilidade ocorre quando o software gera mensagens de erro que incluem informação sensível sobre o ambiente de execução ,utilizadores ou outras informações.Esta informação pode ser ela mesma valiosa no caso de serem passwords ou pode revelar informação que permite que o atacante efetue um ataque mais focado.Para evitar esta vulnerabilidade deve ser revelado o mínimo de informação possível em mensagens de erro.

    

+ **Information Exposure Through Directory Listing** Esta vulnerabilidade ocorre quando o conteúdo de uma diretoria se encontra exposto revelando informação sensível para os atacantes,o risco associado depende do tipo de ficheiros que acessíveis  a uma atacante.Para evitar esta vulnerabilidade pastas com conteúdo sensível não devem estar disponíveis para visualização. 

  ​	

## Pergunta 1.3

Uma vulnerabilidade de dia-zero destinge-se das outras vulnerabilidades pois é uma vulnerabilidade apenas conhecida num meio restrito,não tendo um CVE associado, sendo assim a maior parte da comunidade não a conhece.Estas vulnerabilidades podem ser utilizadas em meios militares como ciber-armas ou então utilizadas para ataques informáticos,permitindo atacar sistemas que sejam administrados por equipas de segurança competentes uma vez que estes não tem conhecimento da vulnerabilidade.As vulnerabilidades dia-zero são normalmente vendidas no mercado negro por elevadas quantias uma vez que são uma informação bastante valiosa.