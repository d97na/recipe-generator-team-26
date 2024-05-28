from typing import Literal

from pydantic import BaseModel, Field


class InputModel(BaseModel):
    include: str = Field(
        default='tomato, cheese, pepper',
    )
    exclude: str = Field(
        default='onion',
    )
    time: Literal[
        '10 mins',
        '15 mins',
        '20 mins',
        '30 mins',
    ] = Field(
        default='10 mins',
    )
    taste: Literal[
        'salty',
        'sweet',
        'sour',
        'spicy',
    ] = Field(
        default='salty',
    )

    llm_type: Literal['chatgpt'] = Field(
        alias='Large Language Model Type',
        description='사용할 LLM 종류',
        default='chatgpt',
    )


class OutputModel(BaseModel):
    output: str = Field(
        description='Recipe',
    )