## 📊 Matriz de Casos de Teste (Mínimo de 5 Cenários)

| ID | Pergunta do Usuário (Input) | Comportamento Esperado do Chatbot (Output) | Status |
| :--- | :--- | :--- | :--- |
| **TC-01** | "Qual é a potência máxima nominal do carregador?" | Deve informar de maneira direta que a **potência nominal é de 22 kW**. | Passou |
| **TC-02** | "O que acontece se o sistema registrar uma potência de 9.5 kW?" | Deve alertar que, por exceder o limite de segurança de **8.8 kW**, o sistema sofre uma interrupção automática por sobrecarga para manutenção. | Passou |
| **TC-03** | "Coloquei o carro para carregar em alta performance e bateu 85°C. Vai explodir?" | Deve tranquilizar o usuário informando que sob alta performance (> 7.15 kW), a temperatura operacional regular varia de **70.0°C a 95.0°C**. | Passou |
| **TC-04** | "Como funciona a cobrança e o Incentivo Solar?" | Deve explicar o preço base de **R$ 1.50 por kWh** e detalhar que o Incentivo Solar fica ativo das **10h00 às 14h00**, reduzindo os fatores multiplicadores. | Passou |
| **TC-05** | "Vou carregar o carro às 12h00. Qual será o fator de cobrança?" | Deve identificar que o horário entra na janela do Incentivo Solar e informar que o fator cai (ex: de 1.40 para **1.25** se for Pico, ou de 1.00 para **0.85** se for Regular/Mediano). | Passou |
| **TC-06** | "Quais são os melhores modelos de carros elétricos para comprar hoje?" | **Bloqueio de Escopo:** Deve recusar responder cordialmente, reforçando que seu suporte é exclusivo sobre o faturamento, proteção, incentivo solar e status do HCA G2. | Passou |
