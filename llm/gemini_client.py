# llm/gemini_client.py
import os
import time

API_KEY = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
USE_REAL = bool(API_KEY)

# Simple deterministic mock for local testing / demo mode
def _mock_generate(prompt, max_tokens=256):
    # Keep mock deterministic and short so outputs are predictable
    p = prompt.lower()
    if "root cause" in p or "why" in p or "identify" in p:
        return "Database connection pool exhausted (mock)"
    if "fix" in p or "recommend" in p or "remediate" in p:
        return "Increase DB pool size, add connection retry logic, and monitor connections (mock)"
    # fallback short reply
    return "Mock response: couldn't call Gemini API."

if USE_REAL:
    try:
        import google.generativeai as genai  # package name may vary; check your installed package
        MODEL_NAME = os.environ.get("GEMINI_MODEL", "gemini-1.5")  # replace if needed
        genai.configure(api_key=API_KEY)
    except Exception as e:
        # If the real client import fails, fall back to mock but warn
        print("[GeminiClient] WARNING: could not import google.generativeai client, falling back to mock.", e)
        USE_REAL = False

def generate(prompt: str, max_tokens: int = 256, temperature: float = 0.0) -> str:
    """
    Single-call helper: returns text result from Gemini (if available) or a deterministic mock.
    - Set environment variable GEMINI_API_KEY or GOOGLE_API_KEY to enable real calls.
    - Optionally set GEMINI_MODEL to the model name you want (e.g., "gemini-1.5" or "gemini-pro").
    """
    if not USE_REAL:
        return _mock_generate(prompt, max_tokens)

    # Real call (best-effort shape — check Google docs for up-to-date usage)
    try:
        # Example chat-style call — adapt keys to the client version you installed.
        response = genai.chat.create(
            model=MODEL_NAME,
            messages=[{"role":"system","content":"You are an assistant that helps analyze incidents."},
                      {"role":"user","content": prompt}],
            temperature=temperature,
            max_output_tokens=max_tokens
        )
        # response structure may vary by client version; try common fields:
        if hasattr(response, "candidates") and response.candidates:
            return response.candidates[0].content
        if isinstance(response, dict):
            # navigate a common REST-like shape
            # This is defensive — update if your installed client returns a different shape
            if "candidates" in response and len(response["candidates"])>0:
                return response["candidates"][0].get("content","")
            if "output" in response:
                return response["output"]
        # Fallback: stringify
        return str(response)
    except Exception as e:
        # Never crash — fallback to mock if real call fails
        print("[GeminiClient] ERROR during real call, falling back to mock. Error:", e)
        return _mock_generate(prompt, max_tokens)
