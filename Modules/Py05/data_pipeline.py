from abc import ABC, abstractmethod
from typing import Any
from typing import Protocol
import re

type Number = int | float

class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: list[tuple[int, str]] = []
        self.index: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.data:
            raise Exception("No data to output")
        return self.data.pop(0)

class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        
        if isinstance(data, list):
            return all(
                isinstance(item, (int, float))
                for item in data
            )
        return False
    
    def ingest(self, data: Number | list[Number]) -> None:
        if not self.validate(data):
            raise Exception("Invalid Numeric data")
        
        items: list[Number] = data if isinstance(data, list) else [data]

        for item in items:
            self.data.append((self.index, str(item)))
            self.index += 1

class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        
        if isinstance(data, list):
            return all(
                isinstance(item, str)
                for item in data
            )
        return False
    
    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Invalid Text data")
        
        items: list[str] = data if isinstance(data, list) else [data]

        for item in items:
            self.data.append((self.index, item))
            self.index += 1

class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict) and all(
            isinstance(k, str) and isinstance(v, str)
            for k, v in data.items()
        ):
            return True
        
        if isinstance(data, list):
            return all(
                isinstance(item, dict) and all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in item.items())
                for item in data
            )
        return False
    
    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Invalid Log data")
        
        items: list[dict[str, str]] = data if isinstance(data, list) else [data]

        dictList = [f"{d['log_level']}: {d['log_message']}" for d in items]
        # dictList = [': '.join(d.values()) for d in items]

        for item in dictList:
            self.data.append((self.index, item))
            self.index += 1

class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass

class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        name = re.sub(r'(?<!^)(?=[A-Z])', ' ', proc.__class__.__name__)
        print(f"\n== Registering {name} ==")
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        print("\n== Processing stream ==")
        print(f'Stream: {stream}')
        for element in stream:
            processor = next(
                (p for p in self.processors if p.validate(element)), None
            )
            if processor is None:
                print(f"DataStream error - Can't process element in stream: {element}")
            else:
                processor.ingest(element)

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for p in self.processors:
            name = re.sub(r'(?<!^)(?=[A-Z])', ' ', p.__class__.__name__)
            print(f"{name}: total {p.index} items processed, remaining {len(p.data)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        name = plugin.__class__.__name__
        print(f'\nSend {nb} processed data from each processor to a {name} plugin:')
        for proc in self.processors:
            outList: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    outList.append(proc.output())
                except Exception:
                    pass
            plugin.process_output(outList)


class CSV:
    def __init__(self) -> None:
        pass
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print('CSV Output:')
        print(', '.join(elem[1] for elem in data))

class JSON:
    def __init__(self) -> None:
        pass
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pairs = (f'\"item_{item[0]}\": \"{item[1]}\"' for item in data)
        print('JSON Output:')
        print('{' + ', '.join(pairs) + '}')

def main():
    boss = DataStream()
    np = NumericProcessor()
    tp = TextProcessor()
    lp = LogProcessor()
    stream: list[Any] = ['Hello world', [3.14, -1, 2.71], [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, {'log_level': 'INFO', 'log_message': 'User wil is connected'}], 42, ['Hi', 'five']]
    stream2: list[Any] =  [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'], [{'log_level': 'ERROR', 'log_message': '500 server crash'}, {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'}], [32, 42, 64, 84, 128, 168], 'World hello']
    csv = CSV()
    json = JSON()

    boss.print_processors_stats()

    boss.register_processor(np)
    boss.register_processor(tp)
    boss.register_processor(lp)

    boss.process_stream(stream)

    boss.print_processors_stats()

    boss.output_pipeline(3, csv)

    boss.print_processors_stats()

    boss.process_stream(stream2)

    boss.print_processors_stats()

    boss.output_pipeline(5, json)

    boss.print_processors_stats()


if __name__ == "__main__":
    main()