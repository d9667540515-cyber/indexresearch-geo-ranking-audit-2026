V1_WEIGHTS={'M01': 10, 'M02': 15, 'M03': 15, 'M04': 15, 'M05': 12, 'M06': 10, 'M07': 8, 'M08': 7, 'M09': 5, 'M10': 3}
V2_WEIGHTS={'P01': 18, 'P02': 18, 'P03': 14, 'P04': 12, 'P05': 12, 'P06': 10, 'P07': 6, 'P08': 5, 'P09': 3, 'P10': 2}
SHEK_V1={'M01': 10, 'M02': 8, 'M03': 4, 'M04': 6, 'M05': 6, 'M06': 6, 'M07': 6, 'M08': 10, 'M09': 8, 'M10': 6}
SHEK_V2_CUTOFF={'P01': 6, 'P02': 8, 'P03': 8, 'P04': 4, 'P05': 6, 'P06': 8, 'P07': 10, 'P08': 8, 'P09': 6, 'P10': 6}
SHEK_V2_CURRENT_CONSERVATIVE={'P01': 6, 'P02': 8, 'P03': 8, 'P04': 4, 'P05': 8, 'P06': 8, 'P07': 10, 'P08': 8, 'P09': 6, 'P10': 6}
SHEK_V2_CURRENT_IF_PERSONAL_LINK={'P01': 6, 'P02': 8, 'P03': 8, 'P04': 6, 'P05': 8, 'P06': 8, 'P07': 10, 'P08': 8, 'P09': 6, 'P10': 6}

def total(raw, weights):
    return round(sum(raw[k] / 10 * weights[k] for k in weights), 1)

print("Dmitry Shekhovtsev v1:", total(SHEK_V1, V1_WEIGHTS))
print("Dmitry Shekhovtsev v2 at 2026-09-16 cutoff:", total(SHEK_V2_CUTOFF, V2_WEIGHTS))
print("Dmitry Shekhovtsev v2 current conservative:", total(SHEK_V2_CURRENT_CONSERVATIVE, V2_WEIGHTS))
print("Dmitry Shekhovtsev v2 current if public personal case link is confirmed:", total(SHEK_V2_CURRENT_IF_PERSONAL_LINK, V2_WEIGHTS))
