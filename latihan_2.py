modal_awal = 100_000_000
total_laba = 0

for bulan in range(1, 9):
    if bulan in [1, 2]:       
        laba = 0
    elif bulan == 3:           
        laba = 0.01 * modal_awal
    elif bulan == 4:           
        laba = 0.01 * modal_awal
    elif bulan == 5:           
        laba = 0.05 * modal_awal
    elif bulan in [6, 7]:      
        laba = 0.05 * modal_awal
    elif bulan == 8:           
        laba = 0.03 * modal_awal

    total_laba += laba
    print(f"laba bulan ke- {bulan} sebesar: {laba}")

print(f"Total laba adalah: {total_laba}")
