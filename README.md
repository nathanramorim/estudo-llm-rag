# estudo-llm-rag

Repositório de estudos para construir, módulo a módulo, um sistema RAG (Retrieval-Augmented Generation) do zero — da geração de embeddings até avaliação de qualidade. Cada pasta representa um módulo prático do roadmap abaixo.

## Estrutura do repositório

- `embeddings-lab/` — Módulo 1: embeddings e busca semântica

Novos módulos serão adicionados como novas pastas conforme o roadmap avança.

---

# Roadmap de estudo — engenharia de IA (foco em LLMs & RAG)

**Perfil de partida:** base em Python e APIs, boa intuição de conceitos, gaps em fundamentos técnicos de RAG (embeddings, vector DBs, avaliação).
**Objetivo:** conseguir uma vaga na área.
**Duração estimada:** 12 semanas (ajuste o ritmo à sua rotina — o importante é praticar toda semana, não só ler).

## Como usar este roadmap

Cada módulo tem: **o que aprender**, **por que isso importa pra vaga**, **prática obrigatória** (sem prática, o conhecimento não gruda) e **recursos**. Não pule a prática — quem contrata quer ver projeto rodando, não teoria decorada.

---

## Módulo 1 — Embeddings e busca semântica (semanas 1–2)

**O que aprender:**
- O que é um embedding e como um texto vira vetor
- Similaridade de cosseno e distância euclidiana
- Diferença entre embeddings de palavra (word2vec) e embeddings de frase/documento (modelos modernos)
- Modelos de embedding populares: `text-embedding-3` (OpenAI), modelos open-source do Hugging Face (`sentence-transformers`)

**Por que importa:** é a base técnica de todo RAG. Sem entender isso, você não consegue debugar por que uma busca trouxe resultado errado.

**Prática obrigatória:**
1. Gerar embeddings de 10 frases diferentes via API (OpenAI ou Hugging Face) e calcular similaridade entre elas em Python
2. Visualizar embeddings em 2D usando redução de dimensionalidade (t-SNE ou PCA) — ver visualmente o agrupamento por assunto

**Recursos:**
- OpenAI Cookbook — seção de embeddings
- Curso curto "Understanding embeddings" (DeepLearning.AI, gratuito)
- Biblioteca `sentence-transformers` (documentação oficial)

---

## Módulo 2 — Chunking e ingestão de dados (semana 3)

**O que aprender:**
- Estratégias de chunking: fixo, por sentença, por parágrafo, recursivo
- Overlap entre chunks e por que ele existe
- Como lidar com PDFs, tabelas e documentos estruturados na hora de dividir

**Prática obrigatória:**
1. Pegar um PDF real (manual, artigo) e implementar 2 estratégias de chunking diferentes em Python
2. Comparar os resultados: qual estratégia manteve mais contexto?

**Recursos:**
- Documentação do `RecursiveCharacterTextSplitter` (LangChain) — mesmo sem usar o framework, a doc explica bem as estratégias
- Artigo "Chunking strategies for RAG" (Pinecone Learning Center)

---

## Módulo 3 — Vector databases (semanas 4–5)

**O que aprender:**
- Diferença entre banco vetorial e banco relacional
- Como funciona indexação vetorial (HNSW, IVF — visão geral, não precisa aprofundar matemática)
- Comparar pelo menos 2 opções: uma gerenciada (Pinecone) e uma open-source (Chroma ou Qdrant)
- `pgvector` — extensão vetorial pro Postgres (muito pedido em vaga que já usa Postgres)

**Prática obrigatória:**
1. Subir um banco vetorial local (Chroma é o mais simples pra começar)
2. Inserir os chunks do módulo 2 com seus embeddings
3. Fazer uma busca por similaridade e conferir se o resultado faz sentido

**Recursos:**
- Documentação oficial do Chroma (quickstart)
- Pinecone Learning Center (conceitos de indexação vetorial)

---

## Módulo 4 — Construindo um RAG do zero, sem framework (semanas 6–7)

**O que aprender:**
- Juntar tudo: documento → chunk → embedding → vector DB → busca → prompt → resposta
- Prompt engineering para "grounding" (forçar o modelo a responder só com base no contexto)
- Como montar o prompt final concatenando os chunks recuperados

**Prática obrigatória (projeto principal do roadmap):**
1. Construir um chatbot de RAG completo, do zero, sem LangChain — só Python puro + API de LLM + Chroma
2. Usar seus próprios documentos (PDFs de estudo, por exemplo) como base de conhecimento
3. Subir esse projeto no GitHub com README explicando a arquitetura — **esse é o primeiro item forte do seu portfólio**

**Recursos:**
- OpenAI Cookbook — exemplo de RAG do zero
- Vídeo/tutorial "Build RAG from scratch" (procurar no YouTube, tem vários bons e gratuitos)

---

## Módulo 5 — Frameworks: LangChain e LlamaIndex (semanas 8–9)

**O que aprender:**
- Os mesmos conceitos do módulo 4, mas usando as abstrações prontas dos frameworks
- Quando vale a pena usar framework vs fazer na mão
- Conceito de "chains" e "agents" no LangChain (visão inicial, aprofunda depois se for pra área de agentes)

**Prática obrigatória:**
1. Refazer o projeto do módulo 4 usando LangChain **ou** LlamaIndex
2. Comparar: o que ficou mais simples? O que ficou "mágico demais" (difícil de debugar)?

**Recursos:**
- Documentação oficial LangChain (seção RAG)
- Documentação oficial LlamaIndex (seção "Building a RAG pipeline")

---

## Módulo 6 — Fine-tuning: quando e como (semana 10)

**O que aprender:**
- Recapitular a regra de ouro: prompt → RAG → fine-tuning
- Fine-tuning via API gerenciada (OpenAI, por exemplo) — o caminho mais acessível
- Visão geral de LoRA/PEFT (não precisa dominar, só entender que existe pra treinar modelos open-source mais barato)

**Prática obrigatória:**
1. Fazer um fine-tuning pequeno via API (dataset de 50-100 exemplos) em algum caso simples (ex: sempre responder num formato específico)
2. Comparar a resposta do modelo fine-tuned vs o mesmo prompt no modelo base

**Recursos:**
- Documentação oficial de fine-tuning do provedor que você escolher (OpenAI, Google, etc.)

---

## Módulo 7 — Avaliação e debugging de sistemas RAG (semanas 11–12)

**O que aprender:**
- Métricas: retrieval accuracy, faithfulness, relevance
- Framework RAGAS pra automatizar avaliação
- Processo de debugging: quando um RAG erra, onde investigar primeiro (retrieval? chunking? prompt?)

**Prática obrigatória:**
1. Montar um conjunto de 15-20 perguntas de teste com resposta esperada, baseado no projeto do módulo 4
2. Rodar RAGAS (ou métricas manuais) nesse conjunto e identificar onde o sistema falha
3. Ajustar chunking ou prompt com base no resultado, e medir de novo

**Recursos:**
- Documentação oficial do RAGAS
- Artigo "Evaluating RAG pipelines" (Pinecone ou Weaviate blog, ambos têm conteúdo bom e gratuito)

---

## Preparação para vaga (paralelo, a partir da semana 8)

- Deixar o projeto do módulo 4 e 5 público no GitHub, com README bem escrito (arquitetura, decisões técnicas, resultados)
- Praticar explicar verbalmente: "como você resolveria alucinação num RAG?", "quando você usaria fine-tuning?" — são perguntas comuns de entrevista
- Seguir vagas reais de "AI Engineer" / "LLM Engineer" e ver quais stacks pedem mais (isso vai te dizer se vale focar mais em LangChain, em algum vector DB específico, etc.)

---

## Resumo visual da ordem de prioridade

1. Embeddings (fundamento)
2. Chunking (fundamento)
3. Vector DB (fundamento)
4. RAG do zero (projeto de portfólio)
5. Frameworks (produtividade)
6. Fine-tuning (caso de uso específico)
7. Avaliação (o que separa amador de profissional)
