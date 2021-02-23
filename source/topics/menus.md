# Menus in Game

## Menu Statement in Dialogue

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
```

![](menus/dialogue_menu1.png)

```gdscript
# continuation of the previous script
if cond(choice == 1):
	if is_active():
        say(null, "You choose First choice")

elif cond(choice == 2):
	if is_active():
        say(null, "You choose Second choice")

say (null , "Choose another option.")
var choice = menu([
    ["Only visible if \"A\" was chosen", 1, {"visible":choice == "a"}],
    ["Only visible if \"B\" was chosen", 2, {"visible":choice == "b"}],
    ["Always visible", 3, {}],
])
```

![](menus/dialogue_menu2.png)

## Custom Menus

To crate custom menu use **Container** node like:

- **VBoxContainer**
- **HBoxContainer**
- **GridContainer**

Add some **Buttons** to **Container**:

![](menus/button_types.png)