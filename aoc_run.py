#!/usr/bin/env python
from functools import wraps
from importlib import import_module
import inspect
from pathlib import Path
from timeit import timeit

from cleo import Application
from cleo import Command as BaseCommand
from pydantic import validate_call


ROOT_PATH = Path(__file__).resolve().parent
SEPERATOR = " " * 2


def perf(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        output = f(*args, **kwds)
        tit = timeit("f(*args, **kwds)", number=0, globals=locals())
        return output, tit

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
        year = str(
            self.option("year")
            or max(x for x in (x.name for x in ROOT_PATH.glob("*") if x.is_dir()) if x.startswith("20"))
        )

        day = (
            f'{self.argument("day"):0>2}'
            if self.argument("day")
            else max(x for x in (x.name for x in (ROOT_PATH / year).glob("*") if x.is_dir()))
        )
        days = [day]
        if day.lower() == "all":
            days = sorted(x.name for x in (ROOT_PATH / year).glob("*") if x.is_dir())

        parts = (self.argument("part"),) if self.argument("part") else ("1", "2")

        for day in days:
            day_module = import_module(f"{year}.{day}")
            print(day_module.__name__)
            funcs = list(
                x for x in inspect.getmembers(day_module, predicate=inspect.isfunction) if not x[0].startswith("_")
            )
            for part in parts:
                path = ROOT_PATH / f"{year}/{day}"
                cast_func = day_module.__dict__.get(f"part{part}_cast_input", day_module.__dict__["cast_input"])
                cast_func = validate_call(validate_return=True)(cast_func)
                input_file = path / f"part{part}.input"
                if not Path(input_file).is_file():
                    input_file = path / "input"
                    if not Path(input_file).is_file():
                        continue
                with open(input_file) as f:
                    input_data = cast_func(f.read())
                print(SEPERATOR + f"part-{part}")
                for _, func in list(filter(lambda x: x[0].endswith(f"part{part}"), funcs)):
                    func = validate_call(validate_return=True)(func)
                    print(
                        SEPERATOR * 2 + f"ƒ {func.__name__}",
                    )
                    output, tit = None, -1
                    try:
                        output, tit = self._run(func, input_data)
                    except BaseException as e:
                        output = e
                    print(SEPERATOR * 3 + "\033[90m" + f"{tit:f}" + "\033[0m", output)

            print()

    @perf
    def _run(self, func, input_data):
        return func(input_data)


if __name__ == "__main__":
    app = Application()
    command = RunCommand()
    app.add(command)
    from sys import argv

    from clikit.args import ArgvArgs

    app.run(ArgvArgs([argv[0], command._config._name] + argv[1:]))
