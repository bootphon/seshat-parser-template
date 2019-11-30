from seshat.parsers.base import BaseCustomParser, AnnotationError


# Your class HAS TO inherit from BaseCustomParser
class MyCustomParser(BaseCustomParser):
    """An example custom parser class"""
    NAME = "My Parser"  # this name should be unique, and will be displayed in Seshat's interface
    LANGUAGE = None

    def check_annotation(self, annot: str) -> None:
        """You should check the annotation in this function. If anything's
        wrong with the annotation, raise an `AnnotationError` to tag it
        as invalid.
        This function shouldn't return anything."""
        pass
