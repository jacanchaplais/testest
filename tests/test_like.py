import pytest

from testest.like import LikeState, push_many


@pytest.mark.parametrize("test_input,expected", [
    ('ll', LikeState.empty),
    ('dd', LikeState.empty),
    ('ld', LikeState.disliked),
    ('dl', LikeState.liked),
    ('ldd', LikeState.empty),
    ('lldd', LikeState.empty),
    ('ddl', LikeState.liked),
    ])
def test_multi_pushes(test_input, expected):
    assert push_many(LikeState.empty, test_input)


def test_invalid_push():
    with pytest.raises(ValueError):
        push_many(LikeState.empty, 'x')


# def test_empty_push():
#     assert push_many(LikeState.empty, '') is LikeState.empty


# def test_single_push():
#     assert push_many(LikeState.empty, 'l') is LikeState.liked
#     assert push_many(LikeState.empty, 'd') is LikeState.disliked


# def test_many_pushes():
#     assert push_many(LikeState.empty, 'dl') is LikeState.liked
#     assert push_many(LikeState.empty, 'ddl') is LikeState.liked
#     assert push_many(LikeState.empty, 'ld') is LikeState.disliked
#     assert push_many(LikeState.empty, 'll') is LikeState.empty
#     assert push_many(LikeState.empty, 'ldd') is LikeState.empty
#     assert push_many(LikeState.empty, 'lldd') is LikeState.empty
