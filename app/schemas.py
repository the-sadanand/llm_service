from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    prompt: str = Field(..., example="Explain AI in simple terms")
    max_tokens: int = Field(50, ge=10, le=200)


class GenerateResponse(BaseModel):
    generated_text: str
