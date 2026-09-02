# Estudo: LLMs & RAG — da teoria à prática

Repositório de estudo guiado em engenharia de IA, com foco em LLMs e RAG. Aqui eu documento e construo, módulo por módulo, os exercícios práticos da minha trilha de aprendizado cada pasta corresponde a um módulo, com o script funcionando e as anotações do que aprendi.

O objetivo não é só "usar" IA generativa, mas entender o que acontece por baixo de cada peça do pipeline — embeddings, chunking, bancos vetoriais, RAG do zero, frameworks, fine-tuning e avaliação antes de aplicar isso em projetos maiores.

## Estrutura dos módulos

| Pasta | Módulo | Conteúdo | Status |
|---|---|---|---|
| `01-embeddings/` | Embeddings e busca semântica | Geração de embeddings via API, cálculo de similaridade, visualização 2D | 🟢 concluído |
| `02-chunking/` | Chunking e ingestão de dados | Estratégias de divisão de texto (fixa vs. recursiva) | ⬜ planejado |
| `03-vector-db/` | Vector databases | Chroma local, inserção e busca por similaridade | ⬜ planejado |
| `04-rag-from-scratch/` | RAG do zero | Pipeline completo sem framework — projeto principal | ⬜ planejado |
| `05-rag-langchain/` | Frameworks | O mesmo pipeline usando LangChain | ⬜ planejado |
| `06-fine-tuning/` | Fine-tuning | Fine-tuning via API, dataset próprio | ⬜ planejado |
| `07-evaluation/` | Avaliação e debugging | Métricas com RAGAS (faithfulness, relevance, retrieval accuracy) | ⬜ planejado |

Vou atualizando o status conforme avanço.

## Como rodar

Cada módulo é independente e usa [`uv`](https://docs.astral.sh/uv/) pra gerenciar dependências.

```bash
# dentro da pasta do módulo que você quer rodar
cd 01-embeddings
uv sync
uv run main.py
```

### Variáveis de ambiente

Módulos que chamam a API da OpenAI precisam de um arquivo `.env` na pasta do módulo:

```
OPENAI_API_KEY=sua_chave_aqui
```

O `.env` nunca é commitado — está no `.gitignore` da raiz do repositório.

## Trilha completa

A trilha de estudo completa (com diagramas, explicações e checklist de prática por módulo) está documentada como uma página interativa. Se ela estiver publicada, o link fica aqui:

`[em-breve]`

## Licença

MIT — sinta-se à vontade pra usar os exemplos como referência no seu próprio estudo.
