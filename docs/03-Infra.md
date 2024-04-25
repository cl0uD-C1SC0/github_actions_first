<div align="center">
<img src="../images/SENAI-Logo.png" height="100">
</div>

<h1 align="center"> Sobre a infraestrutura </h1>

## 01 - Infraestrutura (Básico)

> A infraestrutura sempre deverá seguir um padrão de acordo com a empresa, mas geralmente tende a se separar em três ambientes: <br>
>> * **Produção**: Ambiente que deve ser altamente escalável, com tipos de máquinas mais robustos e uma arquitetura resiliente e sempre baseada em segurança; <br><br>
>> * **Homologação**: Ambiente de homologação de aplicações e softwares, onde são realizados testes de carga, segurança, e latência. Caso passe em todos os processos, a aplicação será promovida para produção por meio de PULL REQUEST; <br><br>
>> * **Develop**: Ambiente de desenvolvimento, onde é "permitido" que as aplicações subam com vulnerabilidades e problemas de código, para fins de validação da lógica. Antes de subir para homologação, o código deve estar em conformidade com os padrões definidos pela empresa; <br><br>
>> * **OBS: A Infraestrutura sempre ira depender do orçamento do cliente, empresa ou time, não existe uma regra definida de como deve ser uma infraestrutura, mas existe boas práticas mediante a ela, veja mais abaixo.**

## 02 - Segurança da infraestrutura, contas e permissõs

> Construa sua infraestrutura pensando sempre na segurança.

> A infraestrutura deve ser segura para evitar falhas em produção, invasões de privacidade ou vazamento de dados sensíveis, pois isso pode gerar custos graves para a empresa.

> No quesito de permissões, utilize o princípio de ``Least Privilege`` (Privilégio Mínimo), atribuindo somente as permissões necessárias e removendo as não utilizadas. Nunca dê permissões para um usuário individualmente, mas sim para grupos de usuários.

> Quanto às contas, exija que os funcionários do time ou da empresa sempre utilizem MFA - Multi-Factor Authenticator.

> Nunca utilize a conta root para realizar qualquer tipo de tarefa e nunca compartilhe sua senha ou de outras contas.

> Estabeleça regras de segurança na rede restritivas, por exemplo, evite utilizar a porta 22 para SSH, trocando-a por uma diferente. Configure regras na ACL de rede em vez do grupo de segurança, para que se apliquem a todos na rede.

## 03 - Resiliência + Custos

> Uma infraestrutura com mais resiliência é capaz de se recuperar de possíveis desastres.

> Prepare a infraestrutura para suportar a carga de trabalho, mas evite abusar disso, pois pode resultar em custos elevados.

> Assegure-se de que a infraestrutura tenha backups para lidar com eventuais falhas, como no banco de dados.

> Utilize instâncias grandes apenas quando necessário para evitar custos excessivos.

> Sempre que possível, adicione TAGs aos seus recursos para facilitar o GERENCIAMENTO DE CUSTOS.

> Crie budgets (orçamentos) para todos os tipos de projetos, a fim de evitar custos elevados.

> Utilize e explore o conceito de ``Chaos Engineering`` (Engenharia do Caos) para testar a resiliência de sua infraestrutura.

## 04 - Automatizações

> Automatize tarefas repetitivas para evitar falhas humanas.

> Adote a cultura DevOps para facilitar o processo de desenvolvimento e garantir uma melhor qualidade na entrega de software.

> Desenvolva automações robustas e dinâmicas que funcionem em qualquer tipo de software, seja na nuvem ou local.

> Lembre-se: menos é mais! Automações complexas geram manutenções prolongadas.


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