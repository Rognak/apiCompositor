import asyncio

from clients.classes_api_client.client import Client as ClassesClient
from clients.classes_api_client.api.default import get_classes_classes_post
from clients.classes_api_client.models import ClassesFilter

from clients.ships_api_client.client import Client as ShipsClient
from clients.ships_api_client.api.default import get_ships_ships_post
from clients.ships_api_client.models import ShipsFilter

from clients.outcomes_api_client.client import Client as OutcomesClient
from clients.outcomes_api_client.api.default import get_outcomes_outcomes_post
from clients.outcomes_api_client.models import OutcomesFilter

from providers.battles_provider import get_battles
import pandas as pd


class BattleHistoryCompositor:

    def __init__(self,
                 classes_client: ClassesClient,
                 ships_client: ShipsClient,
                 outcomes_client: OutcomesClient,
                 ):

        self.classes_client = classes_client
        self.ships_client = ships_client
        self.outcomes_client = outcomes_client

    async def composite(self, db):
        classes = get_classes_classes_post.asyncio(client=self.classes_client, json_body=ClassesFilter.from_dict({}))
        ships = get_ships_ships_post.asyncio(client=self.ships_client, json_body=ShipsFilter.from_dict({}))
        outcomes = get_outcomes_outcomes_post.asyncio(client=self.outcomes_client, json_body=OutcomesFilter.from_dict({}))

        results = await asyncio.gather(*(classes, ships, outcomes))

        classes, ships, outcomes = results

        classes_df = pd.DataFrame(data=[c.to_dict() for c in classes])
        ships_df = pd.DataFrame(data=[s.to_dict() for s in ships])
        outcomes_df = pd.DataFrame(data=[o.to_dict() for o in outcomes])

        t = outcomes_df[~outcomes_df.ship.isin(ships_df["name"])]
        t['cls'] = t.ship
        t = t.rename(columns={"ship": "name"})

        t = t[['cls', 'name']]

        merged = pd.merge(classes_df, ships_df, on=['cls'])
        merged = merged[['cls', 'name']]

        x = pd.concat([merged, t])
        all_ships = x.drop_duplicates()
        all_ships = all_ships.rename(columns={"name": "ship"})

        ships_total = pd.merge(all_ships, outcomes_df, how='left', on=['ship'])
        ships_total = ships_total[['ship', 'battle', 'result']]
        ships_total = ships_total[~ships_total.result.isin(['sunk'])]

        result = ships_total.groupby(['ship']).count()
        result = result[['battle']]

        return result.to_dict()
