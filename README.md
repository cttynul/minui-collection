# MinUI Collection

This Python script is designed to **automatically generate custom collection files** (`.txt`) for the **MinUI** frontend, commonly used on some handhelds.

It searches the `Roms` folder on your SD card for files that match specific search parameters and excludes others based on your input, creating a clean list of ROMs for your custom collection.

## 🚀 Run

1.  **Save the Code:** Save the provided Python code into a file named, for example, `minui.py`.
2.  **Open Terminal/Command Prompt:** Navigate to the directory where you saved the file.
3.  **Execute:** Run the script using the Python interpreter:

    ```bash
    python minui.py
    ```

## 🛠️ Usage

The script will guide you through a few simple steps, asking for the necessary information to create your collection.

### 1. Enter the SD card path

The script will first ask for the path to your **SD card**.

* **Example (Windows):** `E:\`
* **Example (macOS/Linux):** `/Volumes/MIYOOSD` (Note: The script might need adjustments for non-Windows paths, but for typical use, entering the mount point should work.)

### 2. Enter the collection name

This will be the name of the generated file (`<name\>.txt`) and how it appears in the **Collections** menu.

* **Example:** `Pokemon`
* **Resulting file:** `E:\Collections\Pokemon.txt`

### 3. Enter search parameters

Enter one or more keywords that **must** be present in the ROM filename (case-insensitive) for the file to be included in the collection. Separate multiple parameters with **commas** (`,`).

* **Example:** If you enter `mario,bros`, only files containing **both** "mario" **and** "bros" will be included (e.g., `Super Mario Bros.nes`).

### 4. Enter exclude parameters
Enter one or more keywords that, if present in the ROM filename (case-insensitive), will **exclude** the file from the collection. Separate multiple parameters with **commas** (`,`).

* This is useful for filtering out unwanted files like **ROM hacks**, **translations**, **demos**, or specific regional versions.
* **Leave empty** and press Enter if you don't want to exclude anything.

### Output
Once completed, the script will confirm the location of the newly created collection file inside the `Collections` folder on your SD card.

## 💡 MinUI Collections

Collection files (`.txt`) are not **official** supported but last MinUI versions can handle a **`Collections`** folder in the root of MinUI SD card. Each line in the file must contain the **absolute path** of a ROM, relative to the SD card root (starting with `/`).

Example of a collection file content:

```
/Roms/GBA/Final Fantasy VXI.gba
/Roms/GBA/Final Fantasy Advance (USA).gba
/Roms/SNES/Final Fantasy IIXXI (USA).sfc
/Roms/NES/Final Fantasy Really (Hack) (USA).nes
```

## 🧻 License

```
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
```
