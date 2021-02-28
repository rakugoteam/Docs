# Adding Multiple Styles of Displaying Dialogue

## Edit GUI Template

This tutorial show you how you can and your own other ways of displaying Dialogues.
For that we need to change gui template and gui is for you to be changed if you need that.

In your project open *gui/InGame/InGameGUI.tscn* scene.

*Tip: You can use short cut `Shift + Ctrl + O`*

![](styles_of_displaying_dialogue/find_scene.gif)

Node that handle displaying dialogue is **InGameGUI/DialoguePanel**.

![](styles_of_displaying_dialogue/dialogue_panel.png)

## How DialoguePanel Works ?

If you look into it script you will see that 
you only need to connect your node to signal `"say"`
so it will receive call dialogue `say()` funcs.
```gdscript
Rakugo.connect("say", self, "_on_say")
```

```gdscript
extends PanelContainer

func _ready():
  Rakugo.connect("say", self, "_on_say")
  Rakugo.connect("ask", self, "_on_ask")

func _on_say(_character, _text, _parameters):
  $HideTimer.stop()
  show()

func _on_ask(_default_answer, _parameters):
  $HideTimer.stop()
  show()

func _step():
  $HideTimer.start()

func _on_HideTimer_timeout():
  hide()
```

## Edit Original Script to use Parameters

We need add some way to switch between dialogue displays,
for this we will use parameters.

````{note}
In this tutorial I use only `style` parameter, but you can add and use whatever parameters you want.
For example `pos` to set DialoguePanel position:

```gdscript
func _on_say(_character, _text, _parameters):
  if _parameters.has("pos"):
    rect_position = _parameters["pos"]
    $HideTimer.stop()
    show()

```
````

```gdscript
extends PanelContainer

# export keyword make possible edit var through Inspector
export var style = "default"

func _ready():
  Rakugo.connect("say", self, "_on_say")
  Rakugo.connect("ask", self, "_on_ask")

func _on_say(_character, _text, _parameters):
  hide()
  if _parameters.has("style"):
		if _parameters["style"] == style:
      $HideTimer.stop()
      show()

func _on_ask(_default_answer, _parameters):
  hide()
  if _parameters.has("style"):
		if _parameters["style"] == style:
      $HideTimer.stop()
      show()

func _step():
  $HideTimer.start()

func _on_HideTimer_timeout():
  hide()
```

This code make Rakugo use this dialogue style if it will look like this:
```gdscript
extends Dialogue

func default_style():
  start_event("default_style")

  say(null, "This text show in default dialogue style.", {"style": "default"})
  step()

  end_event()
```

To make it automatic edit **Project Settings**.
Open *Project > Project Settings*.
Then go to *rakugo/default*
![](../topics/project_setup/project-settings-defaults.png)

Next edit parameters for **Say** and **Ask**.
![](styles_of_displaying_dialogue/defaults.gif) 

```{note}
Must click on *Add Key/Value Pair* to confirm.
```

## Add Other Style of Display Dialogue

First duplicate **DialoguePanel**.
```{tip}
You can use `Ctrl + D` shortcut for this.
```

Change node name and `style` value.
In this example I will add DialoguePanel to top of screen.

![](styles_of_displaying_dialogue/new_dp.gif)

Change new DialoguePanel as you need.

![](styles_of_displaying_dialogue/top_dp.gif)

## Test it

```gdscript
extends Dialogue

func default_style():
  start_event("default_style")

  say(null, "This text show in default dialogue style.")
  step()

  say(null, "This text show is show at top of the screen.", {"style": "top"})
  step()

  end_event()
```
Result:

![](styles_of_displaying_dialogue/result.gif)