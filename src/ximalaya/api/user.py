from ximalaya.client import XimalayaClient, ResponsePaginator
from ximalaya.typing import FollowingInfo


def api_user_following(client: XimalayaClient, uid: int, page_size: int = 50) -> ResponsePaginator[FollowingInfo]:
    client.host = 'www.ximalaya.com'

    return ResponsePaginator(
        client,
        url_path=f'/revision/user/following?uid={uid}&pageSize={page_size}&keyWord=',
        data_path='data.followingsPageInfo'
    )
