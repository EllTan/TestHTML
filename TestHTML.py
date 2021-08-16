from fastapi import FastAPI
from fastapi.responses import HTMLResponse



app = FastAPI()


@app.get('/', response_class=HTMLResponse)
async def read_items():
    return  """
    <html>
        <head>
            <title>Gide GitHub-Heroku</title>
        </head>
        <body>
            <h1>Launching a project on the Internet<h1>            
            <h3> Step 1. Create a repository on GitHub <h3>
            <h3> Step 2. Clone the repository to the computer. "git clone" command <h3>
            <h3> Step 3. create a .py file with the name of your project <h3>
            <h3> Step 4. Create a file without an extension. Give it the name "Procfile" <h3>
            <h3> Step 5. Write to Procfile - "web: uvicorn --host 0.0.0.0 --port $ PORT name_your_py_file: app" <h3>
            <h3> Step 6. Ceate a requirements.txt file and indicate in it what we are working with. For example, the first line is -fastapi
                    the second line is - uvicorn <h3>
            <h3> Step 7. Working with our .py file with the name of your project <h3>
            <h3> Step 8. Pushing everything to GutHub. "git add ." / "git commit -m 'text'" / "git push" <h3>
            <h3> Step 9. At https://dashboard.heroku.com create a new app <h3>
            <h3> Step 10. In "App connected" to GitHub choose our project <h3>
            <h3> Step 11. In the "Deployment method", select GitHub <h3>
            <h3> Step 12. In "Automatic deploys" press "Enable automatic deploys" <h3>
            <h3> Step 13. In "Manual deploy", select the necessary branch and click Deploy Branch <h3>
            <h3> Step 14. Watch the build results in the Activity tab <h3>
            <h3. Step 15. Click Open app. Share the link. Enjoy :-) <h3>


        </body>
    </html>
    """