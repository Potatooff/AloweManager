from src.auth.auth import AuthPage
from src.auth.database import only_oneTime
from src.Corelia.Program import _close_api


try:
    only_oneTime()

    AuthPage().run()

    
except KeyboardInterrupt:
    pass

finally:
    _close_api()
