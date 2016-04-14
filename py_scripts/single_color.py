#!/bin/env python3
# coding=utf-8
# Filename    : testpillow.py
# Date        : 2016-02-18 13:54:18
# Author      : statby
# Description : v1 每次出一个颜色


import colorsys
from PIL import Image

def get_single_color():
    img = Image.open('kuai.jpg')  
    image = img.convert('RGBA')
    max_score = 0
    single_color = None
     
    for count, (r, g, b, a) in image.getcolors(img.size[0] * img.size[1]):
        # 跳过纯黑色
        if a == 0:
            continue
         
        saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]
        y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)
        y = (y - 16.0) / (235 - 16)

        # 忽略高亮色
        if y > 0.9:
            continue
         
        # Calculate the score, preferring highly saturated colors.
        # Add 0.1 to the saturation so we don't completely ignore grayscale
        # colors by multiplying the count by zero, but still give them a low
        # weight.
        score = (saturation + 0.1) * count
         
#        print ('score={},max_score={}'.format(score,max_score))
        if int(score) > max_score:
            max_score = score
            single_color = (r, g, b)
    return (single_color)
 


colors = {'mistyrose': '255,228,225', 'purple': '128,0,128', 'mediumturquoise': '72,209,204', 'bisque': '255,228,196', 'mediumorchid': '186,85,211', 'ghostwhite': '248,248,255', 'mediumpurple': '147,112,219', 'darkorange': '255,140,0', 'mediumvioletred': '199,21,133', 'whitesmoke': '245,245,245', 'honeydew': '240,255,240', 'darkkhaki': '189,183,107', 'oldlace': '253,245,230', 'maroon': '128,0,0', 'midnightblue': '25,25,112', 'yellow': '255,255,0', 'olive': '128,128,0', 'goldenrod': '218,165,32', 'aqua': '0,255,255', 'deepskyblue': '0,191,255', 'crimson': '220,20,60', 'tomato': '255,99,71', 'cornflowerblue': '100,149,237', 'cornsilk': '255,248,220', 'paleturquoise': '175,238,238', 'darkcyan': '0,139,139', 'lavenderblush': '255,240,245', 'coral': '255,127,80', 'silver': '192,192,192', 'chocolate': '210,105,30', 'lime': '0,255,0', 'thistle': '216,191,216', 'firebrick': '178,34,34', 'darkslategray': '47,79,79', 'steelblue': '70,130,180', 'lawngreen': '124,252,0', 'blue': '0,0,255', 'lightslategray': '119,136,153', 'darkgoldenrod': '184,134,11', 'seashell': '255,245,238', 'seagreen': '46,139,87', 'lightblue': '173,216,230', 'gold': '255,215,0', 'ivory': '255,255,240', 'plum': '221,160,221', 'darkturquoise': '0,206,209', 'navajowhite': '255,222,173', 'papayawhip': '255,239,213', 'skyblue': '135,206,235', 'dodgerblue': '30,144,255', 'lightsteelblue': '176,196,222', 'olivedrab': '107,142,35', 'lightgoldenrodyellow': '250,250,210', 'darkblue': '0,0,139', 'beige': '245,245,220', 'wheat': '245,222,179', 'magenta': '255,0,255', 'darkgray': '169,169,169', 'navy': '0,0,128', 'orangered': '255,69,0', 'rosybrown': '188,143,143', 'lemonchiffon': '255,250,205', 'palegreen': '152,251,152', 'chartreuse': '127,255,0', 'royalblue': '65,105,225', 'aquamarine': '127,255,212', 'limegreen': '50,205,50', 'white': '255,255,255', 'darkmagenta': '139,0,139', 'slateblue': '106,90,205', 'khaki': '240,230,140', 'mediumslateblue': '123,104,238', 'lightskyblue': '135,206,250', 'lightgreen': '144,238,144', 'palevioletred': '219,112,147', 'brown': '165,42,42', 'tan': '210,180,140', 'mediumspringgreen': '0,250,154', 'palegoldenrod': '238,232,170', 'darkolivegreen': '85,107,47', 'darkseagreen': '143,188,143', 'teal': '0,128,128', 'cyan': '0,255,255', 'mediumblue': '0,0,205', 'azure': '240,255,255', 'fuchsia': '255,0,255', 'lightcoral': '240,128,128', 'greenyellow': '173,255,47', 'blueviolet': '138,43,226', 'slategray': '112,128,144', 'antiquewhite': '250,235,215', 'darkviolet': '148,0,211', 'forestgreen': '34,139,34', 'gainsboro': '220,220,220', 'powderblue': '176,224,230', 'lavender': '230,230,250', 'lightseagreen': '32,178,170', 'mediumaquamarine': '102,205,170', 'turquoise': '64,224,208', 'mintcream': '245,255,250', 'black': '0,0,0', 'pink': '255,192,203', 'burlywood': '222,184,135', 'lightyellow': '255,255,224', 'chocolatesaddlebrown': '192,14,235', 'linen': '250,240,230', 'springgreen': '0,255,127', 'sienna': '160,82,45', 'mediumseagreen': '60,179,113', 'lightcyan': '224,255,255', 'darkred': '139,0,0', 'hotpink': '255,105,180', 'moccasin': '255,228,181', 'salmon': '250,128,114', 'sandybrown': '244,164,96', 'cadetblue': '95,158,160', 'lightgrey': '211,211,211', 'red': '255,0,0', 'dimgray': '105,105,105', 'orange': '255,165,0', 'floralwhite': '255,250,240', 'yellowgreen': '154,205,50', 'orchid': '218,112,214', 'snow': '255,250,250', 'indianred': '205,92,92', 'aliceblue': '240,248,255', 'violet': '238,130,238', 'blanchedalmond': '255,235,205', 'darkslateblue': '72,61,139', 'indigo': '75,0,130', 'lightsalmon': '255,160,122', 'peru': '205,133,63'}


new_colors = {'221,160,221': 'plum', '165,42,42': 'brown', '72,61,139': 'darkslateblue', '250,240,230': 'linen', '220,20,60': 'crimson', '127,255,0': 'chartreuse', '148,0,211': 'darkviolet', '124,252,0': 'lawngreen', '0,0,128': 'navy', '72,209,204': 'mediumturquoise', '95,158,160': 'cadetblue', '128,0,128': 'purple', '255,0,0': 'red', '139,0,0': 'darkred', '176,224,230': 'powderblue', '210,180,140': 'tan', '169,169,169': 'darkgray', '222,184,135': 'burlywood', '205,133,63': 'peru', '240,128,128': 'lightcoral', '128,128,0': 'olive', '65,105,225': 'royalblue', '220,220,220': 'gainsboro', '192,14,235': 'chocolatesaddlebrown', '240,255,255': 'azure', '176,196,222': 'lightsteelblue', '230,230,250': 'lavender', '139,0,139': 'darkmagenta', '154,205,50': 'yellowgreen', '250,128,114': 'salmon', '255,255,0': 'yellow', '138,43,226': 'blueviolet', '64,224,208': 'turquoise', '244,164,96': 'sandybrown', '253,245,230': 'oldlace', '255,245,238': 'seashell', '173,216,230': 'lightblue', '75,0,130': 'indigo', '0,255,127': 'springgreen', '85,107,47': 'darkolivegreen', '102,205,170': 'mediumaquamarine', '255,160,122': 'lightsalmon', '60,179,113': 'mediumseagreen', '255,192,203': 'pink', '0,0,0': 'black', '147,112,219': 'mediumpurple', '255,255,240': 'ivory', '255,250,205': 'lemonchiffon', '105,105,105': 'dimgray', '255,0,255': 'magenta', '0,206,209': 'darkturquoise', '240,255,240': 'honeydew', '218,112,214': 'orchid', '210,105,30': 'chocolate', '255,228,196': 'bisque', '32,178,170': 'lightseagreen', '106,90,205': 'slateblue', '0,255,255': 'cyan', '25,25,112': 'midnightblue', '238,232,170': 'palegoldenrod', '192,192,192': 'silver', '189,183,107': 'darkkhaki', '240,230,140': 'khaki', '255,105,180': 'hotpink', '248,248,255': 'ghostwhite', '186,85,211': 'mediumorchid', '255,127,80': 'coral', '0,128,128': 'teal', '250,250,210': 'lightgoldenrodyellow', '255,165,0': 'orange', '255,99,71': 'tomato', '255,255,224': 'lightyellow', '250,235,215': 'antiquewhite', '255,140,0': 'darkorange', '255,250,240': 'floralwhite', '255,250,250': 'snow', '255,248,220': 'cornsilk', '0,0,205': 'mediumblue', '178,34,34': 'firebrick', '30,144,255': 'dodgerblue', '255,235,205': 'blanchedalmond', '245,222,179': 'wheat', '238,130,238': 'violet', '255,255,255': 'white', '50,205,50': 'limegreen', '0,191,255': 'deepskyblue', '199,21,133': 'mediumvioletred', '255,240,245': 'lavenderblush', '160,82,45': 'sienna', '119,136,153': 'lightslategray', '112,128,144': 'slategray', '0,0,139': 'darkblue', '255,222,173': 'navajowhite', '0,0,255': 'blue', '70,130,180': 'steelblue', '255,215,0': 'gold', '245,245,245': 'whitesmoke', '188,143,143': 'rosybrown', '255,228,181': 'moccasin', '184,134,11': 'darkgoldenrod', '218,165,32': 'goldenrod', '100,149,237': 'cornflowerblue', '205,92,92': 'indianred', '128,0,0': 'maroon', '107,142,35': 'olivedrab', '135,206,235': 'skyblue', '34,139,34': 'forestgreen', '245,255,250': 'mintcream', '144,238,144': 'lightgreen', '240,248,255': 'aliceblue', '0,255,0': 'lime', '255,228,225': 'mistyrose', '175,238,238': 'paleturquoise', '245,245,220': 'beige', '152,251,152': 'palegreen', '219,112,147': 'palevioletred', '46,139,87': 'seagreen', '47,79,79': 'darkslategray', '0,139,139': 'darkcyan', '255,239,213': 'papayawhip', '135,206,250': 'lightskyblue', '216,191,216': 'thistle', '143,188,143': 'darkseagreen', '224,255,255': 'lightcyan', '173,255,47': 'greenyellow', '127,255,212': 'aquamarine', '211,211,211': 'lightgrey', '255,69,0': 'orangered', '123,104,238': 'mediumslateblue', '0,250,154': 'mediumspringgreen'}

abs_color = {}
result = {}
def diff_color():
    for color_rgb,key in new_colors.items():
        color_rgb=color_rgb.split(',')
        abs_color[key] = sum(map(abs,(get_single_color()[0] - int(color_rgb[0]),get_single_color()[1] - int(color_rgb[1]),get_single_color()[2] - int(color_rgb[2]))))
    result[get_single_color()] = min(abs_color.items(),key=lambda x:x[1])[0]
    return (result)


if __name__ = '__main__':
    print (diff_color())
