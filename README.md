# Gitwork Test Satellite

Test repository with submodule support.

## Submodules
- `libs/greeting`: Greeting library with formal and casual options

## Usage
```python
from libs.greeting.lib import greet, farewell, formal_greet, casual_greet

print(greet("World"))
print(formal_greet("Smith", "Dr."))
print(casual_greet("Bob"))
print(farewell("Everyone"))
```
