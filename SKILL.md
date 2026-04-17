---
name: legal-document-explainer
description: Analisa documentos jurídicos (contratos, ToS, aluguel, privacidade), resume em linguagem simples, destaca cláusulas abusivas (red flags), atribui um placar de risco e sugere perguntas críticas. Use sempre que o usuário fornecer um documento legal ou pedir para "explicar um contrato" ou "ver se este termo de serviço é seguro".
---

# Legal Document Explainer

Este skill transforma documentos jurídicos complexos em relatórios compreensíveis e acionáveis, focando na proteção do consumidor e na transparência.

## Quando usar
- O usuário envia um PDF, DOCX ou texto de um contrato, termos de serviço ou política de privacidade.
- O usuário pergunta sobre "armadilhas" em um documento.
- O usuário quer saber se deve assinar algo.

## Fluxo de Trabalho

1. **Extração de Texto**: 
   - Se o arquivo for PDF ou DOCX, use o script `scripts/analyze_document.py <caminho_do_arquivo>` para extrair o conteúdo.
   - Se for texto puro ou Markdown, leia diretamente.

2. **Análise de Cláusulas (Red Flags)**:
   - Consulte `references/red_flags.md` para identificar padrões de risco.
   - Procure especificamente por:
     - Arbitragem forçada.
     - Renovação automática.
     - Coleta e venda de dados.
     - Taxas de cancelamento abusivas.
     - Direito unilateral de alteração dos termos.
   - Use `references/glossary.md` para traduzir termos técnicos para o usuário.

3. **Cálculo do Placar de Risco (Risk Score)**:
   - **Baixo (Low)**: Documento transparente, fácil cancelamento, sem cláusulas de arbitragem agressivas.
   - **Médio (Medium)**: Cláusulas de arbitragem padrão ou compartilhamento de dados com parceiros.
   - **Alto (High)**: Renovação automática sem aviso, taxas de cancelamento ocultas, indenização ampla ou perda total de direitos de privacidade.

4. **Geração do Relatório**:
   - Use o template em `assets/report_template.md` como base.
   - O relatório deve ser visualmente atraente e fácil de ler.

## Formato de Resposta Exemplo

### ⚖️ Relatório de Análise: Termos de Serviço da "Empresa X"

#### 📋 Resumo Executivo
Este documento é um termo de serviço padrão para plataformas de streaming. No geral, é aceitável, mas contém cláusulas de renovação automática que exigem atenção.

#### ✅ Destaques Positivos
- Linguagem relativamente clara.
- Opção de cancelamento direto pelo painel do usuário.

#### 🚩 Cláusulas Problemáticas (Red Flags)
- **Cláusula:** Renovação Automática (Seção 4.2)
- **Risco:** 🔴 Alto
- **Contexto:** "A assinatura será renovada automaticamente por períodos iguais, a menos que seja cancelada com 30 dias de antecedência."
- **Por que importa:** Se você esquecer a data, será cobrado por mais um ano inteiro sem aviso prévio.

- **Cláusula:** Resolução de Disputas (Seção 12)
- **Risco:** 🟡 Médio
- **Contexto:** "Todas as disputas devem ser resolvidas via arbitragem em Delaware."
- **Por que importa:** Você desiste de ir a um tribunal comum no seu estado.

#### 📊 Placar de Risco
**Score:** 🟡 **Médio**
**Análise:** O principal risco é a renovação automática "zumbi" e a jurisdição distante para disputas legais.

#### ❓ 3 Perguntas para Fazer
1. Posso desativar a renovação automática imediatamente após a assinatura?
2. Existe algum reembolso proporcional se eu cancelar no meio do período?
3. Como posso solicitar a exclusão total dos meus dados após o término do contrato?

---
*Aviso: Esta análise não substitui o conselho de um advogado qualificado.*
