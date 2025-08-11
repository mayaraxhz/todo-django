**Documento de Requisitos AcheIF** 

**Documento de Requisitos** 

**1 Introdução** 

**1.1 Propósito do documento** 

Este documento propõe a especificação dos requisitos do sistema AcheIF, um sistema de gerenciamento de achados e perdidos, que será aplicado no IFRN. 

**1.2 Escopo do produto** 

O sistema tem como objetivo auxiliar na organização, controle e registro de objetos perdidos e encontrados dentro do IFRN. O gerenciamento completo será feito exclusivamente por usuários com perfil de administrador. 

**1.3 Visão geral do documento** 

Este documento apresenta uma visão geral do sistema, descrevendo suas funcionalidades e delimitações de requisitos, seja pelo contexto no qual será aplicado ou por questões de segurança. 

**2 Descrição Geral** 

O sistema AcheIF será utilizado por funcionários responsáveis pelo setor de achados e perdidos, bem como será acessível para usuários externos, mas com menos funcionalidades. Ele permitirá o cadastro, consulta, edição, exclusão e registro de devolução dos objetos encontrados. Usuários externos (alunos ou visitantes) não terão acesso direto ao sistema, mas poderão consultar objetos perdidos por meio de um terminal público ou site informativo (futuro recurso), bem como cadastrar. 

**2.1 Perspectiva do Produto** 

Todo o controle será feito por administradores logados, que poderão realizar todas as ações disponíveis no sistema, operando com banco de dados. 

**2.2 Restrições Gerais** 

O sistema só será acessado por administradores previamente cadastrados; Usuários não autenticados não poderão cadastrar informações; Todos os registros de objetos devem incluir data, descrição e local em que foram encontrados. 

**3 Requisitos** 

**3.1 Requisitos Funcionais** 

AcheIF 1.0 Documento de Requisitos.doc  
**Documento de Requisitos AcheIF** 

| RF001  | Cadastro de objetos encontrados por usuários e administradores |
| :---- | ----- |
| **Detalhes**  | Informar nome, descrição, data, local onde foi encontrado, categoria (roupa, eletrônico etc.) e status (aguardando devolução ou devolvido). |
| **Restrições**  | Nome e data do objeto são obrigatórios. |
| **Importância**  | **\[ X \] Obrigatório** \[ \] Importante \[ \] Desejável |

| RF002  | Consulta de objetos cadastrados |
| :---- | ----- |
| **Detalhes**  | Consulta por nome, categoria, local encontrado e status (devolvido ou não). |
| **Importância**  | **\[ X \] Obrigatório** \[ \] Importante \[ \] Desejável |

| RF003  | Administrador deve poder editar dados de objetos cadastrados |
| :---- | ----- |
| **Detalhes**  | Alterar descrição, local, categoria, status e observações. |
| **Importância**  | **\[X\] Obrigatório** \[ \] Importante \[ \] Desejável |

| RF004  | Administrador deve poder registrar a devolução de um objeto |
| :---- | ----- |
| **Detalhes**  | Inserir nome e CPF da pessoa que retirou, data da devolução e observações opcionais. |
| **Importância**  | **\[ X \] Obrigatório** \[ \] Importante \[ \] Desejável |

| RF005  | Administrador deve poder excluir registros de objetos |
| :---- | ----- |
| **Detalhes**  | Exclusão de objetos cadastrados por engano ou duplicados. |
| **Importância**  | **\[ X \] Obrigatório** \[\] Importante \[ \] Desejável |

| RF006  | Administrador deve poder gerar relatórios de objetos |
| :---- | :---- |

AcheIF 1.0 Documento de Requisitos.doc  
**Documento de Requisitos AcheIF** 

|  | perdidos e devolvidos |
| :---- | ----- |
| **Detalhes**  | Listagem por período, categoria e status. |
| **Importância**  | **\[ X \] Obrigatório** \[ \] Importante \[ \] Desejável |

| RF007  | Upload e manipulação de imagens |
| :---- | ----- |
| **Detalhes**  | Inserção e edição de imagens para complementação da interface gráfica. |
| **Importância**  | **\[ X \] Obrigatório** \[ \] Importante \[ \] Desejável |

| RF008  | Validações de formulários e tratamento de erros |
| :---- | ----- |
| **Detalhes**  | Verificação de dados antes de serem processados. |
| **Importância**  | **\[ X \] Obrigatório** \[ \] Importante \[ \] Desejável |

**3.1 Requisitos não Funcionais** 

| RNF001 | Terminal público ou site informativo |
| :---- | ----- |
| **Detalhes**  | Permite que usuários externos vejam os objetos que foram cadastrados após serem encontrados. |
| **Importância**  | **\[ X \] Obrigatório** \[ \] Importante \[ \] Desejável |

| RNF002  | Registro de login de usuários e administradores |
| :---- | ----- |
| **Detalhes**  | Identificação de acesso deve ser feito via login por  administradores e usuários. |
| **Importância**  | **\[ X \] Obrigatório** \[ \] Importante \[ \] Desejável |

| RNF003  | Serviço deve estar disponível 24 horas por dia |
| :---- | ----- |
| **Detalhes**  | Disponibilidade de acesso. |
| **Importância**  | **\[ X \] Obrigatório** \[ \] Importante \[ \] Desejável |

AcheIF 1.0 Documento de Requisitos.doc  
**Documento de Requisitos AcheIF** 

| RNF004  | Somente administradores podem ver e editar dados de objetos cadastrados |
| :---- | ----- |
| **Detalhes**  | Permite uma maior fidelidade dos dados, evitando que haja equívocos nas informações alteradas pelos demais usuários. |
| **Importância**  | **\[ X \] Obrigatório** \[ \] Importante \[ \] Desejável |

| RNF005  | Interface responsiva |
| :---- | ----- |
| **Detalhes**  | Adaptação a diferentes tamanhos de telas e dispositivos. |
| **Importância**  | **\[ X \] Obrigatório** \[ \] Importante \[ \] Desejável |

| RNF006  | Painel administrativo do Django configurado |
| :---- | ----- |
| **Detalhes**  | Registro dos models e configuração do ModelAdmin. |
| **Importância**  | **\[ X \] Obrigatório** \[ \] Importante \[ \] Desejável |

AcheIF 1.0 Documento de Requisitos.doc