from mensaup_api.app import app


def run():
    app.run(port=8080, debug=False, server='flask')


def run_debug():
    app.run(port=8080, debug=True, server='flask')
