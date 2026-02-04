# Gitwork Test Satellite

Test repository with submodule support.

## Submodules
- `libs/greeting`: Greeting library with formal and casual options

## Usage
```python
from libs.greeting.lib import greet, formal_greet
print(greet("World"))
print(formal_greet("Smith", "Dr."))
```
