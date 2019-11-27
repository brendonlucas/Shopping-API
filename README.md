# Shopping-API
<h3> O que é? </h3>
<ul>
  <li> Exemplificação de uma API de um Shopping de lojas. </li>
  <li> Onde o Shopping possue lojas, essas lojas possuem funcionarios e produtos. </li>
  <li> Clientes cadastrados poderão realizar compras nas lojas. As compras serão registradas por um funcionario da loja. </li>
</ul>

<h3> Requisitos </h3>
<ul>
  <li> Python 3.6 </li>
  <li> Django </li>
  <li> django_rest_framework </li>
  <li> Requests </li>
  <li> django-rest-swagger </li>
  <li> djangorestframework_simplejwt </li>
  <li> django-filter </li>
</ul>

<h3> Instalando Requisitos</h3>
<pre> <code> $ pip install -r requirements.txt </code> </pre>


<h3> Modelos de Json para realizar POSTs </h3>

 <h4> - Adicionar Loja </h4>
 <p> OBS: Somente um administrador do sistema poderá adicioniar uma Loja. </p>
    <pre> <code>  {
  "name": "string",
  "local": "string",
  "cnpj": "string"
}</code> </pre>
  
 <h4> - Adicionar Funcionario à uma Loja </h4>
 <p >OBS: Em 'cargo' a entradas tem que ser Funcionario ou Chefe.</p>
 <p> OBS 2: Somente Administrador ou o Chefe da Loja poderá adicionar um Funcionario à Loja. </p>
    <pre> <code>  
{
    "name": "string",
    "cpf": "string",
    "telefone": "string",
    "endereco": "string",
    "cargo": "string",
    "complemento": {
        "username": "string",
        "password": "string",
        "email": "string"
    }
}</code> </pre>
    
 <h4> - Adicionar um Produto à uma Loja </h4>
  <p> OBS: Funcionarios e Chefe da Loja podem adicionar Produtos. </p>
    <pre> <code> {
  "name": "string",
  "quantidade": 0,
  "valor": 0
}</code> </pre>
    
 <h4> - Adicionar Cliente </h4>
  <p> OBS: Administrador, Funcionario e Chefe da Loja poderá adicioniar um Cliente. </p>
    <pre> <code> 
{
    "name": "string",
    "cpf": "string",
    "telefone": "string",
    "endereco": "string",
    "email": "string"
} </code> </pre>
    
 <h4> - Adicionar uma Compra </h4>
  <p> OBS: Funcionario e Chefe da Loja podem adicionar uma Compra. </p>
    <pre> <code> {
    "cliente": {
        "name": "name",
        "cpf": "cpf"
    },
    "quantidade": 0
} </code> </pre>
  


<h3> Video demonstração </h3>
<ul>
 <li> Loading...... </li>
</ul>
