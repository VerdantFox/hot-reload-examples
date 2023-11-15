# Hot reload examples

Example project to get hot-reload for Python, HTML, CSS, and other file changes for FastAPI and Flask template projects. However, it should work with any Python framework with `--reload` functionality.

To run the `FastAPI` example, `cd` into the `fastapi` directory and follow the steps below. Similarly, to run the `Flask` example, `cd` into the `flask` directory and follow the steps below.

## Installations

These are the installations you'll need to perform to get this working.

### For both FastAPI and Flask

- NodeJS (google installation for your OS)
- npm (google installation for your OS)
- [browser-sync](https://browsersync.io/). The following command will install it globally.

  ```bash
  npm install -g browser-sync
  ```

### For FastAPI

- fastapi
- uvicorn[standard]
- jinja2

These can be installed with `pip install fastapi "uvicorn[standard]" jinja2`.

### For Flask

- flask
- gunicorn

These can be installed with `pip install flask gunicorn`.

## The steps

1. Run the server with `--reload`, specifying the files to look for when reloading.

   - `FastAPI` with `uvicorn`:

     ```bash
     uvicorn main:app --reload --reload-include="*.html" --reload-include="*.css" --reload-include="*.js"
     ```

     The above command will run a server on `http://localhost:8000` and watch for changes to Python files (default) and CSS, HTML, and JS files (according to the glob patterns we provided).

   - `Flask` with `gunicorn`:

     ```bash
     gunicorn main:app --reload --reload-extra-file="templates/index.html" --reload-extra-file="static/styles.css"
     ```

     The above command will run a server on `http://localhost:8000` and watch for changes to Python files (default), `templates/index.html`, and `static/styles.css`. Annoyingly, `gunicorn` currently does not allow you to specify glob patterns, so you must specify each non-python file to watch for changes.

   - Alternatively, you could run `Flask` with the Flask development server:

     ```bash
     flask --app main:app run --debug --extra-files templates/index.html:static/styles.css
     ```

     Use `;` on Windows to separate the `--extra-files` instead of `:`. The above command will run a server on `http://localhost:5000` and watch for changes to Python files (default), `templates/index.html`, and `static/styles.css`. Annoyingly, like with gunicorn, `flask` does not allow you to specify glob patterns, so you must specify each non-python file to watch for changes.

2. Run [browser-sync](https://browsersync.io/) in watch mode, specifying the address to proxy and the static files path.

   ```bash
   browser-sync 'http://localhost:8000' 'static' --watch --files .
   ```

   Change the `localhost` port to the port your server is running on if it differs from `8000`. The above command will run a server on `http://localhost:3000` and proxy requests to `http://localhost:8000` (your server running FastAPI or Flask). It will also forward static files from the `static` directory (you can change the static files directory with the second argument to `browser-sync`). Finally, it will watch for changes to all files relative to the working directory and reload the browser when they change.

   Go to `http://localhost:3000`.

3. Turn off caching in your browser

   By default, browsers will cache static files. Therefore, you might not see changes to CSS and JavaScript files reflected in the browser, as the browser will use the stale cached after the first load. To fix this, you will need to turn off caching in your browser. For Chrome, you can do this with the following steps:

   1. Open the browser to `http://localhost:3000`
   2. Right-click on the browser page
   3. Click "Inspect" to open dev tools
   4. Navigate to the "Network" tab
   5. Check "Disable cache"
