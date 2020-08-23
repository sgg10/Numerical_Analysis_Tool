from app import create_app

app = create_app()

# Error Handlers
@app.errorhandler(500)
def internal_server_error(error):
  return {
    "name": "Error 500 - Internal Server Error",
    "msg": error
  }

@app.errorhandler(404)
def not_found(error):
  return {
    "name": "Error 404 - Not Found",
    "msg": error
  }

# Routes