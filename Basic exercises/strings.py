dna = "ATGCGATCGATCGATCGATCGA"

#The total length of the string

print("Lenght:", len(dna))

#The first 5 characters

print("First 5:",dna[:5])

#The last 3 characters

print("Last 3:", dna[-3:])

#The string converted to lowercase

print("Lowercase:",dna.lower())

#How many times the substring "ATC" appears

i = 0
atc_count = 0
while i < len(dna) - 2:
    if dna[i] == "A" and dna[i + 1] == "T" and dna[i + 2] == "C":
        atc_count += 1
    i += 1
print("ATC count:", atc_count)

#The string with all occurrences of "T" replaced by "U" (DNA to RNA transcription)

new_dna = ""
for base in dna:
    if base == "T":
        new_dna += "U"
    else:
        new_dna += base
print("RNA:", new_dna)

