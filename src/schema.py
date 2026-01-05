from pydantic import BaseModel, Field

class CropInput(BaseModel):
    # This prevents users from sending negative values or impossible numbers
    N: float = Field(..., ge=0, le=200, description="Nitrogen content")
    P: float = Field(..., ge=0, le=200, description="Phosphorous content")
    K: float = Field(..., ge=0, le=250, description="Potassium content")
    temperature: float = Field(..., ge=0, le=60, description="Temperature (C)")
    humidity: float = Field(..., ge=0, le=100, description="Humidity (%)")
    ph: float = Field(..., ge=0, le=14, description="Ph Level")
    rainfall: float = Field(..., ge=0, le=400, description="Rainfall (mm)")