from urllib import request
from project import Project
import tomllib

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = str(request.urlopen(self._url).read().decode("utf-8"))
        # print("content:", content)
        # toml_str  = tomllib.loads(content)

        # print("toml_str: ",toml_str)

        # print("a")
        # print(toml_str["tool"]["poetry"]["description"])
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(content)

