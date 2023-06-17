# Sort-images-by-literal-Aspect-Ratio


## External dependencies: ImageMagick

Sort any amount of images into folders by literal aspect ratio. For filtering large quantities of scraped images, specifically for datasetting. Across physical drives etc.

There's some irrelevant imports, like PIL, that I'm too lazy to remove. 


* image_dir = folder with images.
* output_dir = folder where the images will be moved and the aspect ratio folders will be created.

Useful for datasetting Stablediffusion embeddings or models, without having to mess with resizing. Reduces preprocessing time, depending on workflow. Can easily be configured into dimensions to reduce folders generated, like Portrait, Landscape & Square. Or arbitrary aspect ratio ranges as well, if you want to group 4:3, 16:9 and 16:10 together as an example.

![](https://github.com/bucketcat/Sort-images-by-literal-Aspect-Ratio/blob/main/Resulting_Folder_Structure_example.png)()

