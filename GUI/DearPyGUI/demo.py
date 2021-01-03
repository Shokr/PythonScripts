# https://medium.com/datadriveninvestor/create-quick-and-powerful-guis-using-dear-pygui-in-python-713cc138bf5a#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImQ0Y2JhMjVlNTYzNjYwYTkwMDlkODIwYTFjMDIwMjIwNzA1NzRlODIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2MDc2MDMyMzYsImF1ZCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjEwNTI1Njg2MDc3MzA0MzI2NDEwNiIsImVtYWlsIjoibW9oYW1tZWRzaG9rcjIwMTRAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF6cCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsIm5hbWUiOiJNdWhhbW1lZCBTaG9rciIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQU9oMTRHZ3Q2YmFqNnNkZEpBVExmMXhaV0wtTlNZN0I1ZDVxekpNbk1DV0otZz1zOTYtYyIsImdpdmVuX25hbWUiOiJNdWhhbW1lZCIsImZhbWlseV9uYW1lIjoiU2hva3IiLCJpYXQiOjE2MDc2MDM1MzYsImV4cCI6MTYwNzYwNzEzNiwianRpIjoiMmFjMzcyYTU4MzYyZjY3OWFjNmQyZGRiMDcwYzc4ZmI2NTA2ODQ0NyJ9.mLB0NsPWfLA3e3T9vyrRXXwLxMea0hBmCNwrpE7KcFJRvZwlZ1quGP6Ft-b_WgkHZiuBDpARKW40S7wEDneb0RrqPUqslNmmRmmZuqMvhFfDt89sKUA0IjtI03m4DyszOcJl45Jb29S-FsGXeGtvW4OUzQ3TbFk4W3cwwYU2Ah712I08j5W58MspgHjJJuHYf2NlSmXgymHh4atyDoo3lPUTSz8ivUbd_Rhhig9prVZruSCSNNG8beonLXwbV6lYuGDG8U-vbTslSfJMK4Dwm6WOHyn6S2r_sQI4CpYKaxoOwSYv91lW9SfMN0pCdNn7oGW23WKNbLQOGt4zmcMM8g

# # Usage

# from dearpygui.core import *
# from dearpygui.simple import show_about, show_documentation
#
# set_main_window_size(800, 800)
# show_about()
# show_documentation()
#
# # when running this code please look at the about window and it will report which version of Dear PyGUI is running
# # Even if you just did a pip install please ensure you your environment is using the latest package
# start_dearpygui()


# # Developer Tools
#
# from dearpygui.core import *
# from dearpygui.simple import show_documentation, show_debug, show_about, show_metrics
#
# show_documentation()
# show_debug()
# show_about()
# show_metrics()
# show_logger()
#
# start_dearpygui()


# # Built-in Logging
#
# from dearpygui.core import *
#
# show_logger()
# set_log_level(mvTRACE)
# log("trace message")
# log_debug("debug message")
# log_info("info message")
# log_warning("warning message")
# log_error("error message")
#
# start_dearpygui()


# # Creating Widgets and Containers
#
# from dearpygui.core import *
#
# add_button("Apply")
# add_same_line(spacing=10)
# add_button("Apply##1")
# add_same_line(spacing=10, name="sameline1")
# add_button("Apply2", label="Apply")
# add_spacing(count=5, name="spacing1")
# add_button("Apply##3")
#
# start_dearpygui()
