import tomllib
class Project:
    def __init__(self, content):
        toml_str  = tomllib.loads(content)
        self.name = toml_str["tool"]["poetry"]["name"]
        self.description = toml_str["tool"]["poetry"]["description"]
        self.dependencies = toml_str["tool"]["poetry"]["dependencies"]
        self.dev_dependencies = toml_str["tool"]["poetry"]["group"]["dev"]["dependencies"]
        self.authors = toml_str["tool"]["poetry"]["authors"]
    def _stringify_dependencies(self, dependencies):
        return "\n - ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\n\n Authors: \n - {self._stringify_dependencies(self.authors)}"
            f"\n\nDependencies: \n - {self._stringify_dependencies(self.dependencies)}"
            f"\n\nDevelopment dependencies: \n - {self._stringify_dependencies(self.dev_dependencies)}"
        )
