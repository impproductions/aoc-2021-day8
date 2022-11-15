import re

data = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
]

def intersection(a, b):
    return list(set(a) & set(b))

# when intersecting each set of segments (ie representation of a digit) with all the others,
# the list of intersections (which I'm calling fingerprint) is unique and represents
# the relationship between the sets of segments, which is the same regardless of how each segment is represented
def generate_fingerprints(input: list):
    return [sorted(fingerprint) for fingerprint in [[len(intersection(seq, other_seq)) for other_seq in input] for seq in input]]

# the order is important here, because the index is the corresponding digit, and is looked up later
reference_fingerprints = generate_fingerprints([
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg"
])

# create a dictionary that associates numbers to sets of segments to be used in translation
# by generating fingerprints for the input and comparing them to the reference
def generate_dictionary(input_digits):
    return { ''.join(sorted(input_digits[i])): reference_fingerprints.index(fingerprint) for i, fingerprint in enumerate(generate_fingerprints(input_digits)) }

def translate_digit(untranslated, dictionary):
    return str(dictionary[''.join(sorted(untranslated))])

def translate_all_digits(data):
    return [int(''.join([translate_digit(digit, generate_dictionary(entry.split(" | ")[0].split())) for digit in entry.split(" | ")[1].split()])) for entry in data]

def part1():
    return len(re.findall("[1478]", ''.join(map(str, translate_all_digits(data)))))

def part2():
    return sum(translate_all_digits(data))
    
print("part 1: " + str(part1()))
print("part 2: " + str(part2()))