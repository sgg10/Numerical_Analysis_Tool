from . import api

@api.route('/test')
def test():
  return {"msg": "Test"}