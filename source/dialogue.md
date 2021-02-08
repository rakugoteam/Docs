# Dialogue and Narration

Functions (called _statements_) listed below you should use them as part of [dialogue event](dialogue_node.html#create-dialogue-event).

```{note}

You can call this functions from Rakugo like: `Rakugo.say()`, but we don't recommend this.
```

## Say Statement

This function is like this:

```gdscript
say("character_tag", "Text to say by character.", parameters)
```

Args:

1. Tag of character set when you create character, if `null` then it will use default [Narrator](project_setup.html#Narrator)
1. Text to be sed by character it can use [markup](text.md)
1. Additional parameters in from of dictionary, default empty.

Build in additional parameters:

- `markup` - use different then default markup for this dialogue part.

Additional parameters from visual novel template:

- `typing` - turn on/off typing effect for this dialogue.
- `typing_effect_delay` - overwrite typing effect delay for this part of dialogue.
- `typing_effect_punctuation_factor` - overwrite typing effect punctuation factor for this part of dialogue.

## Define Character

To define new character use this function:

```gdscript
Rakugo.define_character("Character Name", "character_tag", character_label_tag)
```

For example:

```gdscript
Rakugo.define_character("Cool Developer", "cool", Color.blue)
```

Use this example character in dialogue:

```gdscript
# this example uses markdown as markup
say("cool", "I'm cool :sunglasses: Developer")
```

<!-- todo add screen shot -->

## Ask Statement

This function can be used to get information (as string) from player.

```gdscript
var player_input = ask("default_answer", parameters)
```

1. default value returned by ask if player just press enter and don't provided any input or empty string
2. Additional parameters in from of dictionary, default empty.

Additional parameters from visual novel template:

- `placeholder` - text to display as hit for player, it will disappear if player start to provided input

Example of using ask to get player character name.

```gdscript
extends Dialogue

onready var player_ch = Rakugo.define_character("Player-kun", "player", Color.aqua)

func first_dialogue():
	start_event("first_dialogue")

  # this example use markdown as markup
	say(null, "What is your name? (default: _<player.name>_.)", {"typing":false})

	var player_name = ask("", {"placeholder": "Player Name"})

	if cond(player_name != null):
		if is_active():
			player_ch.name = player_name

	step()
```

```{note}
<!-- add link -->
What are `cond()` and `is_active()` is explained here.
```

This code give us this result in visual novel template:
![](_images/dialogue/ask.png)

## Notify

This can be used to notify player of consequences of their decisions.

```gdscript
notify("notification text", parameters)
```

1. Text to be sed by character it can use [markup](text.md)
1. Additional parameters in from of dictionary, default empty.
   There are no build in parameters for this statement.

For example:

```gdscript
notify("[elie.name] will remember this.")
```

<!-- todo add screen shot -->
