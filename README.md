foundation_images
=================

A simple Pelican plugin for inserting captioned images into my foundation-default-colours theme which you can download from https://github.com/FuzzyWuzzie/foundation-default-colours.

It provides a macro in posts to easily insert the following chunk of html:

```html
<div class="row image-container">
	<div class="large-12 columns text-center">
		<div class="row">
			<div class="large-12 columns text-center image-image">
				<img src="YOUR IMAGE SOURCE HERE"/>
			</div>
		</div>
		<div class="row image-caption">
			YOUR IMAGE CAPTION HERE
		</div>
	</div>
</div>
```

using the following shorthand:

```
{image-caption[YOUR IMAGE SOURCE HERE][YOUR IMAGE CAPTION HERE]}
```
