# BBCode in RichTextLabel

## Introduction

Label nodes are great for displaying basic text, but they have limits.
If you want to change the color of the text, or its alignment, that
change affects all of the text in the Label node. You can't have only
one part of the text be one color, or only one part of the text be
centered. To get around this limitation you would use a
`class_RichTextLabel`.

`class_RichTextLabel` allows the display of complex text markup in a
Control. It has a built-in API for generating the markup, but can also
parse a BBCode.

Note that the BBCode tags can also be used, to some extent, in the XML
source of the class reference. For more information, see
`doc_class_reference_writing_guidelines`.

## Using BBCode

For uniformly formatted text you can write in the "Text" property, but
if you want to use BBCode markup you should use the "Text" property in
the "Bb Code" section instead (<span
class="title-ref">bbcode\_text</span>). Writing to this property will
trigger the parsing of your markup to format the text as requested.
Before this happens, you need to toggle the "Enabled" checkbox in the
"Bb Code" section (<span class="title-ref">bbcode\_enabled</span>).

![image](img/bbcodeText.png)

For example, <span class="title-ref">BBCode
\[color=blue\]blue\[/color\]</span> would render the word "blue" with a
blue color.

![image](img/bbcodeDemo.png)

You'll notice that after writing in the BBCode "Text" property the
regular "Text" property now has the text without the BBCode. While the
text property will be updated by the BBCode property, you can't edit the
text property or you'll lose the BBCode markup. All changes to the text
must be done in the BBCode parameter.

<div class="note">

<div class="title">

Note

</div>

For BBCode tags such as `[b]` (bold), `[i]` (italics) or `[code]` to
work, you must set up custom fonts for the RichTextLabel node first.

There are no BBCode tags to control vertical centering of text yet.

</div>

## Reference

|                    |                                                                                    |                                                                                              |
|--------------------|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Command            | Tag                                                                                | Description                                                                                  |
| **bold**           | <span class="title-ref">\[b\]{text}\[/b\]</span>                                   | Makes {text} bold.                                                                           |
| \**italics* \*     | <span class="title-ref">\[i\]{text}\[/i\]</span>                                   | Makes {text} italics.                                                                        |
| **underlin e**     | <span class="title-ref">\[u\]{text}\[/u\]</span>                                   | Makes {text} underline.                                                                      |
| **striketh rough** | <span class="title-ref">\[s\]{text}\[/s\]</span>                                   | Makes {text} strikethrough.                                                                  |
| **code**           | <span class="title-ref">\[code\]{text}\[/code\]</span>                             | Makes {text} use the code font (which is typically monospace).                               |
| **center**         | <span class="title-ref">\[center\]{text}\[/center\] </span>                        | Makes {text} horizontally centered.                                                          |
| **right**          | <span class="title-ref">\[right\]{text}\[/right\]</span>                           | Makes {text} horizontally right-aligned.                                                     |
| **fill**           | <span class="title-ref">\[fill\]{text}\[/fill\]</span>                             | Makes {text} fill the RichTextLabel's width.                                                 |
| **indent**         | <span class="title-ref">\[indent\]{text}\[/indent\] </span>                        | Increase the indentation level of {text}.                                                    |
| **url**            | <span class="title-ref">\[url\]{url}\[/url\]</span>                                | Show {url} as such, underline it and make it clickable.                                      |
| **url (ref)**      | <span class="title-ref">\[url=&lt;url&gt;\]{text}\[/url\] </span>                  | Makes {text} reference &lt;url&gt; (underlined and clickable).                               |
| **image**          | <span class="title-ref">\[img\]{path}\[/img\]</span>                               | Insert image at resource {path}.                                                             |
| **resized image**  | <span class="title-ref">\[img=&lt;width&gt;\]{path}\[/im g\]</span>                | Insert image at resource {path} using &lt;width&gt; (keeps ratio).                           |
| **resized image**  | <span class="title-ref">\[img=&lt;width&gt;x&lt;height&gt;\]{ path}\[/img\]</span> | Insert image at resource {path} using &lt;width&gt;×&lt;height&gt;.                          |
| **font**           | <span class="title-ref">\[font=&lt;path&gt;\]{text}\[/fo nt\]</span>               | Use custom font at &lt;path&gt; for {text}.                                                  |
| **color**          | <span class="title-ref">\[color=&lt;code/name&gt;\]{tex t}\[/color\]</span>        | Change {text} color; use name or \# format, such as <span class="title-ref">\#ff00ff</span>. |
| **table**          | <span class="title-ref">\[table=&lt;number&gt;\]{cells} \[/table\]</span>          | Creates a table with &lt;number&gt; of columns.                                              |
| **cell**           | <span class="title-ref">\[cell\]{text}\[/cell\]</span>                             | Adds cells with the {text} to the table.                                                     |

Built-in color names \~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~

List of valid color names for the \[color=&lt;name&gt;\] tag:

-   aqua
-   black
-   blue
-   fuchsia
-   gray
-   green
-   lime
-   maroon
-   navy
-   purple
-   red
-   silver
-   teal
-   white
-   yellow

Hexadecimal color codes \~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~

For opaque RGB colors, any valid 6-digit hexadecimal code is supported,
e.g. <span class="title-ref">\[color=\#ffffff\]white\[/color\]</span>.

For transparent RGB colors, any 8-digit hexadecimal code can be used,
e.g. <span class="title-ref">\[color=\#88ffffff\]translucent
white\[/color\]</span>. In this case, note that the alpha channel is the
**first** component of the color code, not the last one.

Image vertical offset \~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~

You use a custom font for your image in order to align it vertically.

1.  Create a <span class="title-ref">BitmapFont</span> resource
2.  Set this bitmap font with a positive value for the <span
    class="title-ref">ascent</span> property, that's your height offset
3.  Set the BBCode tag this way: <span
    class="title-ref">\[font=&lt;font-path&gt;\]\[img\]{image-path}\[/img\]\[/font\]</span>

## Animation effects

BBCode can also be used to create different text animation effects. Five
customizable effects are provided out of the box, and you can easily
create your own.

Wave \~\~\~\~

![image](img/wave.png)

Wave makes the text go up and down. Its tag format is <span
class="title-ref">\[wave amp=50 freq=2\]\[/wave\]</span>. <span
class="title-ref">amp</span> controls how high and low the effect goes,
and <span class="title-ref">freq</span> controls how fast the text goes
up and down.

Tornado \~\~\~\~\~\~\~

![image](img/tornado.png)

Tornao makes the text move around in a circle. Its tag format is <span
class="title-ref">\[tornado radius=5 freq=2\]\[/tornado\]</span>. <span
class="title-ref">radius</span> is the radius of the circle that
controls the offset, <span class="title-ref">freq</span> is how fast the
text moves in a circle.

Shake \~\~\~\~\~

![image](img/shake.png)

Shake makes the text shake. Its tag format is <span
class="title-ref">\[shake rate=5 level=10\]\[/shake\]</span>. <span
class="title-ref">rate</span> controls how fast the text shakes, <span
class="title-ref">level</span> controls how far the text is offset from
the origin.

Fade \~\~\~\~

![image](img/fade.png)

Fade creates a fade effect over the text that is not animated. Its tag
format is <span class="title-ref">\[fade start=4
length=14\]\[/fade\]</span>. <span class="title-ref">start</span>
controls the starting position of the falloff relative to where the fade
command is inserted, <span class="title-ref">length</span> controls over
how many characters should the fade out take place.

Rainbow \~\~\~\~\~\~\~

![image](img/rainbow.png)

Rainbow gives the text a rainbow color that changes over time. Its tag
format is <span class="title-ref">\[rainbow freq=0.2 sat=10
val=20\]\[/rainbow\]</span>. <span class="title-ref">freq</span> is the
number of full rainbow cycles per second, <span
class="title-ref">sat</span> is the saturation of the rainbow, <span
class="title-ref">val</span> is the value of the rainbow.

## Custom BBCode tags and text effects

You can extend the `class_RichTextEffect` resource type to create your
own custom BBCode tags. You begin by extending the
`class_RichTextEffect` resource type. Add the <span
class="title-ref">tool</span> prefix to your GDScript file if you wish
to have these custom effects run within the editor itself. The
RichTextLabel does not need to have a script attached, nor does it need
to be running in <span class="title-ref">tool</span> mode. The new
effect will be activable in the Inspector through the **Custom Effects**
property.

There is only one function that you need to extend: <span
class="title-ref">\_process\_custom\_fx(char\_fx)</span>. Optionally,
you can also provide a custom BBCode identifier simply by adding a
member name <span class="title-ref">bbcode</span>. The code will check
the <span class="title-ref">bbcode</span> property automatically or will
use the name of the file to determine what the BBCode tag should be.

<span class="title-ref">\_process\_custom\_fx</span>
\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~

This is where the logic of each effect takes place and is called once
per character during the draw phase of text rendering. This passes in a
`class_CharFXTransform` object, which holds a few variables to control
how the associated character is rendered:

-   <span class="title-ref">identity</span> specifies which custom
    effect is being processed. You should use that for code flow
    control.
-   <span class="title-ref">relative\_index</span> tells you how far
    into a given custom effect block you are in as an index.
-   <span class="title-ref">absolute\_index</span> tells you how far
    into the entire text you are as an index.
-   <span class="title-ref">elapsed\_time</span> is the total amount of
    time the text effect has been running.
-   <span class="title-ref">visible</span> will tell you whether the
    character is visible or not and will also allow you to hide a given
    portion of text.
-   <span class="title-ref">offset</span> is an offset position relative
    to where the given character should render under normal
    circumstances.
-   <span class="title-ref">color</span> is the color of a given
    character.
-   Finally, <span class="title-ref">env</span> is a `class_Dictionary`
    of parameters assigned to a given custom effect. You can use
    `get() <class_Dictionary_method_get>` with an optional default value
    to retrieve each parameter, if specified by the user. For example
    <span class="title-ref">\[custom\_fx spread=0.5
    color=\#FFFF00\]test\[/custom\_fx\]</span> would have a float <span
    class="title-ref">spread</span> and Color <span
    class="title-ref">color</span> parameters in its \` \`env\`\`
    Dictionary. See below for more usage examples.

The last thing to note about this function is that it is necessary to
return a boolean <span class="title-ref">true</span> value to verify
that the effect processed correctly. This way, if there's a problem with
rendering a given character, it will back out of rendering custom
effects entirely until the user fixes whatever error cropped up in their
custom effect logic.

Here are some examples of custom effects:

Ghost \~\~\~\~\~

    tool
    extends RichTextEffect
    class_name RichTextGhost

    # Syntax: [ghost freq=5.0 span=10.0][/ghost]

    # Define the tag name.
    var bbcode = "ghost"

    func _process_custom_fx(char_fx):
        # Get parameters, or use the provided default value if missing.
        var speed = char_fx.env.get("freq", 5.0)
        var span = char_fx.env.get("span", 10.0)

        var alpha = sin(char_fx.elapsed_time * speed + (char_fx.absolute_index / span)) * 0.5 + 0.5
        char_fx.color.a = alpha
        return true

Pulse \~\~\~\~\~

    tool
    extends RichTextEffect
    class_name RichTextPulse

    # Syntax: [pulse color=#00FFAA height=0.0 freq=2.0][/pulse]

    # Define the tag name.
    var bbcode = "pulse"

    func _process_custom_fx(char_fx):
        # Get parameters, or use the provided default value if missing.
        var color = char_fx.env.get("color", char_fx.color)
        var height = char_fx.env.get("height", 0.0)
        var freq = char_fx.env.get("freq", 2.0)

        var sined_time = (sin(char_fx.elapsed_time * freq) + 1.0) / 2.0
        var y_off = sined_time * height
        color.a = 1.0
        char_fx.color = char_fx.color.linear_interpolate(color, sined_time)
        char_fx.offset = Vector2(0, -1) * y_off
        return true

Matrix \~\~\~\~\~\~

    tool
    extends RichTextEffect
    class_name RichTextMatrix

    # Syntax: [matrix clean=2.0 dirty=1.0 span=50][/matrix]

    # Define the tag name.
    var bbcode = "matrix"

    func _process_custom_fx(char_fx):
        # Get parameters, or use the provided default value if missing.
        var clear_time = char_fx.env.get("clean", 2.0)
        var dirty_time = char_fx.env.get("dirty", 1.0)
        var text_span = char_fx.env.get("span", 50)

        var value = char_fx.character

        var matrix_time = fmod(char_fx.elapsed_time + (char_fx.absolute_index / float(text_span)), \
                               clear_time + dirty_time)

        matrix_time = 0.0 if matrix_time < clear_time else \
                      (matrix_time - clear_time) / dirty_time

        if value >= 65 && value < 126 && matrix_time > 0.0:
            value -= 65
            value = value + int(1 * matrix_time * (126 - 65))
            value %= (126 - 65)
            value += 65
        char_fx.character = value
        return true

This will add a few new BBCode commands, which can be used like so:

    [center][ghost]This is a custom [matrix]effect[/matrix][/ghost] made in
    [pulse freq=5.0 height=2.0][pulse color=#00FFAA freq=2.0]GDScript[/pulse][/pulse].[/center]
