# Banco de Dados Distribuído

Este projeto foi um trabalho da disciplina de Sistemas Distribuídos do curso de Ciência da Computação da Universidade Federal de Uberlândia.

## CRUD 

A ideia é criar um servidor de banco de dados eficiente (multi-thread), do tipo chave:valor com as opções de um CRUD: Create, Read, Update e Delete.
Todo o projeto foi feito em Python, na versão 3. 
O servidor aceita conexões por RPC (Remote Procedure Call) e executa as operações retornando para o cliente os status de sua requisição: se foi bem sucedida ou não.

## Cliente

O cliente é inicializado a partir do arquivo client.py e as configurações são lidas de um arquivo na pasta configs.

Caso o arquivo de configuração seja excluído por acidente, o próprio código cria uma configuração padrão para a conexão com o servidor. E caso o servidor esteja também executando em sua configuração padrão o serviço deverá funcionar.

## Servidor

