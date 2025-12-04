# 🏦 Desafio de Código — Sistema Bancário

Este projeto implementa um sistema bancário simples, seguindo as regras propostas no desafio.  
O foco principal é a separação das operações bancárias em funções independentes e o uso correto dos tipos de passagem de argumentos.

---

## ✅ Funcionalidades Implementadas

### 👤 Cadastro de Usuário (Cliente)
- Armazena nome, data de nascimento, CPF e endereço.
- Impede cadastro duplicado pelo CPF.

### 🏛 Cadastro de Conta Bancária
- Cada conta é vinculada a um cliente existente.
- Número da conta gerado automaticamente.
- Armazenamento em estrutura de dados interna.

### 💰 Operações Bancárias

#### **Depósito**
- Recebe argumentos **somente por posição**.
- Atualiza saldo e extrato.

#### **Saque**
- Recebe argumentos **somente nomeados** (*kwargs).
- Valida:
  - saldo insuficiente  
  - limite por saque  
  - limite diário de saques  

#### **Extrato**
- Recebe:
  - `saldo` → **por posição**
  - `extrato` → **por nome**
- Exibe todas as movimentações.

---

## ✅ Regras de Passagem de Argumentos

| Função | Tipo de Argumentos | Assinatura |
|-------|---------------------|------------|
| **saque** | keyword-only | `def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques)` |
| **depósito** | positional-only | `def deposito(saldo, valor, extrato, /)` |
| **extrato** | mixed | `def exibir_extrato(saldo, /, *, extrato)` |

---

## ✅ Outras Funcionalidades

- Modelos (`model`) para criação de **clientes** e **contas**.
- Listagem de clientes cadastrados.
- Listagem de contas existentes.
- Menu interativo para navegação entre operações.

---

## 🚀 Próximas Melhorias (Backlog)

- Seleção de conta quando o cliente possuir múltiplas contas.
- Busca de contas por CPF.
- Busca de contas por faixa de saldo.
- Ajuste de limite de saques por período (ex.: mensal).
- Persistência de dados em arquivo (JSON ou banco de dados).

---
