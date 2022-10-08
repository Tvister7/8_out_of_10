from asyncio import get_event_loop

from core.create_app import create_app as create_notification_app

if __name__ == "__main__":
    loop = get_event_loop()
    loop.run_until_complete(create_notification_app())
