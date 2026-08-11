from pydantic import BaseModel

class Document(BaseModel):
    document_id: str
    original_filename: str
    stored_filename: str
    