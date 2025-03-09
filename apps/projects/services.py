from sentence_transformers import SentenceTransformer
import numpy as np
from scipy.spatial.distance import cosine
from .models import Project

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text):
    # Convertir el texto a un vector numerico
    return model.encode(text).astype(np.float32).tobytes()

def find_similar_projects(title, description, threshold=0.7):
    # Busca proyectos similares en la BD usando similitud coseno
    new_text = f"{title} {description}"
    new_vector = np.frombuffer(get_embedding(new_text), dtype=np.float32)

    projects = Project.objects.exclude(embedding=None).values("id", "title", "description", "embedding")
    similarities = []

    for project in projects:
        stored_vector = np.frombuffer(project["embedding"], dtype=np.float32)
        similarity = 1 - cosine(new_vector, stored_vector)

        if similarity >= threshold:
            similarities.append({
                "id": project["id"],
                "title": project["title"],
                "description": project["description"],
                "similarity": round(similarity * 100, 2)
            })

    return sorted(similarities, key=lambda x: x["similarity"], reverse=True)