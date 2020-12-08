"""Providers Configuration File."""
from masonite.logging.providers import LoggingProvider
from masonite.providers import AppProvider
from masonite.providers import AuthenticationProvider
from masonite.providers import BroadcastProvider
from masonite.providers import CacheProvider
from masonite.providers import CsrfProvider
from masonite.providers import HelpersProvider
from masonite.providers import MailProvider
from masonite.providers import QueueProvider
from masonite.providers import RouteProvider
from masonite.providers import SessionProvider
from masonite.providers import StatusCodeProvider
from masonite.providers import UploadProvider
from masonite.providers import ViewProvider
from masonite.providers import WhitenoiseProvider
from masonite.validation.providers import ValidationProvider
from masonite.validation.providers.ValidationProvider import ValidationProvider

"""Providers List
Providers are a simple way to remove or add functionality for Masonite
The providers in this list are either ran on server start or when a
request is made depending on the provider. Take some time to can
learn more more about Service Providers in our documentation
"""

PROVIDERS = [
    # Framework Providers
    AppProvider,
    AuthenticationProvider,
    SessionProvider,
    RouteProvider,
    StatusCodeProvider,
    WhitenoiseProvider,
    ViewProvider,
    # Optional Framework Providers
    MailProvider,
    UploadProvider,
    QueueProvider,
    CacheProvider,
    BroadcastProvider,
    CsrfProvider,
    HelpersProvider,
    ValidationProvider,
    # Third Party Providers
    LoggingProvider,
    ValidationProvider,
    # Application Providers
]
