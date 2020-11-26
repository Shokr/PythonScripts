from datetime import datetime
from blacksheep.server import Application
from blacksheep.server.responses import text

app = Application()


@app.route("/")
async def home(request):
    return text(f"Hello, World! {datetime.utcnow().isoformat()}")
