from . import incremental_search
from ..Methods.Intervals.Incremental_Search import Incremental_Search

@incremental_search.route('/<x0>&<delta>&<iteration>&<function>')
def incremental_search_method(x0, delta, iteration, function):
  return Incremental_Search(x0, delta, iteration, function).run()