# Dialogue and Narration

Functions (called _statements_) listed below you should use them as part of [dialogue event](dialogue_node.md#create-dialogue-event).

```{admonition} Note
:class: Note

You can call this func for Rakugo like: `Rakugo.say()`, but we don't recommend this.
```

## Say Statement

This function is like this:

```gdscript
say("character_tag", "Text to say by character.", {})
```

Args:

1. Tag of character set when you create character, if `null` then it will use default [Narrator](project_setup.html#Narrator)
2. Text to be sed by character it can use [markup](text.md)
3. Additional parameters in from of Dictionary, default empty.
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
