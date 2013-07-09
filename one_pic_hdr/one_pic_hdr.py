#!/usr/bin/env python

from gimpfu import *


def one_pic_hdr(img, drw):
    "In gimp Help -> Procedure Browser"
    img.disable_undo()

    layer_soft_light = drw.copy(True)
    layer_soft_light.mode = SOFTLIGHT_MODE
    layer_soft_light.name = "Soft light"
    img.add_layer(layer_soft_light, -1)

    pdb.gimp_desaturate_full(layer_soft_light, DESATURATE_LUMINOSITY)
    pdb.gimp_invert(layer_soft_light)
    pdb.plug_in_gauss(img, layer_soft_light, 300, 300, 1)

    layer_soft_light_50_copy = layer_soft_light.copy(True)
    layer_soft_light_50_copy.name = "50 % copy"
    img.add_layer(layer_soft_light_50_copy, -2)
    pdb.gimp_layer_set_opacity(layer_soft_light_50_copy, 50)

    layer_hard_light = pdb.gimp_layer_new_from_visible(img, img, "Hard light")
    layer_hard_light.mode = HARDLIGHT_MODE
    layer_hard_light.name = "Hard light"
    img.add_layer(layer_hard_light, -3)
    pdb.gimp_context_set_foreground((0, 0, 0))
    pdb.gimp_context_set_background((255, 255, 255))
    pdb.plug_in_gradmap(img, layer_hard_light)
    pdb.gimp_layer_set_opacity(layer_hard_light, 25)

    img.enable_undo()
    pdb.gimp_displays_flush

register(
    "my_hdr",  # Name
    "Creates HDR from one picture",  # Description
    "Sometimes it is not possible to make 3 pictures",  # HowTo
    "Michal Lorenc <m.t.lorenc@wp.pl>",
    "GPL",
    "2013",
    "<Image>/Filters/Enhance/One pic HDR",
    "RGB*, GRAY*",
    [],
    [],
    one_pic_hdr)

main()
