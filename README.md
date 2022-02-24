# Boas vindas ao repositório do projeto Predict!

Esse projeto foi desenvolvido em Python.
O propósito é criar uma previão baseada em dados de quantos casos de covid irão surgir em determinados dias.
<div align="center">
  <img alt="python" height="60" width="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" />
  <br />
  <br />
</div>


Foram utilizadas 2 bibliotecas para auxiliar o desenvolvimento do projeto 
  - `Flake8`
  - `Pytest`

# Sumário

- [Instruções](#instruções)
- [Entendendo o projeto](#entendendo-o-projeto)
- [Executando o projeto](#executando-o-projeto)
- [Proximos passos](#proximos-passos)
- [Agradecimentos](#agradecimentos)

---

<p>&nbsp</p>

# Instruções:

Inicie clonando o repositorio para sua máquina local 
~~~
git clone git@github.com:Thales-Daniel/d3-aplication.git
~~~
Entre na pasta do repositorio que você acabou de clonar
~~~
cd d3-aplication/
~~~
Logo em seguida, use o .venv para criar o ambiente virtual
~~~
python3 -m venv .venv && source .venv/bin/activate
~~~
Apos isso, instale as dependecias do projeto
~~~
python3 -m pip install -r requirements.txt
~~~
Para fazer a execução do projeto, esteja na pasta do repositorio e utilize o comando no terminal
~~~
python3 predict.py
~~~
---

<p>&nbsp</p>

# Entendendo o projeto

O projeto tem como objetivo, prever os novos casos de covid dado um numero de dias

O output da sua função precisa dizer o número de dias à frente (calculado por D) e seu respectivo valor de casos.

Dado D=4, teremos:

1 -> 456\
2 -> 765\
3 -> 40\
4 -> 964

Dado esse exemplo, foi utilizado os dados do repositorio [owid/covid](https://github.com/owid/covid-19-data) para criar um calculo de previsão.

o calculo da previsão foi feita atraves do campo Reprodution_rate, onde esse campo contem a porcentagem
de contaminação baseado nos casos de contaminação do dia. Para não deixar o valor da estatico, verifiquei
quais eram as taxas de variação que mais se repetiam e adicionei elas aleatoriamente ao valor da media, dando assim
o valor que iriamos multiplicar pelo numero de casos do dia passado.

Através dessas informações, consegui desenvolver uma formula para fazer o calculo dos novos casos logo a seguir:

![formula cortada](https://user-images.githubusercontent.com/82240828/155482582-af3a3470-bd53-40d2-8b6a-3acad4729c7e.PNG)

OBS: como o covid vai estar sempre espalhado por ai, foi adicionado um algoritimo para gerar casos casuais iguais a gripe.

<p>&nbsp</p>

# Executando o projeto

Seguindo as instruições e executando o projeto o resultado deve ser o seguinte:

![executandoPredict](https://user-images.githubusercontent.com/82240828/155489643-cb89ffb4-9dc1-41f9-a358-4055bfc4f886.gif)

caso seja inserido uma string ou um numero menor que zero, o resultado é o seguinte:

![errorAoExecutar](https://user-images.githubusercontent.com/82240828/155505154-cdb5b19f-cf07-4251-b1ca-3f0d666eebe5.gif)

# Proximos passos

Caso o projeto tivesse uma duração maior, iria fazer a melhoria na logica utilizada na função, substituiria o "for" utilizado no arquivo predict.py por algo
que seja menos complexo de ler. Alem disso, tentaria fazer uma formula mais coesa com a realidade, adicionando várias condições para casos de novas mutações na doença ou eventos incomuns.


# Agradecimentos

Queria agradecer a d3 por ter me dado a essa oportunidade, aprendi bastante com o projeto e pretendo aprender mais no futuro com os projetos seguintes.

