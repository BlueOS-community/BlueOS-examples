from robyn import Robyn

app = Robyn(__name__)

@app.get("/hello")
async def root():
    return "Hello from the Robyn backend!"


def main():
    app.serve_directory(
        route="/",
        directory_path="/frontend",
        index_file="/frontend/index.html",
        show_files_listing=False,
    )
    app.start(host="0.0.0.0", port=8123)


if __name__ == "__main__":
    main()
