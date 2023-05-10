# main.py
import uvicorn
import asyncio
from app import app
from run_loop import run_loop

config = uvicorn.Config(
    "app:app",
    port=8000,
    log_level="info",
    access_log=True,
    use_colors=True,
    reload=True,
)
server = uvicorn.Server(config)

async def main() -> None:
    await asyncio.gather(server.serve(), run_loop(), return_exceptions=True)

if __name__ == "__main__":
    asyncio.run(main())
