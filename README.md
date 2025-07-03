# 🌊 FlowMang

Sistema web em Django para consultas de dados hidrológicos.

---

## ⚙️ Como rodar localmente

- Clone o repositório:

git clone https://github.com/SeuUsuario/FlowMang.git
cd FlowMang

- Crie o ambiente virtual e ative:

python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

- Instale as dependências:


pip install -r requirements.txt

- Aplique as migrações:


python manage.py migrate

- (Opcional) Crie um superusuário:


python manage.py createsuperuser

- Rode o servidor:

python manage.py runserver
Acesse: http://127.0.0.1:8000/

✅ Requisitos
Python 3.10+

Google reCAPTCHA keys (adicione no settings)



