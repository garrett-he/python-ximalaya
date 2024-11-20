from typing import TypedDict


class AlbumInfo(TypedDict):
    albumId: int
    albumPlayCount: int
    albumTrackCount: int
    albumCoverPath: str
    albumTitle: str
    albumUserNickName: str
    anchorId: int
    anchorGrade: int
    mvpGrade: int
    isDeleted: bool
    isPaid: bool
    isFinished: int
    anchorUrl: str
    albumUrl: str
    intro: str
    vipType: int
    logoType: int
    subscriptInfo: dict[{'albumSubscriptValue': int, 'url': str}]
    albumSubscript: int


class FollowingInfo(TypedDict):
    uid: int
    coverPath: str
    anchorNickName: str
    background: str
    description: str
    url: str
    grade: int
    mvpGrade: int
    gradeType: int
    trackCount: int
    albumCount: int
    followerCount: int
    followingCount: int
    isFollow: bool
    beFollow: bool
    isBlack: bool
    logoType: int
