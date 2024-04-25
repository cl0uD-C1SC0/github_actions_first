<div align="center">
<img src="../images/SENAI-Logo.png" height="100">
</div>

<h1 align="center"> Sobre a infraestrutura </h1>

## 01 - Infraestrutura (Básico)

> A infraestrutura sempre deverá seguir um padrão de acordo com a empresa, mas geralmente tende a se separar em três ambientes: <br>
>> * **Produção**: Ambiente que deve ser altamente escalável, com tipos de máquinas mais fortes e deverá ter uma arquitetura resiliente e sempre baseada em segurança; <br><br>
>> * **Homologação**: Ambiente de homologação de aplicações, softwares, é onde é testado o quanto uma aplicação aguenta, testes de segurança, testes de latência, caso passe em todos os processos a aplicação ira subir para a produção por meio de PULL REQUEST; <br><br>
>> * **Develop**: Ambiente de desenvolvimento, onde é "permitido" que as aplicações subam com vulnerabilidades, problemas de código, tudo isso para fins de validação da lógica, antes de subir para homologação, o código deverá estar nos padrões conforme as regras da empresa. <br><br>
>> * **OBS: A Infraestrutura sempre ira depender do orçamento do cliente, empresa ou time, não existe uma regra definida de como deve ser uma infraestrutura, mas existe boas práticas mediante a ela, veja mais abaixo.**

## 02 - Segurança da infraestrutura, contas e permissõs

> Construa sua infraestrutura pensando sempre na segurança;

> A infraestrutura deverá ser segura para que não ocorra falhas em produção, invasões de privacidade ou vazamento de dados sensíveis, pois, isso pode gerar custos graves a empresa;

> No quesito permissões, utilize o princípio de `Least Privilege` (Privilegio Mínimo), atribua somente as permissões necessárias e remova as não utilizadas. Nunca dê permissão para um usuário e sim o grupo de usuários;

> Na questão de contas, obrigue aos funcionários do time ou da empresa sempre utilizar MFA - Multi-Factor Authenticator;

> Jamais utilize a conta root para fazer qualquer tipo de tarefa e nunca compartilhe a senha da mesma ou de outras contas;

> Crie regras de segurança na rede restritas, por exemplo, nunca utilize a porta 22 para SSH, troque-a. Configure regras na ACL de rede ao invés do grupo de segurança, para que aplique para todos na rede.

## 03 - Resiliência + Custos

> Uma infraestrutura com mais resiliência é uma infraestrutura capaz de se recuperar de possíveis desastres;

> Prepare a infraestrutura para aguentar a carga de trabalho, mas jamais abuse disso pois pode gerar custos altos;

> Assegure-se que a infraestrutura tenha backup para eventuais falhas por exemplo no banco de dados;

> Utilize instâncias grandes mas apenas suficiente para evitar custos demasiadamente altos;

> SEMPRE que possível coloque TAG em seus recursos para facilitar o GERENCIAMENTO DE CUSTOS por meio de tags;

> Crie budgets (orçamentos) para todo tipo de projeto, para evitar custos altos;

> Utilize e abuse do conceito `Chaos-engineering` (Engenharia do CAOS) para testar a resiliência de sua infraestrutura.

## 04 - Automatizações

> Automatize tarefas repetitivas para evitar falhas humanas;

> Utilize a cultura DevOps para facilitar o processo de desenvolvimento e garantir uma qualidade de entrega de software melhor;

> Crie automações robustas e dinâmicas para que funcione em qualquer tipo de software, nuvem, local;

> Menos e mais! Automações complexas geram manutenções prolongadas


## 05 - Monitoramento

> Monitore sua infraestrutura para saber o que está acontecendo, quando aconteceu para que você sempre fique informado do que está havendo com sua infraestrutura/aplicações;

> Utilize o monitoramento para "trackear" (rastrear) os custos, você pode desativar recursos que estão ociosos, e para descobrir quais recursos são esses, aplique o monitoramento;

> Utilize a cultura e boas práticas de SRE para facilitar a adoção da Observabilidade em sua empresa ou time;

> Crie alertas para que enviem notificações antes que um problema aconteça, exemplo: A Memória do servidor WEB está chegando perto do limite;

> Crie uma resposta a incidentes automáticas para resolver os problemas como por exemplo a falta de memória.

<div align="center">
<img src="../images/SENAI-Logo.png" height="100">
</div>

<br><br><br>
<div align="center">
<p>SENAI São Caetano do Sul - Informática - Escola Senai "Paulo Antonio Skaf"</p>
<p>Endereço: Rua Niteroi, 180 - Centro - São Caetano do Sul/SP</p>
<p>Copyright 2024 © Todos os direitos reservados.</p>
</div>