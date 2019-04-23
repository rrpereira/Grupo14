## Aula 10

#### Pergunta P1.1

A formula de risco presentada  tem em conta os seguintes paramentos

+ Probabilidade de ataque bem sucedido
+ Impacto

Sendo que probabilidade de ataque bem sucedido está relacionado com o **nível de ameaça** e o **grau de vulnerabilidade** de uma maquina. O *servidor de homebanking* apresenta um nível de ameaça superior ao de um PC domestico uma vez que contem informação bastante sensível sobre um elevado numero de utilizadores. Por outro lado o grau de vulnerabilidade deverá ser bastante menor do que o PC domestico, uma vez que existe um conjunto de requisitos que tem de ser preenchidos para o armazenamento e processamento de dados pessoais por parte do *servidor de homebanking* que o PC domestico não tem em conta.

Relativamente ao impacto de um ataque, este será maior no *servidor de homebanking* uma vez que contem informação mais sensível que o PC domestico e que abranja um maior numero de utilizadores.Tendo este dois parâmetros em consideração podemos afirmar que o *servidor de homebanking* esta sujeito a um maior risco. 



#### Pergunta P2.1

O RGPD deve ser tomando em conta na **Fase de Definição de Requisitos** do *Microsoft Security Development Lifecycle*, nesta fase são definidos os requisitos mínimos de segurança do projeto tendo como base a legislação em vigor e as normas e recomendações internacionais.  



#### Pergunta P2.2

Os controlos de segurança presentes na secção *Security in development and support processes* são os seguintes:

+ **Secure development policy** - Regras de desenvolvimento seguro de software devem ser estabelecidas e aplicadas ao desenvolvimento dentro de uma organização.

+ **System change control procedures** - A introdução de novos sistemas ou mudanças significativas ao sistema existente deve ser acompanhada de um processo de documentação, especificação, testes e controlo de qualidade para garantir a integridade do sistema. 

+ **Technical review of applications after operating platform changes** - Quando as plataformas operacionais são alteradas as aplicações criticas devem ser revistas e testadas para garantir que as alterações não afetam as operações ou segurança da organização.

+ **Restrictions on changes to software packages** - A modificação de pacotes de software deve ser desencorajada,limitada a situações pontuais,sendo que todas as mudanças devem ser controladas.

+ **Secure system engineering principles** - Princípios de engenharia de sistemas seguros devem ser estabelecidos, documentados e aplicados na implementação de qualquer sistema de informação.

+ **Secure development environment** - A organização deve estabelecer e um ambiente seguro de desenvolvimento que preferencialmente envolva todo o ciclo de desenvolvimento. 

+ **Outsourced development** - A organização deve supervisionar as atividades de desenvolvimento quando este é *outsourced*.

+ **System security testing** - Testes ao funcionamento das medidas de segurança devem ser efetuados durante o desenvolvimento.

+ **System acceptance testing** - Devem ser efetuados teste de aceitação para novos sistemas de informação , upgrades ou novas actualizaçoes.



Na secção *Cryptographic controls* são apresentados mais dois controlos adicionais

+ **Policy on the use of cryptographic controls** - Deve ser desenvolvida e implementada uma política para a utilização de funcionalidades criptográficas para proteger os dados. 

+ **Key management** - Devem ser desenvolvidas e implementadas políticas relativa ao uso, proteção controlo de  tempo de vida de chaves criptográficas durante todo o lifecycle do projeto.

  

As políticas de controlo enunciadas acima são importante para garantir o desenvolvimento seguro de software, sendo que devem ser aplicadas no desenvolvimento de software independentemente de qual o produto final a ser desenvolvido.Relacionando a utilização destes controlos com o trabalho pratico da disciplina (Testes de Intrusão) conclui-se que a utilização destas regras por parte de uma organização dificultam o acesso e processo de comprometer o sistema uma vez que a segurança é tida em conta durante todo o processo desenvolvimento.   



#### Pergunta P3.1

As praticas de segurança que se destacaram após na fase *Assets* são

+ **Policy & Compliance** - com uma  maturidade de  2,25
+ **Environment Hardening** - com uma maturidade de 1,50
+ **Secure Architecture** - com uma maturidade de 1,60

#### Pergunta P3.2

Para as praticas de segurança identificadas na pergunta anterior será estabelecido o nível de maturidade pretendido.

- **Policy & Compliance** - pretende - se aumentar o nível de maturidade para 2,50 ou superior.
- **Environment Hardening** -  pretende - se aumentar o nível de maturidade para 2,00 ou superior.
- **Secure Architecture**-> pretende - se aumentar o nível de maturidade para 2,50 ou superior.



#### Pergunta P3.3

As alterações necessárias para atingir o  nível de maturidade pretendido nas praticas de segurança encontra-se no ficheiro[SAMM_Assessment.xlsx](SAMM_Assessment.xlsx) na *sheet* roadmap. 

