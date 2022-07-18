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
  - `Numpy`

# Sumário

- [Instruções](#instruções)
- [Entendendo o projeto](#entendendo-o-projeto)

---

<p>&nbsp</p>

# Instruções:

Inicie clonando o repositorio para sua máquina local 
~~~
git clone git@github.com:Thales-Daniel/Project-Predict.git
~~~
Entre na pasta do repositorio que você acabou de clonar
~~~
cd Project-Predict/
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

O projeto foi pensado para praticar a linguagem Python e  tem como objetivo, prever os novos casos de covid dado um numero de dias

O output da sua função precisa dizer o número de dias à frente (calculado por D) e seu respectivo valor de casos.

Dado D=4, teremos:

1 -> 456\
2 -> 765\
3 -> 40\
4 -> 964

Dado esse exemplo, foi utilizado os dados do repositorio [owid/covid](https://github.com/owid/covid-19-data) para criar um calculo de previsão.

o calculo da previsão foi feita atraves do campo Reprodution_rate, onde esse campo contem a porcentagem
de contaminação baseado nos casos de contaminação do dia. Para calcular o desvio padrão, utilizei o Numpy, e com
esse desvio, consegui chegar no valor da varição sem deixala aleatoria.

Através dessas informações, consegui desenvolver uma formula para fazer o calculo dos novos casos logo a seguir:

![formula](https://user-images.githubusercontent.com/82240828/155584731-d939f781-ee26-4c6f-9045-fd38e2646183.png)

<p>&nbsp</p>
