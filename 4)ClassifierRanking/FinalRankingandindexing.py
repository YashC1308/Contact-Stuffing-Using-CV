from PIL import Image, ImageFont, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
# Unicode ranges for emojis
'''
unicode_ranges = [
    (0x1F300, 0x1F64F),
    (0x1F680, 0x1F6FF),
    (0x1F910, 0x1F96B),
    (0x1F980, 0x1F9E0)
]
'''
#Unicode_0000FFEF
emoji_unicode = chr(0x00FFEF)
image_size = (28, 28)
image_Faulty = Image.new("RGBA", image_size, (0, 0, 0))
font = ImageFont.truetype("//content//drive//MyDrive//", 28, encoding='unic')
draw = ImageDraw.Draw(image_Faulty)
text_width, text_height = draw.textsize(emoji_unicode, font=font)
text_x = (image_size[0] - text_width) // 2
text_y = (image_size[1] - text_height) // 2
draw.text((text_x, text_y), emoji_unicode, (255, 255, 255), font=font)

image_Faulty = np.asarray(image_Faulty)

Unrendered_Unicode =[]

unicode_ranges = [
    (0x000000, 0x00FFFF),
    (0x010000, 0x01FBFF)
]
flag = False
count = 0
for start, end in unicode_ranges:
    for unicode_value in range(start, end + 1):
        # Convert the Unicode value to the emoji character
        emoji_unicode = chr(unicode_value)

        # Create a new image with white background
        image_size = (28, 28)
        image = Image.new("RGBA", image_size, (0, 0, 0))

        # Load the font
        font = ImageFont.truetype("D:\Google\GNUUnifont9FullHintInstrUCSUR.ttf", 28, encoding='unic')

        # Get a drawing context on the image
        draw = ImageDraw.Draw(image)

        # Calculate text size and position to center the emoji
        text_width, text_height = draw.textsize(emoji_unicode, font=font)
        text_x = (image_size[0] - text_width) // 2
        text_y = (image_size[1] - text_height) // 2

        # Draw the emoji on the image
        draw.text((text_x, text_y), emoji_unicode, (255, 255, 255), font=font)
        count+=1

        # Save the rendered emoji as an image
        #filename = f"emoji_{unicode_value:08X}.png"

        '''
        if(unicode_value in  range(0x000000, 0x00FFEF)):
            filename = "/content/drive/MyDrive/Images/" + f"Unicode_{unicode_value:08X}.png"

        else:
            filename = "/content/drive/MyDrive/Images2/" + f"Unicode_{unicode_value:08X}.png"
        '''

        if(np.array_equal(np.asarray(image), image_Faulty)):
          Unrendered_Unicode.append(filename)
        else:
          image.save(filename, dpi=(300, 300))

        print("Cycled : ",filename)


