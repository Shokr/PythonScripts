from pixellib.tune_bg import alter_bg

change_bg = alter_bg()
print(change_bg)

change_bg.load_pascalvoc_model(
    "deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
print("-=-=-")
change_bg.change_bg_img(
    f_image_path="img/sample.jpg",
    b_image_path="img/background.jpg",
    output_image_name="img/new_img.jpg",
)
print("opopop")
