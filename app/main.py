import asyncio
from fastapi import FastAPI, Depends, HTTPException
from app.schemas import GenerateRequest, GenerateResponse
from app.auth import verify_api_key
from app.model import get_model, get_inference_lock

app = FastAPI(
    title="LLM Serving API",
    description="Thread-safe LLM inference service",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


def run_inference(model, lock, request: GenerateRequest):
    """
    Runs LLM inference safely using a global lock.
    Prevents tokenizer/model corruption under concurrency.
    """
    with lock:
        output = model(
            request.prompt,
            max_length=request.max_tokens,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.2,
            eos_token_id=model.tokenizer.eos_token_id,
        )
    return output


@app.post(
    "/generate",
    response_model=GenerateResponse,
    dependencies=[Depends(verify_api_key)],
)
async def generate_text(request: GenerateRequest):
    model = get_model()
    inference_lock = get_inference_lock()
    loop = asyncio.get_event_loop()

    try:
        result = await loop.run_in_executor(
            None,
            run_inference,
            model,
            inference_lock,
            request,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    generated_text = result[0]["generated_text"]
    generated_text = generated_text.replace("\n", " ").strip()

    return GenerateResponse(generated_text=generated_text)
