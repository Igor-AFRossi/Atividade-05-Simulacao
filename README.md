# Atividade 05 - Simulação e Testes de Software

## Integrantes

- Adriel Foppa RA: 22.225.036-7
- Alan Mantelatto RA: 22.125.092-1
- Gustavo das Flores RA: 22.221.041-1
- Igor Rossi RA: 22.225.021-9
- Luca Anequini RA: 22.224.031-9


---

## Estrutura do Projeto

```
projeto_calculadora/
|-- src/
|   |-- calculadora.py     # Código da calculadora
|-- tests/
|   |-- __init__.py        # Arquivo vazio
|   |-- test_unidade.py    # Testes de unidade
|   |-- test_integracao.py # Testes de integração
|-- requirements.txt       # Dependências
|-- README.md              # Este arquivo
|-- relatorio.md           # Relatório dos testes
```

---

## Configuração do Ambiente

### 1. Criar ambiente virtual (opcional)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

---

## Execução dos Testes

### Rodar todos os testes
```bash
python -m unittest discover tests -v
```

### Rodar teste específico
```bash
python -m unittest tests.test_unidade.TestCalculadora.test_somar -v
```

---

## Cobertura de Código

### Executar testes com cobertura
```bash
coverage run -m unittest discover tests
```

### Relatório no terminal
```bash
coverage report
```

### Relatório em HTML
```bash
coverage html
```
Abra o arquivo `htmlcov/index.html` no navegador.

---

## Relatório de Testes

Um resumo da execução está em [`relatorio.md`](relatorio.md).
