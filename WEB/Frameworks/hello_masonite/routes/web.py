"""Web Routes."""
from masonite.routes import Get
from masonite.routes import Post

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    # Blog Routes
    Get("/blog", "BlogController@show"),
]
