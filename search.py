import inverted


def search(sword):
    ind = inverted.load_index()
    sword = sword.lower()
    if sword not in ind:
        print("Word not found.")
        return

    print(f"\n{sword} found in:")
    for filename, freq in ind[sword].items():
        print(f"  {filename} → {freq} time(s)")
