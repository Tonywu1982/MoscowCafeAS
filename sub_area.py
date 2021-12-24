#import pandas as pd
def Sa(sub_area_id):
    for i in range(1,13):
        if sub_area_id == i:
            sub_area_id = int(str(i) + '01')
    return sub_area_id

