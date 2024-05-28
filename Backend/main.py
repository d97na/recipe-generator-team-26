import os
import dotenv
from fastapi import FastAPI

import routers

# Load environment variables from dotenv file
dotenv.load_dotenv()

app = FastAPI(
    root_path=os.environ.get('BASE_URL', ''),
)

app.include_router(routers.functions.recipe_generator.router)
app.include_router(routers.health.router)
app.include_router(routers.home.router)
