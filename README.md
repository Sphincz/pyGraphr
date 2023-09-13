## pyMazerr - Python Maze Generator
*Author: António Raimundo*

Código-base para a Unidade Curricular (UC)
de Inteligência Artificial do Iscte-Sintra.

### Configuração inicial
Têm de garantir que possuem os seguintes requisitos para poderem importar corretamente
o projeto-base para o vosso IDE (Visual Studio Code / PyCharm):
1. Ter a versão Python 3.10 ou superior instalada nas vossas máquinas.
2. Criar um ambiente virtual específico para este projeto. Para tal,
executem algumas operações:
   1. Atualizem a versão do Python Package Manager (pip): ``pip install --upgrade pip``;
   2. Criação do ambiente virtual (**recomendado**): ``conda create -n NOME_ESCOLHIDO python=3.11``;
   3. Configurar interpretador no VS Code ou PyCharm (se fizeram todos os passos corretamente, deverá aparecer nos vossos IDEs o novo ambiente virtual que criaram).

Depois de terminarem a configuração inicial, prossigam para mais uns comandos adicionais:

### Comandos iniciais:
Para garantir que o projeto base inicia sem problemas, devem importar o projeto, e na console 
(garantir que estão localizados na **pasta principal - pyMazerr**)
executem os seguintes comandos:
1. ``python install -r requirements.txt``
2. ``python -m pip install -e .``