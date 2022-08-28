# aluraChallenge_BkEnd_04
#alurachallengebackend4

<h3>Introdução do Challenge</h3>
<p>Após alguns testes com protótipos feitos pelo time de UX de uma empresa, foi requisitada a primeira versão de uma aplicação para controle de orçamento familiar.</p>
<p>A aplicação deve permitir que uma pessoa cadastre suas receitas e despesas do mês, bem como gerar um relatório mensal.</p>
<p>Os times de frontend e UI já estão trabalhando no layout e nas telas. Para o back-end, as principais funcionalidades a serem implementadas são:</p>
<ul>
<li>1 - API com rotas implementadas seguindo as boas práticas do modelo REST;</li>
<li>2 - Validações feitas conforme as regras de negócio;</li>
<li>3 - Implementação de base de dados para persistência das informações;</li>
<li>4 - Serviço de autenticação/autorização para restringir acesso às informações.</li>
</ul>  
<h3>Métodos aplicados</h3>
<p>Projeto em Linguagem Python com Django Rest Framework</p>

<h3><strong>Semana 1</strong></h3>
<p>Criando banco de dados de Receitas e Despesas</p>
<ul>
    <li>id</li>
    <li>descrição</li>
    <li>valor</li>
    <li>data</li>
</ul>
<p>Listagem dos dados com método GET e requisições do tipo POST para os endpoints /receitas e /despesas</p>
<p>Corpo resposta do metodo GET em formato JSON</p>
<p>Aplicação dos métodos GET, PUT e DELETE para os endpoitns /receitas{id} e /despesas{id} </p>

<h3><strong>Semana 2</strong></h3>
<p>Mudanças no banco de dados: Adição de categorias para cada class</p>
<p>Adição de endpoint de busca por descrição por método GET /despesas?descricao=xpto </p>
<p>Adição de endpoint de busca por descrição por método GET /receitas?descricao=xpto </p>
<p>Listagem das classes por mês com por método GET /despesas/{ano}/{mes} e /receitas/{ano}/{mes}</p>
<p>Adição de class Resumo com endpoint GET /resumo/{ano}/{mes}</p>
<p>Devolvendo:</p>
<ul>
    <li>Valor total das receitas do mês</li>
    <li>Valor total das despesas do mês</li>
    <li>Saldo final do mês</li>
    <li>Valor total gasto por catedoria de despesas no mês</li>
</ul>
<h3><strong>Semana 3 e 4</strong></h3>
<p>Adcionado sistema de autenticação e criação de usuarios</p>
<ul>
    <li>Com <strong><em>Django.contrib.auth.models.User</em></strong></li>
</ul>
<ul>
<p>Atribuição de usuarios autenticados</p>
    <li>Ler, adcionar e modificar, receitas e despesas</li>
</ul>
<p>Deploy da Api utilizando <a href="https://financeiro-challenge.herokuapp.com/">Heroku</a></p>