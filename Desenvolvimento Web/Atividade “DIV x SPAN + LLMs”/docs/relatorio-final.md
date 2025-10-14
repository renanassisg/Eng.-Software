# Relatório Final - Experimentos com Block e Inline ALUNO: RENAN DE ASSIS GOMES

## 1. Diferenças entre elementos block-level e inline-level

- **DIV (block-level)**  
  - Empilha verticalmente, ocupando toda a largura disponível.  
  - Permite ajustar largura, altura, margens e padding sem restrições.  
  - Ideal para estruturar seções, cartões ou qualquer bloco de conteúdo.

- **SPAN (inline-level)**  
  - Flui junto ao texto, mantendo elementos lado a lado.  
  - Largura e altura não são respeitadas diretamente; margin e padding vertical têm efeito limitado.  
  - Mais indicado para estilizar trechos de texto ou ícones dentro de blocos.

> **Observação prática:** Transformar um `<span>` em `display:block` permite controlar tamanho, enquanto `inline-block` mantém os elementos na mesma linha e ainda aceita largura e altura.

---

## 2. Comparação entre os LLMs utilizados

Durante o trabalho, usamos **ChatGPT** e **Perplexity** como parceiros de programação. Observações importantes:

- **ChatGPT**  
  - Produziu códigos claros, completos e com comentários explicativos.  
  - Ofereceu sugestões consistentes de melhoria e identificação precisa de problemas.  
  - Foi mais didático, facilitando o aprendizado.

- **Perplexity**  
  - Entregou soluções diretas, funcionando, mas com explicações menos detalhadas.  
  - Em alguns casos, exigiu ajustes manuais para clareza ou correção de pequenos erros.  
  - Útil para testes rápidos ou protótipos simples.

> **Conclusão parcial:** ChatGPT se mostrou mais robusto e confiável para estudo e revisão, enquanto Perplexity foi eficiente para geração rápida de código.

---

## 3. Experimentos com display, block e inline-block

- Aplicar `width` ou `height` diretamente em elementos inline sem mudar o display **não funciona**.  
- `display:inline-block` permite manter elementos lado a lado **e** controlar dimensões.  
- Visualizar o *box model* (content, padding, border, margin) ajudou a perceber como cada camada impacta o layout.

> A experiência prática confirmou que escolher o tipo correto de display evita erros de layout comuns e garante maior previsibilidade no design.

---

## 4. Depuração guiada

- Criar e corrigir bugs foi essencial para entender problemas típicos de inline vs block.  
- LLMs aceleraram a identificação de falhas e sugeriram soluções, mas a validação no navegador foi indispensável.  
- Esse processo reforçou a importância de ler e interpretar o código, não apenas confiar nas sugestões automáticas.

---

## 5. Trabalho assíncrono e documentação

- A divisão de papéis (gerador, revisor e comparador) funcionou bem mesmo com horários diferentes.  
- Registrar prompts, respostas e decisões permitiu acompanhar as diferenças entre LLMs de forma objetiva e organizada.  
- A documentação consolidou aprendizados e forneceu material para consultas futuras.

---

## 6. Observações finais

- Escolher o display correto é fundamental para construir layouts previsíveis e responsivos.  
- LLMs são aliados poderosos no aprendizado e na revisão de código, mas devem ser usados com pensamento crítico.  
- O trabalho mostrou claramente como dois modelos diferentes podem gerar abordagens distintas, ressaltando a importância da análise humana nas decisões de design.
