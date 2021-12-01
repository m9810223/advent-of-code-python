#!/usr/bin/env python
from cleo import Application, Command as BaseCommand


import inspect
from importlib import import_module
from pathlib import Path
from traceback import print_exc
from time import perf_counter
from timeit import timeit
from functools import wraps


ROOT_PATH = Path(__file__).resolve().parent


def perf(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        start_time = perf_counter()
        result = f(*args, **kwds)
        time = perf_counter() - start_time
        tit = timeit('f(*args, **kwds)', number=10**3, globals=locals())
        print(f'(1k, 1) -> ({tit}, {time})')
        return result
    return wrapper


class RunCommand(BaseCommand):
    """
    adventofcode
    run
        {--y|year= : year}
        {day? : day}
        {part? : 1 or 2}
    """

    def handle(self):
        year = self.option('year') or max(
            x for x in (x.name for x in ROOT_PATH.glob("*") if x.is_dir())
            if x.startswith('20')
        )
        day = f'{self.argument("day"):0>2}' if self.argument("day") else max(
            x for x in (x.name for x in (ROOT_PATH/year).glob(f"*") if x.is_dir())
        )
        parts = (self.argument('part'),) if self.argument('part') else ('1', '2')
        day_module = import_module(f'{year}.{day}')
        print(day_module)
        funcs = list(
            x for x in inspect.getmembers(day_module, predicate=inspect.isfunction)
            if not x[0].startswith('_')
        )
        for part in parts:
            path = ROOT_PATH/f'{year}/{day}/part{part}'
            cast_func = day_module.__dict__.get(f'part{part}_cast_input', day_module.__dict__['cast_input'])
            input_file = f'{path}.input'
            if not Path(input_file).is_file():
                continue
            with open(input_file) as f:
                input_data = list(map(cast_func, f.read().split('\n')))
            for _, func in list(filter(lambda x: x[0].endswith(f'part{part}'), funcs)):
                print('_'*80)
                print(func)
                try:
                    output = self._run(func, input_data)
                    print(f'{output = }')
                except BaseException:
                    print_exc()
        print()

    @perf
    def _run(self, module, input_data):
        return module(input_data)


if __name__ == '__main__':
    application = Application()
    application.add(RunCommand())
    application.run()
