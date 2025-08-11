**Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte**  
 **Disciplina: Projeto de Desenvolvimento de Software**  
 **Alunos: Dávila Itauana de Sousa Bento e Mayara Evelyn Nunes** 

**Sistema AcheIF – Achados e Perdidos**

#### **Atores do Sistema**

* **Administrador:** É o funcionário responsável pelo controle do sistema de achados e perdidos. Possui acesso total ao sistema, podendo cadastrar, editar, excluir, consultar, registrar devoluções, gerar relatórios, inserir imagens e validar dados.  
* **Usuário Externo (Aluno ou Visitante):** Não possui acesso direto ao sistema interno. Pode apenas consultar objetos perdidos por meio de um terminal público ou site informativo. Em versões futuras, poderá cadastrar objetos encontrados para análise e validação.

### **Casos de Uso**

#### **Administrador:**

* **Cadastrar objeto encontrado:**  
   O administrador pode registrar um novo objeto perdido, preenchendo informações como nome, descrição, data, local, categoria (como roupa, eletrônico etc.) e status (aguardando devolução ou devolvido). O nome e a data do objeto são obrigatórios.  
* **Consultar objetos cadastrados:** O administrador pode realizar buscas por nome, categoria, local onde foi encontrado e status (devolvido ou não) para verificar os objetos no sistema.  
* **Editar dados de um objeto:** O administrador tem permissão para alterar os dados de objetos já cadastrados, como descrição, local, categoria, status e observações.  
* **Registrar devolução de objeto:** Ao devolver um objeto ao seu dono, o administrador deve registrar o nome e CPF da pessoa que fez a retirada, a data da devolução e, opcionalmente, observações.  
* **Excluir objeto do sistema:** Objetos cadastrados por engano ou em duplicidade podem ser removidos do sistema pelo administrador.  
* **Inserir e editar imagens:** O sistema permite ao administrador complementar os registros com imagens dos objetos, que podem ser inseridas ou alteradas posteriormente.  
* **Gerar relatórios:** O administrador pode gerar relatórios com listagens de objetos perdidos ou devolvidos, filtrando por período, categoria ou status.

#### **Usuário Externo (Aluno ou Visitante):** 

* **Consulta pública de objetos encontrados:** Usuários externos podem consultar os objetos disponíveis utilizando um terminal público ou site informativo, sem a necessidade de autenticação.  
* **Cadastrar objeto encontrado:** usuários externos poderão cadastrar objetos encontrados por meio de um formulário, sujeito à validação pelo administrador.


