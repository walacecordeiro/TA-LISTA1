# Desafio: Lista de Exercícios em Desenvolvimento - Nível 1

> Todos os exercícios devem ser feitos em Python usando tipagem das variáveis, inclusive nas passagens de parâmetro (entrada e retorno).

### Exercícios

1. Faça um programa que leia N números inteiros até que o usuário informe o número 0.Esses números devem ser jogados em uma lista. Após isso, faça as seguintes rotinas:

   - soma: recebe a lista e retorna a soma dos números.
   - multiplica: recebe a lista e retorna o produto dos números.
   - duplicados: recebe a lista e retorna uma lista com os números que aparecem mais de uma vez.
   - ímpares: recebe a lista e retorna uma lista com os números ímpares distintos.
   - pares: recebe a lista e retorna uma lista com os números pares distintos.
   - primos: recebe a lista e retorna uma lista com os números primos.
   - Crie um arquivo main.py e outro arquivo para as funções acima.
   - Imprima o resultado de cada item.

2. Repita o exercício acima usando comprehensions (não pode usar while nem for).

3. Faça um programa com uma função para tratar a entrada de números inteiros. A função pede um número até que o usuário informe um valor válido:

   ```` Python
   def peganumero(mensagem: str, mensagemerro: str) -> int
   ````

   - Parâmetros:
   - mensagem: mensagem para o input.
   - mensagemerro: mensagem de erro se o valor for inválido.
   - Coloque as funções em arquivos separados.

4. Melhore o programa anterior adicionando dois parâmetros: menorvalor e maiorvalor.

   - A função só retorna um inteiro válido dentro do intervalo [menorvalor, maiorvalor].
   - Se algum dos novos parâmetros for None, ignore o menor e/ou maior valor.

   ```` Python
   def peganumero(mensagem: str, mensagemerro: str, menorvalor: int, maiorvalor: int) -> int
   ````

5. Faça um programa que peça um número correspondente a um ano e informe se ele é bissexto.

6. Faça um programa que use uma lista como fila de banco:

   - Adicionar cliente: recebe um nome e adiciona na lista.
   - Atende cliente: retira o próximo da lista.
   - Fim: termina o programa.

        > Verificar se há elementos antes de retirar.

7. Faça o programa anterior usando a lista como pilha:

   - Adicionar cliente: recebe um nome e adiciona na lista.
   - Atende cliente: retira o último cliente adicionado.
   - Fim: termina o programa.

8. Faça um programa que leia uma string e imprima a string com a primeira letra de cada palavra em maiúscula.

   - Exemplo: "a casa amarela bonita" → "A Casa Amarela Bonita"

9. Faça um programa que leia uma string e imprima a string com a primeira letra de cada palavra em maiúscula, exceto preposições e artigos.

   - Exemplo: "a casa amarela da clara bonita" → "A Casa Amarela da Clara Bonita"
   - Neste exemplo as preposições e artigos não devem ter a primeira letra em maiúscula.
