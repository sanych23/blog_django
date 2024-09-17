import os
from pprint import pprint
import importlib


class Main:
    dirs = list()
    list_modules = list()

    def __init__(self) -> None:
        self.scan()
        self.modules()
        self.sort_modules()

    def scan(self):
        dir = os.scandir(path="seeds/tables")
        for item in dir:
            if "__" in item.name:
                continue
            self.dirs.append(item)
        dir.close()
        return dir
    
    def modules(self):
        for dir in self.dirs:
            seed_name = f"{dir.name[0:-3].capitalize()}Seed"
            module = getattr(importlib.import_module(f"seeds.tables.{dir.name[0:-3]}", package=seed_name), seed_name)
            self.list_modules.append(module())
            
    def sort_modules(self):
        self.list_modules.sort(key=lambda module: module.order)
    
    def start(self):
        self.delete()
        for module in self.list_modules:
            module.start()
            print(f"Seed {module} complete!")

    def delete(self):
        for module in self.list_modules[::-1]:
            module.delete()
            print(f"Delete {module} complete!")
