from models import *
from repository import *

if __name__ == '__main__':
    event_repos = EventRepository()
    person_repos = PersonRepository()
    pos_emo_repos = PositiveEmotionsRepository()
    pos_th_repos = PositiveThoughtRepository()
    neg_emo_repos = NegativeEmotionsRepository()
    neg_th_repos = NegativeThoughtRepository()
    calm_repos = CalmingTechniqueRepository()

    event_repos.save_item(Event(
        name='event',
        date='12.11.2023',
        negative_emotions=[NegativeEmotions(name='sad', strength=9, emoji=':(')]
    ))

    print(event_repos.get_item(0))
