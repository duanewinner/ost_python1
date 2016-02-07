#!/usr/local/bin/python3
"""Break up a paragraph into sentences and phrases. Sentences are delineated by periods and phrases are delineated by commas."""

import string

line_sep = "*" * 80

big_ass_string = \
  "We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness. - That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, - That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness. Prudence, indeed, will dictate that Governments long established should not be changed for light and transient causes; and accordingly all experience hath shewn that mankind are more disposed to suffer, while evils are sufferable than to right themselves by abolishing the forms to which they are accustomed. But when a long train of abuses and usurpations, pursuing invariably the same Object evinces a design to reduce them under absolute Despotism, it is their right, it is their duty, to throw off such Government, and to provide new Guards for their future security.  - Such has been the patient sufferance of these Colonies; and such is now the necessity which constrains them to alter their former Systems of Government. The history of the present King of Great Britain is a history of repeated injuries and usurpations, all having in direct object the establishment of an absolute Tyranny over these States. To prove this, let Facts be submitted to a candid world."


"""
big_ass_string = \
  "Lesh (On \"Box of Rain\"): The lyrics came about in an unusual way. This was the first time I had written a song in a long time, and I had worked out the melody and the chords, and in fact the whole song, from beginning to end—introduction, coda, and everything—and I put it on a tape and gave it to Hunter. Hunter: He'd just written these lovely changes and put 'em on a tape on a tape for me, and he sang along (scat singing of melody)—so the phrasing was all there, I think I went through it two or three times, writing as fast as I could, and that song was written. I guess it was written for a young man whose father was dying. Lesh: And at that time, my dad was dying of cancer, and I would drive out to visit with him, in the hospital, and also at the nursing home he spent his final days in, and after Bob gave me the lyrics, on the way out there I would practice singing the song. I sort of identified that song with my dad and his approaching death. The lyrics that he produced were so apt, so perfect. It was very moving, very moving for me to experience that during the period of my dad's passing. I felt like singing it in other situations similar to that since then."
"""

for snum, sentence in enumerate(big_ass_string.split(".")):
    if sentence:
        print(line_sep)
        print("Sentence #" + str(snum+1))
        for pnum, phrase in enumerate(sentence.split(",")):
            print("Phrase " + str(pnum+1) + ": " + (phrase.lstrip(" - ")).lstrip())
print(line_sep)


