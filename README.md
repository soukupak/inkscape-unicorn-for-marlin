Marlin G-Code Output for Inkscape
===========================================

Notice
------
**Now works with Inkscape >= 1.0!**
**There is also version for older Inkscape, check releases.**

**I tested it with version Inkscape 0.92 with document units set to mm and it seems to work, no other configuration is tested**

**Please feel free to fork and improve this extension for your own needs!**

This is an Inkscape extension that allows you to save your Inkscape drawings as
G-Code files suitable for plotting with any Marlin based plotter.

**Users who use this extension to generate G-Code for a their machine do so at their own risk.**

Original Author: [Marty McGuire](http://github.com/martymcguire)

Website: [http://github.com/martymcguire/inkscape-unicorn](http://github.com/martymcguire/inkscape-unicorn)

Credits
=======

* Marty McGuire pulled this all together into an Inkscape extension.
* Ondrej Soukup made modification to the script to make it work with Marlin firmware and new inkscape
* [Inkscape](http://www.inkscape.org/) is an awesome open source vector graphics app.
* [Scribbles](https://github.com/makerbot/Makerbot/tree/master/Unicorn/Scribbles%20Scripts) is the original DXF-to-Unicorn Python script.
* [The Egg-Bot Driver for Inkscape](http://code.google.com/p/eggbotcode/) provided inspiration and good examples for working with Inkscape's extensions API.

Install
=======

Copy the contents of `src/` to your Inkscape `extensions/` folder.

Typical locations include:

* OS X - `/Applications/Inkscape.app/Contents/Resources/extensions`
* Linux - `/usr/share/inkscape/extensions`
* Windows - `C:\Program Files\Inkscape\share\extensions` or better `C:\Users\[your_user_name]\AppData\Roaming\inkscape\extensions`

Usage
=====

* Size and locate your image appropriately:
	* Setting units to **mm** in Inkscape makes it easy to size your drawing.
* Convert all text to paths:
	* Select all text objects.
	* Choose **Path | Object to Path**.
* Save as G-Code:
	* **File | Save a Copy**.
	* Select **Marlin G-Code (\*.gcode)**.
	* Save your file.
* Preview
	* Simple web viewer: [GCode Viewer](http://jherrm.com/gcode-viewer/)
* Print!
