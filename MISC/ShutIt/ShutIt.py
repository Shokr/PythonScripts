# ShutIt is an shell automation framework designed to be easy to use.
import shutit

session = shutit.create_session("bash")
session.send("echo Hello World", echo=True)
