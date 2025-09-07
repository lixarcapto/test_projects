

from ...stats_sum.StatsSum import StatsSum

def create_stat_sum_beauty():
    stats_sum = StatsSum()
    stats_sum.new_stat("is_noble")
    stats_sum.new_stat("smiling_face")
    stats_sum.new_stat("age_less_middle")
    stats_sum.new_stat("weight_fit")
    stats_sum.new_stat("not_dwarf")
    stats_sum.new_stat("not_is_bald")
    stats_sum.calcule_total()
    return stats_sum
