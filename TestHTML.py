from fastapi import FastAPI
from fastapi.responses import HTMLResponse



app = FastAPI()


@app.get('/', response_class=HTMLResponse)
async def read_items():
    return  """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Test<h1>
        </body>
    </html>
    """