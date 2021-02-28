# Variables and Conditions

## Variables and Constans in GDScript

Variables are box with labels for values that **can** change.
Constans are box with labels for values that **can't** change.
In GDScript you can define new local variables and constans for script.

```gdscript
# Member variables

var a = 5
var s = "Hello"
var arr = [1, 2, 3]
var dict = {"key": "value", 2: 3}
var typed_var: int
var inferred_type := "String"

# Constants

const ANSWER = 42
const THE_NAME = "Charly"

# Enums

enum {UNIT_NEUTRAL, UNIT_ENEMY, UNIT_ALLY}
enum Named {THING_1, THING_2, ANOTHER_THING = -1}

# Built-in vector types

var v2 = Vector2(1, 2)
var v3 = Vector3(1, 2, 3)

# and more
```

```{note}
[More types are listed in godot docs.](https://docs.godotengine.org/en/stable/getting_started/scripting/gdscript/gdscript_basics.html#built-in-types)
```

## Variables in Rakugo

With Rakugo it possible to define global variables that are automatically part of game save.

```gdscript
Rakugo.StoreManager.set("variable_name", value)
```

This support all GDScript base types, but **not** `null`.
To get null-like variable in Rakugo use `"nothing"`.

```gdscript
Rakugo.StoreManager.set("null_variable", "nothing")
```

Get global Rakugo variable value:

```gdscript
var value_to_load = Rakugo.StoreManager.get("variable_name")
```

## Conditions

In GDScript normal functions conditions look like this:

```gdscript
func some_function(param1, param2):
    var local_var = 5

    if param1 < local_var:
        print(param1)
    elif param2 > 5:
        print(param2)
    else:
        print("Fail!")
```

But in Rakugo dialogue event conditions are a little bit more complicated.

```gdscript
if cond(choice == 1):
  say(null, "You choose First choice")

elif cond(choice == 2):
  say(null, "You choose Second choice")
```

Conditions in Rakugo are constructed like this:

```gdscript
if cond(condition):
```

This is like normal `if`, but for dialogue event.
Can be also used with `elif`.

