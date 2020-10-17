from . import multiRoots
from ..Methods.Open.MultiRoots import MultiRoots

@multiRoots.route('/<x0>&<tol>&<iterations>&<function>')
def multiRootMethod(x0, tol, iter, function):
  return MultiRoots(x0, tol, iter, function).run()