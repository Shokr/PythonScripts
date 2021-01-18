"""A BlogController Module."""
from masonite.controllers import Controller
from masonite.request import Request
from masonite.view import View


class BlogController(Controller):
    """BlogController Controller Class."""

    def __init__(self, request: Request):
        """BlogController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return view.render("blog")
