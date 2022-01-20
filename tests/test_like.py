from testest.like import LikeState, push_many


def test_pushes():
    assert push_many(LikeState.empty, 'l') is LikeState.liked
    assert push_many(LikeState.empty, 'dl') is LikeState.liked
    assert push_many(LikeState.empty, 'ddl') is LikeState.liked

    assert push_many(LikeState.empty, 'd') is LikeState.disliked
    assert push_many(LikeState.empty, 'ld') is LikeState.disliked

    assert push_many(LikeState.empty, '') is LikeState.empty
    assert push_many(LikeState.empty, 'll') is LikeState.empty
    assert push_many(LikeState.empty, 'ldd') is LikeState.empty
    assert push_many(LikeState.empty, 'lldd') is LikeState.empty
