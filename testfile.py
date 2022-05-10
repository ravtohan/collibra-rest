from collibra_api.collibra_api import CollibraApi
from os import environ

collibra = CollibraApi(hostname=environ.get('COLLIBRA_DGC_HOSTNAME'),
                       username=environ.get('COLLIBRA_USERNAME'),
                       password=environ.get('COLLIBRA_PASSWORD'))
# assets = collibra.get_assets()
# a = collibra.get_asset(assetId='2b1fd126-7064-454b-b815-287107552f3d')
# assetTypes = collibra.get_asset_types()
assetType = collibra.get_asset_type(assetTypeId='00000000-0000-0000-0000-000000011003')
