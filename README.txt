Demo
====

Run `make html` in this directory. The output should contain the following
error message:

```
/**/demo_module.py:docstring of demo_module.bar:22: WARNING: Exception occurred in plotting index-1 from /**/index.rst:
Traceback (most recent call last):
  File "/**/site-packages/matplotlib/sphinxext/plot_directive.py", line 524, in run_code
    six.exec_(code, ns)
  File "<string>", line 2
    but end the docstring with a text line right after invoking `plt.show()` the
          ^
SyntaxError: invalid syntax
```

Open the file `_build/html/index.html` and compare how the docstrings of the
two functions are rendered. One doesn't contain the expected plot!