from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.llm import LLMGenerator
from app.sd_pipeline import StableDiffusionPipeline

app = FastAPI()

class ImageEditRequest(BaseModel):
    user_prompt: str
    mask_description: Optional[str] = None

class ImageEditResponse(BaseModel):
    generated_image_path: str

llm_generator = LLMGenerator()
sd_pipeline = StableDiffusionPipeline()

@app.post("/edit_image", response_model=ImageEditResponse)
def edit_image(request: ImageEditRequest):
    try:
        detailed_prompt = llm_generator.generate_prompt(request.user_prompt)
        image_path = sd_pipeline.generate_and_edit(detailed_prompt, request.mask_description)
        return ImageEditResponse(generated_image_path=image_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))