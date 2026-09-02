# 1. Carrega a chave da API guardada no .env
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

client = OpenAI()

# 2. As frases de teste — 3 grupos de assunto diferentes
frases = [
    "O cachorro correu no parque",
    "Meu gato dorme o dia todo",
    "Levei o cão pro veterinário",
    "O carro quebrou na estrada",
    "Fui de ônibus pro trabalho",
    "A moto ficou sem gasolina",
    "A receita de bolo levou farinha",
    "Temperei a carne com alho",
    "O forno esquentou rápido demais",
]

# 3. Manda as frases pra API e recebe os embeddings de volta
response = client.embeddings.create(
    input=frases,
    model="text-embedding-3-small"
)
vetores = [item.embedding for item in response.data]

print(f"Cada frase virou um vetor de {len(vetores[0])} números")

# 4. Calcula o quão parecida cada frase é das outras
matriz = cosine_similarity(np.array(vetores))
print("\nMatriz de similaridade:")
print(np.round(matriz, 2))

# 5. Achata os vetores pra 2D só pra dar pra desenhar no gráfico
coords = PCA(n_components=2).fit_transform(np.array(vetores))

plt.figure(figsize=(8, 6))
plt.scatter(coords[:, 0], coords[:, 1])
for i, frase in enumerate(frases):
    plt.annotate(frase[:20], (coords[i, 0], coords[i, 1]), fontsize=8)
plt.title("Frases no espaço de embeddings")
plt.show()