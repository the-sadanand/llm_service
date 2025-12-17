import threading
from transformers import pipeline

_model = None
_model_lock = threading.Lock()
_inference_lock = threading.Lock()


def get_model():
    """
    Lazy-load the model once per container.
    """
    global _model
    with _model_lock:
        if _model is None:
            _model = pipeline(
                "text-generation",
                model="distilgpt2"
            )
    return _model


def get_inference_lock():
    """
    Global lock to serialize inference.
    """
    return _inference_lock
