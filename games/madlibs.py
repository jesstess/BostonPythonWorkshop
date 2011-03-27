# Word type prompts to display to the user.
girls_name = "girl's name"
pp_verb = "present participle (-ing form of verb)"
noun = "noun"
plural_noun = "plural noun"
adjective = "adjective"
emotion = "emotion"
adverb = "adverb"
living_thing = "living thing"
pt_verb = "past tense verb"

# A list of labels for word types to be supplied by the user. Even if
# a label is used multiple times in the story (e.g. if it is a name
# that is said several times), only prompt for it once.
word_types = [
    ("girls_name_1", girls_name),
    ("pp_verb_1", pp_verb),
    ("living_thing_1", living_thing),
    ("plural_noun_1", plural_noun),
    ("plural_noun_2", plural_noun),
    ("adjective_1", adjective),
    ("adjective_2", adjective),
    ("emotion_1", emotion),
    ("noun_1", noun),
    ("pp_verb_2", pp_verb),
    ("adverb_1", adverb),
    ("living_thing_2", living_thing),
    ("plural_noun_3", plural_noun),
    ("pt_verb_1", pt_verb),
    ]

# A list of what goes in each blank in the story. If a response is
# used multiple times in the story, the label for it is in this list
# multiple times.
word_occurences = [
    "girls_name_1",
    "pp_verb_1",
    "living_thing_1",
    "living_thing_1",
    "plural_noun_1",
    "plural_noun_2",
    "girls_name_1",
    "plural_noun_1",
    "plural_noun_2",
    "adjective_1",
    "adjective_2",
    "emotion_1",
    "noun_1",
    "pp_verb_2",
    "noun_1",
    "adverb_1",
    "living_thing_2",
    "plural_noun_3",
    "pt_verb_1",
]

# Use canned responses to fill out the story instead of having to
# enter them manually at a prompt.
canned_responses = {"girls_name_1": "Alice",
                    "pp_verb_1": "sitting",
                    "living_thing_1": "sister",
                    "plural_noun_1": "pictures",
                    "plural_noun_2": "conversations",
                    "adjective_1": "sleepy",
                    "adjective_2": "stupid",
                    "emotion_1": "pleasure",
                    "noun_1": "daisy",
                    "pp_verb_2": "picking",
                    "adverb_1": "suddenly",
                    "living_thing_2": "rabbit",
                    "plural_noun_3": "eyes",
                    "pt_verb_1": "ran"}

debug = False
if debug:
    provided_words = canned_responses
else:
    provided_words = dict()
    for type, display_text in word_types:
        answer = raw_input(display_text + ": ")
        provided_words[type] = answer

words_for_story = []
for word in word_occurences:
    words_for_story.append(provided_words[word])

story = """
%s was beginning to get very tired of %s by her %s on the bank, and of
having nothing to do: once or twice she had peeped into the book her
%s was reading, but it had no %s or %s in it, `and what is the use of
a book,' thought %s `without %s or %s?'

So she was considering in her own mind (as well as she could, for the
hot day made her feel very %s and %s), whether the %s of making a
%s-chain would be worth the trouble of getting up and %s the %s, when
%s a white %s with pink %s %s close by her.
""" % tuple(words_for_story)

print story
