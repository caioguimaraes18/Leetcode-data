# SQL Practice Pack (estilo LeetCode) — Dataset + Exercícios

## Como usar (rápido)
- Importe cada CSV como uma tabela com o mesmo nome do arquivo:
  - departments.csv  -> departments
  - employees.csv    -> employees
  - person.csv       -> person
  - customers.csv    -> customers
  - orders.csv       -> orders
  - scores.csv       -> scores
  - logs.csv         -> logs

Se estiver usando SQLite:
- Dica: defina tipos simples (INTEGER, TEXT, REAL) e depois faça `import`.

---

## Exercícios

### 175. Combine Two Tables (Easy)
**Objetivo:** Liste `employees.name`, `departments.name` (como `department`) para cada funcionário.
- Join: employees.departmentId = departments.id

---

### 176. Second Highest Salary (Medium)
**Objetivo:** Retorne o 2º maior salário distinto da tabela `employees` (coluna `salary`).
- Se não existir, retorne NULL.

---

### 177. Nth Highest Salary (Medium)
**Objetivo:** Crie uma query (ou função, se seu SGBD permitir) que retorne o N-ésimo maior salário distinto de `employees`.
- Teste com N=1,2,3,4.

---

### 178. Rank Scores (Medium)
**Tabela:** `scores(id, score)`
**Objetivo:** Retorne `score` e o `rank` denso (dense rank) em ordem decrescente.
- Mesma nota -> mesmo rank; não “pula” números.

---

### 180. Consecutive Numbers (Medium)
**Tabela:** `logs(id, num)`
**Objetivo:** Encontre números que aparecem **pelo menos 3 vezes consecutivas** (por id crescente).
- Retorne apenas os números.

---

### 181. Employees Earning More Than Their Managers (Easy)
**Tabela:** `employees(id, name, salary, managerId, ...)`
**Objetivo:** Retorne os nomes dos funcionários cujo `salary` é maior que o salário do seu manager.

---

### 182. Duplicate Emails (Easy)
**Tabela:** `person(id, email)`
**Objetivo:** Retorne os emails que aparecem mais de uma vez.

---

### 183. Customers Who Never Order (Easy)
**Tabelas:** `customers`, `orders`
**Objetivo:** Retorne os clientes que **não** possuem pedidos.

---

### 184. Department Highest Salary (Medium)
**Tabelas:** `departments`, `employees`
**Objetivo:** Para cada departamento, retorne:
- department (nome)
- employee (nome do(s) funcionário(s) com maior salário no depto)
- salary

---

### 185. Department Top Three Salaries (Hard)
**Objetivo:** Para cada departamento, retorne os funcionários com os **3 maiores salários distintos**.
- Se houver empate, podem aparecer mais de 3 pessoas (ex.: dois funcionários com o 3º maior salário).

---

### (Extra) 196. Delete Duplicate Emails (Easy)
**Tabela:** `person`
**Objetivo:** “Deletar” duplicados mantendo apenas o menor `id` por email.
- Se seu ambiente não deixa deletar, escreva uma query que retorne apenas os registros “mantidos”.

---

## Desafio bônus (bem real de trabalho)
### A) Ticket médio por cliente + classificação
**Objetivo:** Para cada cliente com pedidos, calcule:
- total_amount (soma do amount)
- orders_count
- avg_ticket (total_amount / orders_count)
E crie uma coluna `bucket`:
- 'High' se avg_ticket >= 300
- 'Mid' se entre 150 e 299.99
- 'Low' se < 150

### B) Clientes com pedidos repetidos no mesmo dia e valor
**Objetivo:** Encontre clientes que fizeram **mais de 1 pedido** no mesmo `orderDate` com o mesmo `amount`.