Para iniciar o projeto será preciso a criação de um ambiente virtual
Comandos:

Windows: Py -m venv env
Obs: "env" é o nome do seu ambiente virtual onde pode ser nomeado da forma que você quiser
Ativação da env: env/scripts/activate

Linux: python3 -m venv env
Obs: Aqui também o nome "env" pode ser da maneira que você achar melhor
Ativação: source env/scripts/activate

Assim que criar seu ambiente virtual clqiue "Ctrl" + Shift + P

- Vá em "Python: Select interpreter"
- Selecione o ambiente, onde deve estar assim: Python 3.XX.X ('venv':venv)
  Assim que selecionado você pode avançar para o próximo passo.

------------------------------------------------------------------------------------------------------------------------

COMANDOS PIP:

pip install fastapi - onde será construido nossa api
pip install tortoise-orm - É um ORM para python inspirado no Django otimizado para uso de framework como FASTAPI
pip install uvicorn - Uvicorn se trata de um servidor que será hospedado de forma local nossa api
