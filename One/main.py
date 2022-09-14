from Modules.CleanData import get_data as g_d
from pathlib import Path

a = g_d('09-14-2022')

a.to_csv(Path('./Output/2.csv'))