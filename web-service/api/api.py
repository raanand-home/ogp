import logging
from dal import Stories
import tasks


def health():
    return "OK"


def request_story(url):
    story = Stories.get_by(url=url)
    if story is None:
        story = Stories(url=url)
        story.save()
    logging.error(tasks.scrap_task.delay(url))
    return dict(id=story.id)


def query_story(id):
    story = Stories.get_by(id=int(id))
    logging.error(story)
    story = story[0] if len(story) > 0 else None
    if story is None:
        return "Not Found", 404
    returns = {
        "url": story.url,
        "updated_time": story.updated_time,
        "scrape_status": story.status,
        "id": story.id
    }
    if story.status == 'done':
        returns.update(story.data)
    return returns
