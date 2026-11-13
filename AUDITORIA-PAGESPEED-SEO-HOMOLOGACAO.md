# AS Beauty Center — Auditoria PageSpeed, SEO, acessibilidade e boas práticas
**Data:** 13/11/2026 · **Ambiente:** Vercel Preview (branch `as-beauty-redesign-etapa-01-paleta-hero`)

> **Escopo:** página inicial + seis páginas de tratamentos. Auditoria de código seguindo o roteiro público da skill `pagespeed-seo-optimizer`, de Anny Gabrielly: https://github.com/annygabb/pagespeed-seo-optimizer. A skill não estava instalada no catálogo do ambiente; o `SKILL.md` e seu checklist público foram consultados e usados como metodologia. As verificações de métricas do navegador (PageSpeed Insights e Lighthouse) **não foram executadas** porque a prévia tem Vercel Authentication/SSO e não houve ambiente compatível para medição autenticada. **Não há notas oficiais PSI/Lighthouse neste relatório.**

## Situação do deploy

- Projeto Vercel: `as-beauty`; origem GitHub: `victorpamplona/as-beauty`.
- Branch de revisão separada da `main`; somente homologação, **não é publicação oficial**.
- Sete páginas com `<html lang="pt-BR">`, um único H1 por página, FAQ específica por tratamento e CTA de consulta.
- Vercel: deploy da branch identificado como `READY` antes deste relatório; estado posterior deve ser consultado após o commit.
- Marcação `<meta name="robots" content="noindex, nofollow">` inserida em todas as sete páginas **somente para homologação**. Não fazer merge na `main` antes de remover esta regra.

## Comparativo verificável (análise estática do código)

| Item | Antes | Depois |
| --- | --- | --- |
| Título da página inicial | 79 caracteres | 53 caracteres |
| Descrição da página inicial | 162 caracteres | 137 caracteres |
| Títulos das seis páginas | 71, 51, 60, 77, 52, 52 caracteres | 47, 47, 45, 47, 48, 48 caracteres |
| Descrições das seis páginas | 169, 156, 157, 204, 170, 179 caracteres | 141, 150, 138, 146, 140, 137 caracteres |
| Links externos da página inicial com `target="_blank"` sem `rel="noopener"` | 9 | 0 |
| Elementos de imagem da página inicial com dimensões incompatíveis com os WebP originais | 10 | 0 |
| Preload prioritário da foto principal na página inicial | Ausente | Presente, somente foto do hero |
| `title` descritivo no iframe do mapa | Ausente | Presente |
| Metadados Twitter Card | Ausentes | Presente nas 7 páginas |
| Noindex da prévia | Ausente | Presente nas 7 páginas |

**Tamanho dos recursos visuais medido do pacote de fotos original:** 11 arquivos WebP, 799.874 bytes (aproximadamente 781 KiB) no total. A otimização desta rodada **não alterou os bytes** dessas imagens; atualizou apenas declarações de dimensões, prioridade e metadados.

## Verificações estáticas concluídas

- [x] Títulos exclusivos e meta descriptions específicas nas 7 páginas.
- [x] Todas as páginas declaram idioma português do Brasil.
- [x] H1 única em cada página; 6 páginas com 6 perguntas frequentes cada.
- [x] As fotografias de cada página de tratamento apontam para `/assets/` e mantêm dimensões declaradas.
- [x] Foto do hero da página principal com `fetchpriority="high"` e preload.
- [x] Elementos de imagem abaixo da dobra com lazy loading onde já previsto.
- [x] Links externos com nova aba seguros, na página inicial.
- [x] Iframe do Google Maps com título descritivo e lazy loading.
- [x] Navegação para as 6 páginas a partir dos cards da página principal.
- [x] Botões de WhatsApp contextualizados para a consulta.
- [x] Staging protegido contra indexação por metatags e controle de acesso do provedor.

## Pendências de performance e verificação real

1. **Alta:** o arquivo `index.html` ainda usa `https://cdn.tailwindcss.com` (compilação de Tailwind no navegador). A substituição por CSS estático deve ocorrer em uma etapa própria, com teste visual comparativo antes/depois; não foi removido para evitar regressão.
2. **Alta:** rodar Lighthouse 13+/PageSpeed Insights em mobile e desktop no endereço acessível e documentar Performance, Acessibilidade, Best Practices, SEO, LCP, CLS e TBT/INP quando disponíveis. **Sem dados reais não declarar nota ou ganho de velocidade**.
3. **Alta:** testar 7 rotas em navegador externo autenticado, console JavaScript, navegação mobile, CTAs e acessibilidade de teclado. Deploy READY não comprova experiência visual.
4. **Média:** revisar o carregamento das fontes e dos ícones de terceiros com medição real.
5. **Média:** considerar políticas de cabeçalhos de segurança (ex.: CSP) sem bloquear scripts e integrações legítimos; requer teste de hospedagem.
6. **Média:** preparar Open Graph/Twitter com imagem social absoluta e URL canônica somente após aprovação do domínio final.
7. **Média:** definir `robots.txt` e `sitemap.xml` para ambiente de produção **após** retirar noindex, validar conteúdo clínico e definir domínio definitivo.

## Conteúdo e aprovação profissional pendentes

- Nome/qualificações/registros profissionais; procedimentos efetivamente oferecidos, indicações, limitações e contraindicações.
- Verificar dados de prova social exibidos no site, incluindo **+2.000 alunos**, **5,0 no Google** e **137 avaliações**.
- Confirmar endereço, WhatsApp, horários, preço da consulta e permissões de uso das imagens reais de atendimentos/depoimentos.
- Conferir a linguagem e as regras de publicidade profissional aplicáveis.
- Não tratar as páginas de saúde como aconselhamento clínico individual.

## Antes do merge para produção

1. Receber aprovação clínica, jurídica e comercial do conteúdo.
2. Confirmar domínio final; configurar canonical, OG/Twitter image, favicon, sitemap e `robots.txt`.
3. **Remover `noindex, nofollow` de todas as sete páginas.**
4. Executar auditorias Lighthouse mobile e desktop e testes completos de URLs; registrar resultados.
5. Promover a branch somente após revisão; o deploy de homologação é separado do site oficial.
