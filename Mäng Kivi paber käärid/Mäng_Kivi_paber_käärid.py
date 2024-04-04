import random 
def mängija_valik():
    return input("Valige kivi, käärid või paber: ").lower().strip()  # Функция, которая предлагает игроку сделать выбор и всегда возвращает его строчными буквами и без пробелов.

def võitja_määramine(valik1, valik2):
    if valik1 == valik2:  # Если выборы игрока и бота совпадают, результат ничья.
        return "Viik"
    elif (valik1 == "kivi" and valik2 == "käärid") or \
         (valik1 == "käärid" and valik2 == "paber") or \
         (valik1 == "paber" and valik2 == "kivi"):
         return "Teie võidate"

    else:  # Если ни одно из условий не выполняется бот побеждает.
        return "Arvuti võidab"

def main():
    print("Tere tulemast mängu 'Kivi, käärid, paber'!")
    mängija_punktid = 0
    arvuti_punktid = 0
    vooru_number = 1

    while True:
        print(f"\nVoor {vooru_number}:")
        mängija_val = mängija_valik()
        arvuti_val = random.choice(["kivi", "käärid", "paber"])

        print(f"Teie valisite: {mängija_val}")
        print(f"Arvuti valis: {arvuti_val}")

        tulemus = võitja_määramine(mängija_val, arvuti_val)

        print(tulemus)

        if "Teie" in tulemus:
            mängija_punktid += 1
        elif "Arvuti" in tulemus:
            arvuti_punktid += 1

        print(f"Teie punktid: {mängija_punktid}")
        print(f"Arvuti punktid: {arvuti_punktid}")

        if input("Kas soovite jätkata? (jah/ei): ").lower() != "jah":
            break

        vooru_number += 1

    print("\nMäng lõppes!")
    print(f"Teie kogusite kokku {mängija_punktid} punkti.")
    print(f"Arvuti kogus kokku {arvuti_punktid} punkti.")

if __name__ == "__main__":
    main()
