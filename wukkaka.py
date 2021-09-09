import os
from glob import glob
import re

tiers = glob("team_cfg/*")

for tier in tiers:
    teams = glob(os.path.join(tier,'*'))
    for team in teams:
        team_name = team.split(os.sep)[-1]
        if team_name[0] == "_":
            continue

        fixed_text=""
        file= open(team,"r")
        for line in file:

            if '"76' in line:
                split_str = line.split('"')
                split_str[3]="WUKAKA"
                line='"'.join(split_str)
            fixed_text += line
        file.close()

        fout = open(team, "w")
        fout.write(fixed_text)
        fout.close()




