import enum


class LikeState(enum.Enum):
    empty = enum.auto()
    liked = enum.auto()
    disliked = enum.auto()


like_transitions = {
        LikeState.empty: LikeState.liked,
        LikeState.liked: LikeState.empty,
        LikeState.disliked: LikeState.liked,
        }

dislike_transitions = {
        LikeState.empty: LikeState.disliked,
        LikeState.liked: LikeState.disliked,
        LikeState.disliked: LikeState.empty,
        }


def push_like(s: LikeState) -> LikeState:
    return like_transitions[s]


def push_dislike(s: LikeState) -> LikeState:
    return dislike_transitions[s]


def push_many(s: LikeState, pushes: str) -> LikeState:
    for c in pushes:
        c = c.lower()
        if c == 'l':
            s = push_like(s)
        elif c == 'd':
            s = push_dislike(s)
        else:
            raise ValueError('Invalid push')
    return s
