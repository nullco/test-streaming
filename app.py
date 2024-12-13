from flask import Flask
import time
import lorem


app = Flask(__name__)


@app.route('/stream')
def stream():
    def generate():
        txt = lorem.text()
        for word in txt.split():
            yield word
            yield ' '
            time.sleep(1)
    return generate(), {'Content-Type': 'text/html'}


@app.route('/')
def index():
    return """
    <html>
        <body>
            <div id='content'></div>
            <script>
            content = document.getElementById('content')
            async function callStreamingAPI() {
                const response = await fetch("http://localhost:8000/stream");
                const reader = response.body.getReader();
                const decoder = new TextDecoder();

                let done = false;
                while (!done) {
                    const { value, done: readerDone } = await reader.read();
                    if (value) {
                        content.innerHTML = content.innerHTML + decoder.decode(value)
                    }
                    done = readerDone;
                }
            }
            callStreamingAPI();
            </script>
        </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=True)
