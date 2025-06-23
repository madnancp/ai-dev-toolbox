from typing import Any
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer


class VectorStore:

    def __init__(
        self,
        store_path: str = "./chroma_db",
        collection_name: str = "vector_store",
    ) -> None:
        self.id = "000"
        self.client = PersistentClient(path=store_path)

        self.embedder = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2",
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name,
        )

    def create(self, sentence: str) -> tuple[bool, str]:
        try:
            new_id = self._generate_id()
            new_embeddings = self._embedd(sentence=sentence)
            self.collection.add(
                ids=[new_id], documents=[sentence], embeddings=new_embeddings
            )
            return True, "ok"
        except Exception as e:
            return False, str(e)

    def update(self, id: str, new_sentence: str) -> tuple[bool, str]:
        if id not in self.fetch_all.get("ids"):
            return False, "id not found!"
        try:
            new_embdd = self._embedd(sentence=new_sentence)
            self.collection.update(
                ids=[id], embeddings=new_embdd, documents=[new_sentence]
            )
            return True, "Ok!"
        except Exception as e:
            return False, str(e)

    def delete(self, id: int) -> tuple[bool, str]:
        if id not in self.fetch_all.get("ids"):
            return False, "id not found!"

        try:
            self.collection.delete(ids=[id])
            return True, "Ok!"
        except Exception as e:
            return False, str(e)

    def search(self, sentence: str) -> Any:
        embeddings = self._embedd(sentence=sentence)
        result = self.collection.query(query_embeddings=embeddings, n_results=2)
        return result

    def _embedd(self, sentence: str) -> list:
        return self.embedder.encode(sentence).tolist()

    def _generate_id(self) -> str:
        """generate ids, 000-999"""

        val = int(self._current_id)
        if 9 <= val <= 98:
            new_id = "0" + str(val + 1)
            self.id = new_id
            return self.id

        elif 99 <= val <= 999:
            new_id = str(val + 1)
            self.id = new_id
            return self.id

        elif val < 9:
            new_id = "00" + str(val + 1)
            self.id = new_id
            return self.id

        else:
            return "NAN"

    @property
    def _current_id(self) -> str:
        result = self.collection.get()
        return result.get("ids")[-1]

    @property
    def fetch_all(self) -> Any:
        return self.collection.get()
