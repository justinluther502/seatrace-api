from trueskill import Rating, TrueSkill
from typing import Tuple
from athletes.models import Rower


def race_update(winner: Tuple[Rating], loser: Tuple[Rating]) -> (
        Tuple[Rating], Tuple[Rating]):
    """
    Updates MMR for athletes in both teams. Teams are lists of Rating instances.

    No update occurs if draw = True.

    :param winner: Tuple of winning athletes.
    :param loser: Tuple of losing athletes.
    :param draw: bool, True if match was a draw.
    :return: Tuple of 2 Lists of ratings instances in the same order as the
    input teams.
    """

    env = TrueSkill(draw_probability=0.01)
    new_winner_tuple, new_loser_tuple = env.rate([winner, loser])
    return new_winner_tuple, new_loser_tuple


def save_mmr(rower_keys: Tuple[int], new_ratings: Tuple[Rating]) -> None:
    """
    Updates a set of Rower instances with new MMRs after a recorded race.

    Does not return anything. Instances are updated via their save() method.

    :param rower_keys: Tuple of int primary keys to identify Rower models.
    :param new_ratings: Tuple of new Ratings.
    """
    for idx, rower_key in enumerate(rower_keys):
        rower_model = Rower.objects.get(id=rower_key)
        rower_model.mmr = new_ratings[idx].mu
        rower_model.mmr_uncertainty = new_ratings[idx].sigma
        rower_model.save()
