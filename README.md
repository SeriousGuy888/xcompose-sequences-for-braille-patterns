# xcompose sequences for characters in the Braille Patterns unicode block

These XCompose sequences allow for typing the 8-dot braille patterns in the [Braille Patterns Block](https://en.wikipedia.org/wiki/Braille_Patterns#Block) (U+2800..U+28FF).

Each compose sequence looks like `<Multi_key> <B> (dots) <space>`,
where `(dots)` is a sequence of the keys
<kbd>1</kbd>,
<kbd>2</kbd>,
<kbd>q</kbd>,
<kbd>w</kbd>,
<kbd>a</kbd>,
<kbd>s</kbd>,
<kbd>z</kbd>,
<kbd>x</kbd>
on a QWERTY keyboard, left to right and then top to bottom.
Each key's presence in the compose sequence indicates that the corresponding dot is raised.

For example,
`⠏` has the compose sequence `<Multi_key> <B> <1> <2> <q> <a> <space>`.

