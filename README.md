# COMPILADORES-LABORATORIO-2

Crie um programa que recebe um arquivo de texto contendo palavras que serão reconhecidas por um AFD
Use as palavras do exercício 2 do laboratório anterior
Faça com que o AFD reconheça cada palavra contida nesse arquivo
Para cada palavra reconhecida, faça com que o AFD retorne um token (tupla <Tipo, Valor>)
Ou seja, atribua a cada estado final uma função de retorno do token
Exemplo:  
  <IF, “if”>
  <ELSE, “else”>
  <IDENTIFICADOR, “var1”>
  <INTEGER, “int”>
