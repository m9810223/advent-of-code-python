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
        output = f(*args, **kwds)
        time = perf_counter() - start_time
        tit = timeit('f(*args, **kwds)', number=10**2, globals=locals())
        return output, tit, time
    return wrapper


class RunCommand(BaseCommand):
    """
    adventofcode
    aoc_run.py
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
        days = [day]
        if day.lower() == 'all':
            days = sorted(
                x.name for x in (ROOT_PATH/year).glob(f"*") if x.is_dir()
            )

        parts = (self.argument('part'),) if self.argument('part') else ('1', '2')

        for day in days:
            day_module = import_module(f'{year}.{day}')
            print(day_module.__name__)
            funcs = list(
                x for x in inspect.getmembers(day_module, predicate=inspect.isfunction)
                if not x[0].startswith('_')
            )
            for part in parts:
                path = ROOT_PATH/f'{year}/{day}'
                cast_func = day_module.__dict__.get(f'part{part}_cast_input', day_module.__dict__['cast_input'])
                input_file = path/f'part{part}.input'
                if not Path(input_file).is_file():
                    input_file = path/'input'
                    if not Path(input_file).is_file():
                        continue
                with open(input_file) as f:
                    input_data = cast_func(f.read())
                for _, func in list(filter(lambda x: x[0].endswith(f'part{part}'), funcs)):
                    print(' '*2 + f'{day_module.__name__}.{func.__name__}: ', end='')
                    try:
                        output, tit, time = self._run(func, input_data)
                        print(output)
                        print(' '*4 + '\033[90m'+f'(100, 1): ({tit:f} sec, {time:f} sec)', '\033[0m')
                    except BaseException:
                        print_exc()
        print()

    @perf
    def _run(self, module, input_data):
        return module(input_data)


if __name__ == '__main__':
    app = Application()
    command = RunCommand()
    app.add(command)
    from sys import argv
    from clikit.args import ArgvArgs
    app.run(
        ArgvArgs([argv[0], command._config._name] + argv[1:])
    )
