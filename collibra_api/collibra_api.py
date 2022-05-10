import logging
from collibra_api.rest_adapter import RestAdapter
from collibra_api.models import Asset, AssetType


class CollibraApi:
    def __init__(self, hostname: str, username: str, password: str, version: str = '2.0', logger: logging.Logger = None) -> None:
        self._rest_adapter = RestAdapter(hostname=hostname, username=username, password=password, version=version, logger=logger)

    def get_assets(self, limit=10) -> list[Asset]:
        result = self._rest_adapter.get(endpoint='/assets', query_params={'limit': limit})
        return [Asset(**asset) for asset in result.results]

    def get_asset(self, assetId: str) -> Asset:
        result = self._rest_adapter.get(endpoint=f'/assets/{assetId}')
        return Asset(**result.results)

    def get_asset_types(self, limit=10) -> list[AssetType]:
        result = self._rest_adapter.get('/assetTypes', query_params={'limit': limit})
        return [AssetType(**asset_type) for asset_type in result.results]

    def get_asset_type(self, assetTypeId: str) -> Asset:
        result = self._rest_adapter.get(endpoint=f'/assetTypes/{assetTypeId}')
        return AssetType(**result.results)
