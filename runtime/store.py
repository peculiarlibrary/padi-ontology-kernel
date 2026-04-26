from rdflib import Graph
import copy


class RDFStore:
    _graph = None
    _path = None

    @classmethod
    def load(cls, path):
        cls._graph = Graph()
        cls._graph.parse(path, format="json-ld")
        cls._path = path
        return cls._graph

    @classmethod
    def get(cls):
        return cls._graph

    @classmethod
    def clone(cls):
        return copy.deepcopy(cls._graph)

    @classmethod
    def replace(cls, new_graph):
        cls._graph = new_graph

    @classmethod
    def save(cls):
        if cls._graph and cls._path:
            cls._graph.serialize(destination=cls._path, format="json-ld", indent=2)
