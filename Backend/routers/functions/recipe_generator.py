import os

from fastapi import APIRouter

from llm.chat import build
from llm.store import LLMStore
from models.recipe_generator import InputModel, OutputModel

# Configure API router
router = APIRouter(
    tags=['functions'],
)

# Configure metadata
NAME = os.path.basename(__file__)[:-3]

# Configure resources
store = LLMStore()

###############################################
#                   Actions                   #
###############################################


@router.post(f'/func/{NAME}')
async def call_recipe_generator(model: InputModel) -> OutputModel:
    # Create a LLM chain
    chain = build(
        name=NAME,
        llm=store.get(model.llm_type),
    )

    return OutputModel(
        output=chain.invoke({
            'input_context': f'''
                # About Company
                * Included ingredients: {model.include}
                * Excluded ingredients: {model.exclude}
                * Preparation time: {model.time}
                * Taste preferences: {model.taste}
            ''',
        }),
    )
