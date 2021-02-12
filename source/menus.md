# Menus in Game

## Menu Statement in dialogue

```gdscript
var choice = menu(array_of_choices, parameters)
```

1. Array of choices every choice is 3 element list like this:
   ```gdscript
   ["choice label", variable_to_return, parameters]
   ```
   1. Choice label that can use chosen [markup](text.md).
   1. Variable to return when this choice is chosen.
   1. Additional parameters in from of dictionary, default empty. Build in parameters:
      - `visible` - can show/hide choice from player if true/false.
1. Additional parameters in from of dictionary, default empty.
   There are no build in parameters for this statement

Example of menu:

```gdscript
say (null , "Choose one option.")
var choice = menu([
    ["A", "a", {}],
    ["B", "b", {}],
])

if cond(choice == 1):
	if is_active():
        say(null, "You choose First choice")

elif cond(choice == 2):
	if is_active():
        say(null, "You choose Second choice")

say (null , "Choose second option.")
var choice = menu([
    ["Only visible if \"A\" was chosen", 1, {"visible":choice == "a"}],
    ["Only visible if \"B\" was chosen", 2, {"visible":choice == "b"}],
    ["Always visible", 3, {}],
])
```

<!-- todo add screen shots -->

## Custom Menus

### Graphical Menus
