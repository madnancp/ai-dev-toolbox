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

        self.embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

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

    def update(self) -> bool:
        pass

    def delete(self) -> bool:
        pass

    def search(self) -> bool:
        pass

    def _embedd(self, sentence: str) -> list:
        return self.embedder.encode(sentence).tolist()

    def _generate_id(self) -> str:
        """generate ids, 000-999"""

        val = int(self.id)
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
