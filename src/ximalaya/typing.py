from typing import TypedDict


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
