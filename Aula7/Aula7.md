# Aula7

## Pergunta 1.1

#### The principle of purpose limitation

O principio da limitação de finalidade é um principio fundamental  da lei europeia de proteção de dados e pretende garantir transparência ,previsibilidade e controlo no processamento de dados pessoais.Este principio diz que o propósito pelo qual os dados serão processados tem de ser definido antes de se dar inicio ao processamento, para alem disso os dados não podem ser processados novamente com um propósito diferente do original,sendo que o regulamento de proteção de dados prevê exceções nos casos  do processamento ser efetuado para fins científicos/históricos bem como para fins estatísticos.

A legitimidade do processamento de dados pessoais depende da especificação explicita e previa da finalidade para qual estes dados irão ser processados,sendo assim o processamento sem uma finalidade definida previamente,apenas considerando que poderá ser úteis futuramente,é ilegal. 

Caso se pretenda processar dados pessoais para uma finalidade diferente da inicialmente definida é necessário que esta finalidade possua uma base jurídica especifica,ou seja a sua legitimidade não pode ser baseada no facto da finalidade inicial ser legal.Sendo assim a partilha de dados pessoais com terceiros tem de ser devidamente controlada uma vez que pode necessitar de uma base jurídica adicional. 

O regulamento geral de proteção de dados declara que o processamento de dados pessoais para fins científicos/históricos e fins estatísticos é a priori compatível com a finalidade inicial do processamento, sendo que devem ser tomadas medidas de segurança adicionais neste processamento,tais como anonimização , cifras e pesudo-anonimização dos dados.Para alem disso o titular dos dados deve ser informado da finalidade para qual os seus dados pessoais estão a ser processados bem como dos seus direitos,tais como o direto de recusar este processamento. 

## Pergunta 1.2

As oito estratégias de *privacy design* presentes no documento são divididas em duas categorias estratégias orientadas aos dados e estratégias orientadas ao processo.

#### Estratégias Orientadas aos Dados

1. **Minimizar**  - Esta estratégias recomenda que a quantidade de dados pessoais a ser processada deve ser restringida ao mínimo  possível.Utilizando esta estratégia tem que verificar-se  o processamento respeita a finalidade inicial com a qual foram recolhidos e se não existem métodos menos evasivos para atingir o objetivo.Os *design patterns* associados a esta estratégia são *"select before you collect"* , anonimização e pseudo-anannomização.

   

2. **Esconder** -  Esta estratégia recomenda que todos os dados pessoais e o seu relacionamento deve estar escondidos.Esta estratégia deve ser aplicada a dados coletados e guardados para futuro processamento,bem como a dados gerados pela utilização de um determinado sistema com o intuito de garantir confidencialidade.Os *design patterns* associados a esta estratégia são a utilizaçao de cifras em dados guardados ou gerados,anonimização e pseudo-anonimização

   

3. **Separar** -  Esta estratégia recomenda que os dados pessoais devem ser processados de uma forma distribuída sempre que possível.Separando o processamento e armazenamento de varias fontes de informação pessoal garante que um perfil completo de um individuo não pode ser criado.É também recomendado que o processamento e armazenamento dos dados seja local.Não existe nenhum *design pattern* para esta estratégia.

   

4. **Agregar** -  Esta estratégia recomenda que os dados pessoais sejam processados com um nível de agregação elevado e com o menor detalhe possível.Agregar a informação em grupos de atributos restringe o nível de detalhe a que a informação é processada, sendo assim a informação torna-se menos sensível se estiver agregada um grupo de grande dimensão,uma vez que a informação é valida para um conjunto grade de indivíduos e pouca informação pode ser extraída sobre uma única pessoa. Os *design patterns* associados a esta estratégia são agregação ao longo do tempo e anonimização.

   

#### Estratégias Orientadas aos Processos

1. **Informar** -  Esta estratégia corresponde a noção de transparência recomendando que os titulares dos dados pessoais sejam informados quando os seus dados forem processados.O titular deve ser informado da finalidade para qual os dados serão processados bem como informação de como os dados estão a ser protegidos e as medidas de segurança implementadas pelo sistema.Deve também ser informado dos seus direitos sobre os dados e como exercê-los, caso terceiros estejam envolvidos no processo de processamento esta informação também deve ser dada. Os *design patterns* associados a esta estratégia são efetuar notificações sempre que ocorre um *data breach* e outras técnicas que aumentam a transparência do processamento.

   

2. **Controlo** -  Esta estratégia recomenda que o titular dos dados tenha controlo sobre os seus dados,tendo o direito de visualizar, alterar e eliminar qualquer informação que coletada sobre ele.Por exemplo numa rede social a facilidade com que um utilizador altera os seus dados pessoais determina o nível de controlo.O *design pattern* associados a esta estratégia é a utilização de cifras fim a fim. 

   

3. **Aplicação** -  Esta estratégia recomenda a existência e aplicação de uma política de privacidade compatível com os requisitos legais. A existência de uma política de privacidade é importante para garantir que o sistema respeita a privacidade durante o processamento, sendo que o nível de proteção de privacidade dependerá da política aplicada. Os *design patterns* desta estratégia são o controlo de acesso e políticas de direitos de privacidade.

      

4. **Demonstrar** -  Esta estratégia obriga que o detentor dos dados demonstre que tem em vigor uma política de privacidade que preenche os requisitos legais.Podendo ser necessário demonstrar como a política de privacidade esta implementada nos sistemas informáticos.Os *design patterns* associados a esta estratégia são a utilização de sistemas de gestão de privacidade bem como registos e auditorias. 

   

## Pergunta 1.3

#### 1-

Para verificar se o processamento de dados pessoais irá resultar num elevado risco são considerados os seguintes nove critérios

+ **Evaluation or Scoring** - Efetuar um perfil de dados pessoais que inclua informação como situação económica,preferências ou crenças pessoais ou localização.  
+ **Automated-decision making with legal or similar significant effect ** - O processamento de dados   pessoais de forma automática pode tomar decisões com consequências jurídicas. 
+ **Systematic monitoring** - Refere-se ao processamento que monitoriza e controla dados pessoais contidos em plataformas de acesso publico. 
+ **Sensitive data or data of highly personal nature** - Corresponde ao processamento de dados de elevado carácter pessoal como convicções políticas, registo criminal,ou seja qualquer tipo de dados que possa ser diretamente ligado a atividades pessoais.
+ **Data processed on a large scale** - Corresponde ao processamento sobre um numero elevado de dados, ou que decorra sobre períodos de tempo extenso ou abranja uma elevada área geográfica.
+ **Matching or combining datasets** - Utilizar dados pessoais recolhidos em outros contextos e agrupá-los com os dados recolhidos pode resultar num processamento que ultrapassa o consentimento do titular.
+ **Data concerning vulnerable data subjects** - Corresponde ao processamento de dados pessoais de titulares que não conseguem opor ou autorizar o seu processamento.Estes titulares são normalmente crianças,idosos, utentes ou empregados. 
+ **Innovative use or applying new techonological or organisational solutions** -Novas tecnologias como reconhecimento facial e autentificação por impressão digital, representam um elevado risco para  dados pessoais.
+ Sempre que o processamento impedir que o titular dos dados possa exercer o seu direito sobre os mesmos.

#### 2- 

Neste exercício será utilizada como exemplo uma aplicação GPS que utiliza dados relativos á localização geográfica dos seus utilizadores.Visto que a localização do utilizador é considerada uma informação sensível sendo abrangida em alguns dos pontos mencionados na primeira alínea, tais como *Evaluation or Scoring* e *Sensitive data or data of highly personal nature,* será necessário medidas de segurança adicionais uma vez que o processamento destes dados tem um elevado risco de violar o regulamento geral de proteção de dados.

#### 3-

No ficheiro [DPIA.pdf](DPIA.pdf) encontra-se o DPIA do projeto.

## Pergunta 1.4

No ficheiro [PIA.pdf](PIA.pdf) encontra-se o PIA do projeto.
