# seshat-parser-template

This is a template for pluginizable parsers that can be used by the 
[Seshat Annotation Manager](https://github.com/bootphon/seshat).

You can find an example of functionnal parsers here : 
[Seshat Sampa Parsers](https://github.com/bootphon/seshat-sampa-parser)

## Implementing your Parser(s)

TODO

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
