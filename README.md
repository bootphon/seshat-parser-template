# seshat-parser-template

This is a template for pluginizable parsers that can be used by the 
[Seshat Annotation Manager](https://github.com/bootphon/seshat).

You can find an example of functionnal parsers here : 
[Seshat Sampa Parsers](https://github.com/bootphon/seshat-sampa-parser)

## Implementing your Parser(s)

You can make several parser classes available in your module, but each of them 
has to comply with the the following requirements:

* Your parser class has to inherit from the `BaseCustomParser` that is made
    available by the `seshat-server` package.

```python
from seshat.parsers.base import BaseCustomParser

class MyFirstCustomParser(BaseCustomParser):
    """An example custom parser class"""

class MySecondCustomParser(BaseCustomParser):
    """Another custom parser class"""
```

* Your parser class **has** to implement _at least_ the `check_annotation` 
    method. It takes an annotation (type `str`) as an input and shouldn't return 
    anything. If the annotation is deemed invalid by your parser, the an 
    `ÀnnotationError` should be raised.
  
```python
from seshat.parsers.base import BaseCustomParser, AnnotationError

class UpperCaseChecker(BaseCustomParser):
    """A parser that checks if an annotation is uppercase"""
    
    def check_annotation(self, annot: str) -> None:
        if not annot.upper() == annot:
            raise AnnotationError("This annotation isn't uppercase")
```
    The error message in the AnnotationError exception will be shown to the 
    annotator when they submit the file.
  
* The default name for the class (displayed in Seshat's interface) is its class 
    name. If you will to have a more human-friendly name, you can set the 
    `NAME` attribute:
      
```python
    from seshat.parsers.base import BaseCustomParser
    
    class SuperFancyParserClassName(BaseCustomParser):
        """An example custom fancy parser class"""
        NAME = "Fancy Parser"
```

* You can also specify an example valid and invalid annotations. These can 
    be useful for documenting the parser's behavior, but also are used by the 
    `check-parsers` CLI tool from Seshat's package to do some basic sanity 
    checks on the detected parsers:

```python
from seshat.parsers.base import BaseCustomParser, AnnotationError

class UpperCaseChecker(BaseCustomParser):
    """A parser that checks if an annotation is uppercase"""
    VALID_ANNOT_EXAMPLE = "AN UPPERCASE SENTENCE"
    INVALID_ANNOT_EXAMPLE = "this is not uppercase"
    
    def check_annotation(self, annot: str) -> None:
        if not annot.upper() == annot:
            raise AnnotationError("This annotation isn't uppercase")
```

* Last, but not least: you can add a `distance` method that will allow Seshat 
    to compute inter-annotator (or inter-rater) agreement on tiers that are
    checked by that parser. That method takes two annotations as input and 
    returns a float. That distance function is expected to comply with the 
    [mathematical definition of a distance](https://en.wikipedia.org/wiki/Metric_(mathematics).

```python
from seshat.parsers.base import BaseCustomParser, AnnotationError
from leveinstein import levenstein_dist

class UpperCaseChecker(BaseCustomParser):
    """A parser that checks if an annotation is uppercase"""
    VALID_ANNOT_EXAMPLE = "AN UPPERCASE SENTENCE"
    INVALID_ANNOT_EXAMPLE = "this is not uppercase"
    
    def check_annotation(self, annot: str) -> None:
        if not annot.upper() == annot:
            raise AnnotationError("This annotation isn't uppercase")
    
    def distance(self, annot_a: str, annot_b: str):
        """Computes the levenstein edit distance between two strings"""
        return levenstein_dist(annot_a, annot_b)
```

**NOTE : this method shouldn't raise any `AnnotationError`. Seshat will
make sure that all annotations that go through this method are all valid.**

Your last step is to make sure that all your valid parser classes are imported
in your module's `__init__.py` (as Seshat will look for your parsers in there).

## Configuring the `setup.py`

TODO

## Installation and Testing

Make sure you already set up a working python virtual environment with the
[Seshat Server](https://github.com/bootphon/seshat-restful-server) package installed in it. If that isn't the case:

 1. git clone the [Seshat Server](https://github.com/bootphon/seshat-restful-server)'s repo somewhere else
 2. create a virtual environment in the cloned repo, and activate it
 3. install the `seshat-server` package with `python setup.py install`

Once this is done, and you've made sure that the environment is activated, go back to your parser module's folder,
and run:

```shell script
python setup.py install
```

Or, if you've uploaded your package to a github repo (also works with gitlab):

```shell script
pip install git+git://github.com/myuser/seshat-parser-mymodule
```

You can then proceed to test the module using Seshat's CLI:
```shell script
check-parser --list # will list all detected parsers (hopefully includin yours)
check-parser --parser MyParserClass # will run checks on your parser to see if complies with seshat
# will run your parser on an annotation and return its validity
check-parser --parser MyParserClass --annot "This is a test annotation"
```
