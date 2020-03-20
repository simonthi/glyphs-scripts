# adhesiontext Arabic Colored Layers (originally published by [Tosche](https://github.com/Tosche))

This is a repository for a Python script for the font editor [Glyphs](http://glyphsapp.com/).

At this point: all the honours to Toshi for creating the original version of this tool. It is an adhesiontext generator that is sensitive to positional Arabic forms.
»The script looks at your Glyphs file, and suggests only the words you have positional forms for. The word dictionary comes with the package and must be stored in the same place as the script. The dictionary can be used for other stuff too, of course.
The source dictionary file is big, so it takes a lot of time picking words from that. You can save time by shrinking the dictionary (this will be only done internally, not saved to the text file).«

Yet I wanted to train a little of python coding and one thing bothered me slightly about Toshi’s script: you can’t decide which characters to include if you have glyphs that you are not empty but that you don’t want to include in your testfile.
Here it comes in handy that you can colour charcters in Glyphs. Choose a colour and pick in the script menu if you want to take the colour for the decision making on which glyph to include in your adhesiontext into account. Tadaa: you now have full control over your text generation.

### Installation

1. Clone the repository using Terminal: git clone https://github.com/simonthi/Glyphs-scripts.git ~/Library/Application\ Support/Glyphs/Scripts/simonthi
2. Update your Scripts in Glyphs. (Alt+Click on Scripts --> Reload scripts)


### License

Copyright 2018 Toshi Omagari (@tosche_e).
Copyright 2020 Simon Thiefes (@simonthi).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
