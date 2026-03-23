#!/usr/bin/env python3
"""Update transliterations and translations for doha groups 66-130 in ayodhya-kand.json"""

import json

INPUT = r"c:/_work/RamayanaPath/data/tulsidas/ayodhya-kand.json"

with open(INPUT, "r", encoding="utf-8") as f:
    data = json.load(f)

# Build a lookup: verse_id -> {transliteration, translation}
updates = {
    # ===== DOHA GROUP 66 =====
    "ay-66-c1": {
        "transliteration": "banadevīṁ banadeva udārā, karihahiṁ sāsu sasura sama sārā.\nkusa kisalaya sātharī suhāī, prabhu saṁga mañju manoja turāī.",
        "translation": "The generous forest goddesses and gods will care for me like mother-in-law and father-in-law.\nA lovely bed of kusha grass and tender leaves, in my Lord's company, will be as beautiful as Cupid's own couch."
    },
    "ay-66-c2": {
        "transliteration": "kanda mūla phala amia ahārū, avadha saudha sata sarisa pahārū.\nchinu chinu prabhu pada kamala biloki, rahihauṁ mudita divasa jimi kokī.",
        "translation": "Roots, fruits and tubers will be like ambrosia for food; the mountains will seem like a hundred palaces of Ayodhya.\nGazing at the Lord's lotus feet every moment, I shall remain happy like the chakwa bird during daytime."
    },
    "ay-66-c3": {
        "transliteration": "bana dukha nātha kahe bahutere, bhaya biṣāda paritāpa ghanere.\nprabhu biyoga lavalesa samānā, saba mili hohi na kṛpānidhānā.",
        "translation": "You have described many hardships of the forest, O Lord — fears, sorrows and afflictions aplenty.\nBut they all combined cannot equal even a fraction of the pain of separation from You, O treasury of mercy."
    },
    "ay-66-c4": {
        "transliteration": "asa jiyaṁ jāni sujāna siromanī, leia saṁga mohi chāḍia jani.\nbinatī bahuta karauṁ kā svāmī, karunāmaya ura aṁtarajāmī.",
        "translation": "Knowing this in Your heart, O crest-jewel among the wise, take me along and do not leave me behind.\nHow much more shall I entreat, O Lord? You are compassionate and know the innermost feelings of all hearts."
    },
    "ay-66-d": {
        "transliteration": "rākhia avadha jo avadhi lagi rahata na jāniahiṁ prāna.\ndīnabaṁdhu suṁdara sukhada sīla saneha nidhāna. 66.",
        "translation": "Keep me in Ayodhya only if my life can last till the end of the exile period.\nO friend of the meek, beautiful, bliss-giving, and treasury of grace and love!"
    },

    # ===== DOHA GROUP 67 =====
    "ay-67-c1": {
        "transliteration": "mohi maga calata na hoihi hārī, chinu chinu carana saroja nihārī.\nsabahi bhāṁti piya sevā karihauṁ, māraga janita sakala śrama harihauṁ.",
        "translation": "I shall not grow weary walking on the path, gazing at Your lotus feet every moment.\nI shall serve my beloved in every way and remove all the fatigue caused by the journey."
    },
    "ay-67-c2": {
        "transliteration": "pāya pakhāri baiṭhi taru chāhīṁ, karihauṁ bāu mudita mana māhīṁ.\nśrama kana sahita syāma tanu dekhēṁ, kahaṁ dukha samau prānapati pekhēṁ.",
        "translation": "Washing Your feet and sitting in the shade of a tree, I shall fan You with a joyful heart.\nSeeing my dark-complexioned Lord's body glistening with drops of perspiration, where is any room for sorrow?"
    },
    "ay-67-c3": {
        "transliteration": "sama mahī tṛna tarupalava ḍāsī, pāga paloṭihi saba nisi dāsī.\nbārabāra mṛdu mūrati johī, lāgahi tāta bayāri na mohī.",
        "translation": "Spreading grass and leaves on level ground, this maidservant shall press Your feet all night long.\nGazing again and again at Your tender form, may no breeze touch You, dear Lord."
    },
    "ay-67-c4": {
        "transliteration": "ko prabhu saṁga mohi citavanihārā, siṁghabadhūhi jimi sasaka siārā.\nmaiṁ sukumāri nātha bana jogū, tumhahi ucita tapa mo kahuṁ bhogū.",
        "translation": "Who would dare look at me with my Lord beside me — like a hare or jackal eyeing a lioness?\nYou say I am delicate and the forest suits only You; that austerity befits You and luxury befits me."
    },
    "ay-67-d": {
        "transliteration": "aiseu bacana kaṭhora suni jauṁ na hṛdau bilagāna.\ntau prabhu biṣama biyoga dukha sahihahiṁ pāvara prāna. 67.",
        "translation": "If even after hearing such harsh words my heart does not break apart,\nthen these wretched vital breaths shall endure the terrible agony of separation from my Lord."
    },

    # ===== DOHA GROUP 68 =====
    "ay-68-c1": {
        "transliteration": "asa kahi sīya bikala bhai bhārī, bacana biyogu na sakī saṁbhārī.\ndekhi dasā raghupati jiyaṁ jānā, haṭhi rākhēṁ nahiṁ rākhihi prānā.",
        "translation": "Saying this, Sita became extremely distressed; she could not bear even the word 'separation.'\nSeeing her condition, Raghupati understood in His heart that if He stubbornly kept her back, she would not survive."
    },
    "ay-68-c2": {
        "transliteration": "kaheu kṛpāla bhānukulanāthā, parihari socu calahu bana sāthā.\nnahiṁ biṣāda kara avasaru ājū, begi karahu bana gavana samājū.",
        "translation": "The gracious Lord of the Solar dynasty said: 'Give up worry and come to the forest with me.\nToday is not the time for sorrow; quickly make preparations for the journey to the forest.'"
    },
    "ay-68-c3": {
        "transliteration": "kahi priya bacana priyā samujhāī, lage mātu pada āsiṣa pāī.\nbegi prajā dukha meṭaba āī, jananī niṭhura bisari jani jāī.",
        "translation": "Consoling His beloved with loving words, He touched His mother's feet and received her blessings.\n'I shall return soon and wipe away the people's sorrows; O mother, cruel as fate is, please do not forget me.'"
    },
    "ay-68-c4": {
        "transliteration": "phirahi dasā bidhi bahuri ki morī, dekhihauṁ nayana manohara jorī.\nsudina sugharī tāta kaba hoihi, jananī jiata badana bidhu joihi.",
        "translation": "'Will fate ever turn in my favor again, that I may behold this enchanting couple with my own eyes?\nWhen will that blessed, auspicious day come, O son, when this mother may live to see your moon-like face?'"
    },
    "ay-68-d": {
        "transliteration": "bahuri baccha kahi lālu kahi raghupati raghubara tāta.\nkabahiṁ bolāi lāgai hiyaṁ haraṣi nirakhihauṁ gāta. 68.",
        "translation": "Calling him 'my child,' 'my darling,' 'Raghupati,' 'best of Raghus,' 'my son' —\n'When shall I call you, press you to my heart, and joyfully gaze upon your form?'"
    },

    # ===== DOHA GROUP 69 =====
    "ay-69-c1": {
        "transliteration": "lakhi saneha kātari mahatārī, bacanu na āva bikala bhai bhārī.\nrāma prabodhu kīnha bidhi nānā, samau sanehu na jāi bakhānā.",
        "translation": "Seeing the mother overwhelmed with love, no words would come; she became extremely distraught.\nRama consoled her in various ways; that moment of tender love cannot be described."
    },
    "ay-69-c2": {
        "transliteration": "taba jānakī sāsu paga lāgī, sunia māya maiṁ parama abhāgī.\nsevā samaya daiaṁ banu dīnhā, mora manorathū saphala na kīnhā.",
        "translation": "Then Janaki touched her mother-in-law's feet: 'Listen, O mother, I am most unfortunate.\nAt the very time when I should be serving you, fate has given us exile to the forest; my heart's desire remains unfulfilled.'"
    },
    "ay-69-c3": {
        "transliteration": "tajaba chobhu jani chāḍia chohū, karamu kaṭhina kachu dosu na mohū.\nsuni siya bacana sāsu akulānī, dasā kavani bidhi kahauṁ bakhānī.",
        "translation": "'Please give up your agitation but do not abandon your affection; fate is harsh, there is no fault of mine.'\nHearing Sita's words, the mother-in-law became distraught — how can I describe her condition?"
    },
    "ay-69-c4": {
        "transliteration": "bārahi bāra lāi ura līnhī, dhari dhīraju sikha āsiṣa dīnhī.\nacala hou ahivātu tumhārā, jaba lagi gaṁga jamuna jala dhārā.",
        "translation": "Again and again she pressed Sita to her bosom; gathering courage, she gave her counsel and blessings.\n'May your married bliss be eternal, as long as the waters of Ganga and Yamuna flow.'"
    },
    "ay-69-d": {
        "transliteration": "sītahi sāsu asīsa sikha dīnhi aneka prakāra.\ncalī nāi pada paduma siru ati hita bārahi bāra. 69.",
        "translation": "The mother-in-law gave Sita blessings and counsel of many kinds.\nBowing her head at her lotus feet again and again with great affection, Sita departed."
    },

    # ===== DOHA GROUP 70 =====
    "ay-70-c1": {
        "transliteration": "samācāra jaba lachimana pāe, byākula bilakha badana uṭhi dhāe.\nkaṁpa pulaka tana nayana sanīrā, gahe carana ati prema adhīrā.",
        "translation": "When Lakshmana received the news, he rose in agitation with a sorrowful face and rushed forth.\nHis body trembling and thrilling, eyes filled with tears, he clasped Rama's feet, overcome with love."
    },
    "ay-70-c2": {
        "transliteration": "kahi na sakata kachu citavata ṭhāḍhe, mīnu dīna janu jala tēṁ kāḍhe.\nsocu hṛdayaṁ bidhi kā honihārā, sabu sukhu sukṛta sirāna hamārā.",
        "translation": "Unable to speak, he stood gazing — pitiful as a fish drawn out of water.\nHis heart was anxious: 'What will fate bring? All our happiness and good fortune has ended.'"
    },
    "ay-70-c3": {
        "transliteration": "mo kahuṁ kāha kahaba raghunāthā, rakhihahiṁ bhavana ki lehahiṁ sāthā.\nrāma biloki baṁdhu kara jorēṁ, deha geha saba sana tṛnu torēṁ.",
        "translation": "'What will the Lord of the Raghus tell me — will He keep me at home or take me along?'\nRama saw His brother standing with folded hands, having renounced all attachment to body and home."
    },
    "ay-70-c4": {
        "transliteration": "bole bacanu rāma naya nāgara, sīla saneha sarala sukha sāgara.\ntāta prema basa jani kadarāhū, samujhi hṛdayaṁ parināma uchāhū.",
        "translation": "Rama, that ocean of wisdom, virtue, love, and guileless bliss, spoke these words:\n'Dear brother, do not be despondent out of love; reflect in your heart that the outcome will be joyful.'"
    },
    "ay-70-d": {
        "transliteration": "mātu pitā guru svāmi sikha sira dhari karahi subhāyaṁ.\nlaheu lābhu tinha janama kara nataru janamu jaga jāyaṁ. 70.",
        "translation": "Those who naturally and willingly obey the instructions of mother, father, guru and master —\nthey have reaped the reward of their birth; otherwise, birth in this world is in vain."
    },

    # ===== DOHA GROUP 71 =====
    "ay-71-c1": {
        "transliteration": "asa jiyaṁ jāni sunahu sikha bhāī, karahu mātu pitu pada sevakāī.\nbhavana bharatu ripusūdana nāhīṁ, rāu bṛddha mama dukhu mana māhīṁ.",
        "translation": "Knowing this in your heart, listen to my counsel, brother: serve at the feet of our mother and father.\nBharata and Shatrughna are not at home; the king is old, and this weighs on my mind."
    },
    "ay-71-c2": {
        "transliteration": "maiṁ bana jāuṁ tumhahi lei sāthā, hoi sabahi bidhi avadha anāthā.\nguru pitu mātu prajā parivārū, saba kahuṁ parai dusaha dukha bhārū.",
        "translation": "If I go to the forest taking you along, Ayodhya will become utterly desolate.\nThe guru, father, mothers, subjects and the whole family — an unbearable burden of sorrow will fall upon all."
    },
    "ay-71-c3": {
        "transliteration": "rahahu karahu saba kara paritoṣū, nataru tāta hoihi baḍa doṣū.\njāsu rāja priya prajā dukhārī, so nṛpu avasi naraka adhikārī.",
        "translation": "Stay here and keep everyone content; otherwise, dear brother, there will be great sin.\nA king in whose reign his beloved subjects suffer is certainly destined for hell."
    },
    "ay-71-c4": {
        "transliteration": "rahahu tāta asi nīti bicārī, sunata lakhanu bhae byākula bhārī.\nsiarēṁ bacana sūkhi gae kaisēṁ, parasata tuhina tāmarasu jaisēṁ.",
        "translation": "Stay here, brother, keeping this principle in mind.' Hearing this, Lakshmana became deeply agitated.\nHis lips dried up as if withered by these cold words, like a lotus touched by frost."
    },
    "ay-71-d": {
        "transliteration": "utaru na āvata prema basa gahe carana akulāi.\nnātha dāsu maiṁ svāmi tumha tajahu ta kāha basāi. 71.",
        "translation": "Overwhelmed by love, no reply would come; he clasped Rama's feet in distress.\n'Lord, I am Your servant and You are my master; if You abandon me, what can I do?'"
    },

    # ===== DOHA GROUP 72 =====
    "ay-72-c1": {
        "transliteration": "dīnhi mohi sikha nīki gosāīṁ, lāgi agama apanī kadarāīṁ.\nnarabara dhīra dharama dhura dhārī, nigama nīti kahuṁ te adhikārī.",
        "translation": "'You have given me good counsel, my Lord, but it seems impossibly daunting and I feel afraid.\nThe brave and steadfast men who uphold the banner of dharma — they are worthy of Vedic precepts.'"
    },
    "ay-72-c2": {
        "transliteration": "maiṁ sisu prabhu sanēhaṁ pratipālā, maṁdaru meru ki lehiṁ marālā.\ngura pitu mātu na jānauṁ kāhū, kahauṁ subhāu nātha patiāhū.",
        "translation": "'I am a child, nurtured by my Lord's love; can a swan carry Mount Mandara or Meru?\nI know no guru, father or mother other than You; I speak my true nature, Lord — please believe me.'"
    },
    "ay-72-c3": {
        "transliteration": "jahaṁ lagi jagata saneha sagāī, prīti pratīti nigama niju gāī.\nmorēṁ sabai eka tumha svāmī, dīnabaṁdhu ura aṁtarajāmī.",
        "translation": "'Whatever bonds of love and kinship exist in the world, whatever affection and trust the Vedas themselves sing of —\nfor me, You alone are everything, O Lord — friend of the meek, knower of all hearts.'"
    },
    "ay-72-c4": {
        "transliteration": "dharama nīti upadesia tāhī, kīrati bhūti sugati priya jāhī.\nmana krama bacana carana rata hoī, kṛpāsiṁdhu pariharia ki soī.",
        "translation": "'Preach dharma and propriety to one who holds dear fame, prosperity and salvation.\nCan one who is devoted to Your feet in thought, word and deed be forsaken, O ocean of mercy?'"
    },
    "ay-72-d": {
        "transliteration": "karunāsiṁdhu subaṁdha ke suni mṛdu bacana binīta.\nsamujhāe ura lāi prabhu jāni sanēhaṁ sabhīta. 72.",
        "translation": "Hearing the soft and humble words of His dear brother, the ocean of compassion\nembraced him and consoled him, knowing he was frightened by love."
    },

    # ===== DOHA GROUP 73 =====
    "ay-73-c1": {
        "transliteration": "māgahu bidā mātu sana jāī, āvahu begi calahu bana bhāī.\nmudita bhae suni raghubara bānī, bhayau lābha baḍa gai baḍi hānī.",
        "translation": "'Go and ask leave of your mother, and come back quickly — let us go to the forest, brother.'\nHearing Raghubara's words, Lakshmana was overjoyed — great was the gain, and the great loss was averted."
    },
    "ay-73-c2": {
        "transliteration": "haraṣita hṛdayaṁ mātu pahiṁ āe, manahuṁ aṁdha phiri locana pāe.\njāi jananī paga nāyau māthā, manu raghanaṁdana jānaki sāthā.",
        "translation": "With a joyful heart he came to his mother, as if a blind man had regained his sight.\nHe went and bowed his head at his mother's feet, his mind already with Rama and Janaki."
    },
    "ay-73-c3": {
        "transliteration": "pūṁche mātu malina mana dekhī, lakhana kahī saba kathā biseṣī.\ngaī sahami suni bacana kaṭhorā, mṛgī dekhi dava janu cahu orā.",
        "translation": "The mother asked, seeing his downcast face; Lakshmana told her the whole story in detail.\nShe was stunned hearing the harsh account, like a doe seeing a wildfire raging on all sides."
    },
    "ay-73-c4": {
        "transliteration": "lakhana lakheu bhā anaratha ājū, ehi saneha basa karaba akājū.\nmāgata bidā sabhaya sakucāhīṁ, jāi saṁga bidhi kahihi ki nāhī.",
        "translation": "Lakshmana perceived: 'Calamity has struck today; overcome by love she may prevent my going.'\nHe hesitated, afraid to ask for leave, uncertain whether fate would let him go along or not."
    },
    "ay-73-d": {
        "transliteration": "samujhi sumitrāṁ rāma siya rūpa susīlu subhāu.\nnṛpa sanehu lakhi dhuneu siru pāpini dīnha kudāu. 73.",
        "translation": "Sumitra reflected on Rama and Sita's beauty, virtue and noble nature;\nseeing the king's love for them, she struck her head and cursed the sinful Kaikeyi who had brought this calamity."
    },

    # ===== DOHA GROUP 74 =====
    "ay-74-c1": {
        "transliteration": "dhīraju dhareu kuavasara jānī, sahaja suhṛda bolī mṛdu bānī.\ntāta tumhāri mātu baidehī, pitā rāmu saba bhāṁti snehī.",
        "translation": "Gathering courage and recognizing the gravity of the moment, the naturally kind-hearted Sumitra spoke gently:\n'Son, Vaidehi is your mother and Rama is your father — loving you in every way.'"
    },
    "ay-74-c2": {
        "transliteration": "avadha tahāṁ jahaṁ rāma nivāsū, tahāṁiṁ divasu jahaṁ bhānu prakāsū.\njau pai sīya rāmu bana jāhīṁ, avadha tumhāra kāju kachu nāhiṁ.",
        "translation": "'Ayodhya is wherever Rama dwells, just as daytime exists wherever the sun shines.\nIf Sita and Rama go to the forest, you have nothing left to do in Ayodhya.'"
    },
    "ay-74-c3": {
        "transliteration": "guru pitu mātu baṁdhu sura sāī, seiahiṁ sakala prāna kī nāīṁ.\nrāmu prānapriya jīvana jī ke, svāratha rahita sakhā sabahī kai.",
        "translation": "'Guru, father, mother, brother, and divine lord — all should be served as dearly as one's own life.\nRama is dearer than life itself, the very life of all lives, a selfless friend to everyone.'"
    },
    "ay-74-c4": {
        "transliteration": "pūjanīya priya parama jahāṁ tēṁ, saba māniahiṁ rāma ke nātēṁ.\nasa jiyaṁ jāni saṁga bana jāhū, lehu tāta jaga jīvana lāhū.",
        "translation": "'All who are worthy of worship and supremely dear are so because of their connection to Rama.\nKnowing this in your heart, go with Him to the forest, and reap the true reward of life, my son.'"
    },
    "ay-74-d": {
        "transliteration": "bhūri bhāga bhājanu bhayahu mohi sameta bali jāuṁ.\njauṁ tumharēṁ mana chāḍi chalu kīnha rāma pada ṭhāuṁ. 74.",
        "translation": "'You have become a vessel of great fortune — I sacrifice myself for you —\nif in your heart, forsaking all guile, you have found a place at Rama's feet.'"
    },

    # ===== DOHA GROUP 75 =====
    "ay-75-c1": {
        "transliteration": "putravatī jubatī jaga soī, raghupati bhagatu jāsu sutu hoī.\nnataru bāṁjha bhali bādi biānī, rāma bimukha suta tēṁ hita jānī.",
        "translation": "'Only that woman in the world is truly a blessed mother whose son is a devotee of Raghupati.\nOtherwise, it is better to be barren than to give birth in vain — thinking a son who is averse to Rama to be one's well-wisher.'"
    },
    "ay-75-c2": {
        "transliteration": "tumharehiṁ bhāga rāmu bana jāhīṁ, dūsara hetu tāta kachu nāhīṁ.\nsakala sukṛta kara baḍa phalu ehū, rāma sīya pada sahaja sanehū.",
        "translation": "'It is because of your good fortune that Rama is going to the forest; there is no other reason, my son.\nThe greatest fruit of all meritorious deeds is spontaneous love for the feet of Rama and Sita.'"
    },
    "ay-75-c3": {
        "transliteration": "rāga roṣu iriṣā madu mohū, jani sapanēhuṁ inha ke basa hohū.\nsakala prakāra bikāra bihāī, mana krama bacana karehu sevakāī.",
        "translation": "'Passion, anger, envy, pride and delusion — never fall under their sway, even in dreams.\nAbandoning all kinds of impurities, serve Rama in thought, word and deed.'"
    },
    "ay-75-c4": {
        "transliteration": "tumha kahuṁ bana saba bhāṁti supāsū, saṁga pitu mātu rāmu siya jāsū.\njehi na rāmu bana lahahiṁ kalesū, suta soi karehu ihai upadesū.",
        "translation": "'For you, the forest will have every comfort, as Rama and Sita — your father and mother — will be with you.\nDo whatever keeps Rama free from distress in the forest — this is my final teaching to you.'"
    },
    "ay-75-ch": {
        "transliteration": "upadesū yaha jehi tāta tumhare rāma siya sukha pāvahīṁ.\npitu mātu priya parivāra pura sukha surati bana bisarāvahīṁ.\ntulasī prabuhi sikha dei āyasu dīnha puni āsiṣa daī.\nrati hou abirala amala siya raghubīra pada nita nita naī.",
        "translation": "This is my teaching: do whatever brings happiness to your Rama and Sita,\nand make them forget the pleasures and memories of parents, dear ones, family and city in the forest.\nTulasidas says, having given this counsel, Sumitra granted her permission and then gave her blessing:\n'May your devotion to the feet of Sita and Raghubira remain ever fresh, unbroken and pure.'"
    },
    "ay-75-d": {
        "transliteration": "mātu carana siru nāi cale turata saṁkita hṛdayaṁ.\nbāgura biṣama torāi manahuṁ bhāga mṛgu bhāga basa. 75.",
        "translation": "Bowing his head at his mother's feet, he left at once with an anxious heart,\nlike a deer that, by good fortune, breaks free from a dreadful snare and runs away."
    },

    # ===== DOHA GROUP 76 =====
    "ay-76-c1": {
        "transliteration": "gae lakhanu jahaṁ jānakināthū, bhe mana mudita pāi priya sāthū.\nbaṁdi rāma siya carana suhāe, cale saṁga nṛpamaṁdira āe.",
        "translation": "Lakshmana went to where the Lord of Janaki was; his heart rejoiced at obtaining his dear Lord's company.\nBowing at the lovely feet of Rama and Sita, he accompanied them as they came to the royal palace."
    },
    "ay-76-c2": {
        "transliteration": "kahahiṁ parasapara pura nara nārī, bhali banāi bidhi bāta bigārī.\ntana kṛsa dukhu badana malīne, bikala manahuṁ mākhī madhu chīne.",
        "translation": "The men and women of the city said to one another: 'Fate first arranged things well and then ruined everything.'\nTheir bodies were thin with grief, their faces pale — distraught like bees robbed of their honey."
    },
    "ay-76-c3": {
        "transliteration": "kara mījahiṁ siru dhuni pachitāhīṁ, janu binu paṁkha bihaga akulāhīṁ.\nbhai baḍi bhīra bhūpa darabārā, barani na jāi biṣādu apārā.",
        "translation": "They wrung their hands, struck their heads and lamented, restless like birds without wings.\nA great crowd gathered in the king's court; the immeasurable grief cannot be described."
    },
    "ay-76-c4": {
        "transliteration": "sacivaṁ uṭhāi rāu baiṭhāre, kahi priya bacana rāmu pagu dhāre.\nsiya sameta dou tanaya nihārī, byākula bhayau bhūmipati bhārī.",
        "translation": "The minister lifted and seated the king; speaking tender words, Rama entered.\nSeeing both sons together with Sita, the lord of the earth became deeply distraught."
    },
    "ay-76-d": {
        "transliteration": "sīya sahita suta subhaga dou dekhi dekhi akulāi.\nbārahi bāra saneha basa rāu lei ura lāi. 76.",
        "translation": "Seeing his two handsome sons together with Sita, the king was overwhelmed;\nagain and again, overcome by love, he pressed them to his heart."
    },

    # ===== DOHA GROUP 77 =====
    "ay-77-c1": {
        "transliteration": "sakai na boli bikala naranāhū, soka janita ura dāruna dāhū.\nnāi sīsu pada ati anurāgā, uṭhi raghubīra bidā taba māgā.",
        "translation": "The distressed king could not speak; a terrible burning grief had arisen in his heart.\nBowing His head at His father's feet with deep love, Raghubira then rose and asked for leave."
    },
    "ay-77-c2": {
        "transliteration": "pitu asīsa āyasu mohi dījai, haraṣa samaya bisamau kata kījai.\ntāta kiēṁ priya prema pramādū, jasu jaga jāi hoi apabādū.",
        "translation": "'Give me your blessing and your command, father; why grieve at what should be a time of joy?\nIf one neglects duty out of excess affection for a dear one, one's fame departs and reproach follows in the world.'"
    },
    "ay-77-c3": {
        "transliteration": "suni saneha basa uṭhi naranāhāṁ, baiṭhāre raghupati gahi bāhāṁ.\nsunahu tāta tumha kahuṁ muni kahahīṁ, rāmu carācara nāyaka ahahīṁ.",
        "translation": "Hearing this, the king rose overcome by love, and seating Raghupati by holding His arm, said:\n'Listen, my son — the sages say of You that Rama is the Lord of all creation, animate and inanimate.'"
    },
    "ay-77-c4": {
        "transliteration": "subha aru asubha karama anuhārī, īsa dei phalu hṛdayaṁ bicārī.\nkarai jo karama pāva phala soī, nigama nīti asi kaha sabu koī.",
        "translation": "'God gives fruits according to one's good and bad deeds, weighing them in His heart.\nOne reaps the fruit of whatever action one performs — this is the doctrine of the Vedas, and everyone says so.'"
    },
    "ay-77-d": {
        "transliteration": "auru karai aparādhu kou aura pāva phala bhogu.\nati bicitra bhagavaṁta gati ko jaga jānai jogu. 77.",
        "translation": "'Yet here, one commits the offence and another reaps its fruit.\nMost mysterious are the ways of Providence — who in this world is able to understand them?'"
    },

    # ===== DOHA GROUP 78 =====
    "ay-78-c1": {
        "transliteration": "rāyaṁ rāma rākhana hita lāgī, bahuta upāya kie chalu tyāgī.\nlakhī rāma rukha rahata na jāne, dharama dhuraṁdhara dhīra sayāne.",
        "translation": "The king tried many sincere means to keep Rama back, abandoning all guile.\nBut he perceived that Rama, the wise and steadfast champion of dharma, was determined not to stay."
    },
    "ay-78-c2": {
        "transliteration": "taba nṛpa sīya lāi ura līnhī, ati hita bahuta bhāṁti sikha dīnhī.\nkahi bana ke dukha dusaha sunāe, sāsu sasura pitu sukha samujhāe.",
        "translation": "Then the king pressed Sita to his bosom and lovingly gave her much counsel.\nHe described the unbearable hardships of the forest and reminded her of the comforts of parents-in-law and father."
    },
    "ay-78-c3": {
        "transliteration": "siya manu rāma carana anurāgā, gharu na sugamu banu biṣamu na lāgā.\naurau sabahi sīya samujhāī, kahi kahi bipina bipati adhikāī.",
        "translation": "But Sita's heart was so devoted to Rama's feet that home did not seem agreeable nor the forest daunting.\nOthers too tried to dissuade Sita, describing the ever-increasing hardships of the wilderness."
    },
    "ay-78-c4": {
        "transliteration": "saciva nāri gura nāri sayānī, sahita saneha kahahiṁ mṛdu bānī.\ntumha kahuṁ tau na dīnha banabāsū, karahu jo kahahiṁ sasura guru sāsū.",
        "translation": "The wise wives of ministers and of the guru spoke affectionately in gentle tones:\n'You have not been sentenced to forest exile; do as your father-in-law, guru and mother-in-law tell you.'"
    },
    "ay-78-d": {
        "transliteration": "sikha sītalī hita madhura mṛdu suni sītahi na sohāni.\nsarada caṁda caṁdani lagata janu cakaī akulāni. 78.",
        "translation": "This cool, well-meaning, sweet and gentle advice did not please Sita,\njust as the autumnal moonlight makes the chakwi bird restless rather than soothed."
    },

    # ===== DOHA GROUP 79 =====
    "ay-79-c1": {
        "transliteration": "sīya sakuca basa utaru na deī, so suni tamaki uṭhī kaikeyī.\nmuni paṭa bhūṣana bhājana ānī, āgēṁ dhari bolī mṛdu bānī.",
        "translation": "Sita was too abashed to reply; hearing this, Kaikeyi sprang up impatiently.\nShe brought garments of bark, ornaments and vessels appropriate for an ascetic, placed them before Sita and spoke in a gentle tone."
    },
    "ay-79-c2": {
        "transliteration": "nṛpahi prāna priya tumha raghubīrā, sīla saneha na chāḍihi bhīrā.\nsukṛta sujasu paraloku nasāū, tumhahi jāna bana kahihi na kāū.",
        "translation": "'You are dearer to the king than life, O Raghubira; out of love and timidity he will never give up his affection.\nLet his merit, good name and the next world perish — he will never tell You to go to the forest.'"
    },
    "ay-79-c3": {
        "transliteration": "asa bicāri soi karahu jo bhāvā, rāma jananī sikha suni sukhu pāvā.\nbhūpahi bacana bānasama lāge, karahiṁ na prāna payāna abhāge.",
        "translation": "'Thinking thus, do whatever pleases You.' Rama was relieved to hear His stepmother's counsel.\nThe king felt her words pierce him like arrows, yet his wretched life-breaths would not depart."
    },
    "ay-79-c4": {
        "transliteration": "loga bikala muruchita naranāhū, kāha karia kachu sūjha na kāhū.\nrāmu turata muni beṣu banāī, cale janaka jananihi siru nāī.",
        "translation": "The people were distraught, the king had fainted — no one could think of what to do.\nRama quickly donned the garb of an ascetic and departed, bowing His head to His father and mothers."
    },
    "ay-79-d": {
        "transliteration": "saji bana sāju samāju sabu banitā baṁdhu sameta.\nbaṁdi bipra guru carana prabhu cale kari sabahi aceta. 79.",
        "translation": "Equipping Himself with all the necessities for forest life, along with His wife and brother,\nbowing at the feet of the Brahmins and the guru, the Lord departed, leaving everyone stunned."
    },

    # ===== DOHA GROUP 80 =====
    "ay-80-c1": {
        "transliteration": "nikasi basiṣṭha dvāra bhae ṭhāḍhe, dekhe loga biraha dava dāḍhe.\nkahi priya bacana sakala samujhāe, bipra bṛṁda raghubīra bolāe.",
        "translation": "Emerging through Vasishtha's gate, they stood outside; they saw the people scorched by the wildfire of separation.\nSpeaking kind words, Rama consoled everyone and then summoned the assembly of Brahmins."
    },
    "ay-80-c2": {
        "transliteration": "gura sana kahi baraṣāsana dīnhe, ādara dāna binaya basa kīnhe.\njācaka dāna māna saṁtoṣe, mīta punīta prema paritoṣe.",
        "translation": "With the guru's permission, He gave away annual provisions; He won people over with respect, gifts and humility.\nSupplicants were satisfied with gifts and honor; friends were gratified with pure love."
    },
    "ay-80-c3": {
        "transliteration": "dāsīṁ dāsa bolāi bahorī, gurahi sauṁpi bole kara jorī.\nsaba kai sāra saṁbhāra gosāīṁ, karabi janaka jananī kī nāī.",
        "translation": "Then He called all the male and female servants, entrusted them to the guru, and said with folded hands:\n'Take care of them all, my lord, as if you were their father and mother.'"
    },
    "ay-80-c4": {
        "transliteration": "bārahi bāra jori juga pānī, kahata rāmu saba sana mṛdu bānī.\nsoi saba bhāṁti mora hitakārī, jehi tēṁ rahai bhuāla sukhārī.",
        "translation": "Again and again, with joined palms, Rama spoke gentle words to all:\n'That person alone is my true well-wisher in every way who keeps the king happy.'"
    },
    "ay-80-d": {
        "transliteration": "mātu sakala more birahaṁ jehi na hohi dukha dīna.\nsoi upāu tumha karehu saba pura jana parama prabīna. 80.",
        "translation": "'In my absence, do whatever it takes so that all my mothers are not wretched with grief.\nDevise such measures, all you most skilled people of the city.'"
    },

    # ===== DOHA GROUP 81 =====
    "ay-81-c1": {
        "transliteration": "ehi bidhi rāma sabahi samujhāvā, guru pada paduma haraṣi siru nāvā.\ngaṇapati gaurī girīsu manāī, cale asīsa pāi raghurāī.",
        "translation": "In this way Rama consoled everyone, then joyfully bowed His head at the guru's lotus feet.\nPraying to Ganesh, Gauri and Lord Shiva, and receiving their blessings, the Lord of the Raghus departed."
    },
    "ay-81-c2": {
        "transliteration": "rāma calata ati bhayau biṣādū, suni na jāi pura ārata nādū.\nkusaguna laṁka avadha ati sokū, haharaṣa biṣāda bibasa suralokū.",
        "translation": "As Rama departed, there was immense grief; the anguished cries of the city were unbearable to hear.\nIll omens appeared in Lanka, extreme sorrow pervaded Ayodhya, and the realm of the gods was torn between joy and sorrow."
    },
    "ay-81-c3": {
        "transliteration": "gaī muruchā taba bhūpati jāge, boli sumaṁtru kahana asa lāge.\nrāmu cale bana prāna na jāhīṁ, kehi sukha lāgi rahata tana māhīṁ.",
        "translation": "When the spell of unconsciousness passed, the king awoke and, summoning Sumantra, began to say:\n'Rama has gone to the forest and yet my life does not leave — for what pleasure do these breaths remain in my body?'"
    },
    "ay-81-c4": {
        "transliteration": "ehi tēṁ kavana byathā balavānā, jo dukhu pāi tajahiṁ tanu prānā.\npuni dhari dhīra kahai naranāhū, lai rathu saṁga sakhā tumha jāhū.",
        "translation": "'Is there any greater agony than this, that people give up their lives upon receiving such pain?'\nThen, gathering courage, the king said: 'Take the chariot and go along with them, my friend.'"
    },
    "ay-81-d": {
        "transliteration": "suṭhi sukumāra kumāra dou janakasutā sukumāri.\nratha caḍhāi dekhāi banu phirehu gaēṁ dina cāri. 81.",
        "translation": "'Both the princes are most delicate, and the daughter of Janaka is tender.\nSeat them in the chariot, show them the forest, and bring them back in four days' time.'"
    },

    # ===== DOHA GROUP 82 =====
    "ay-82-c1": {
        "transliteration": "jau nahiṁ phirahiṁ dhīra dou bhāī, satyasaṁdha dṛḍhabrata raghurāī.\ntau tumha binaya karehu kara jorī, pheria prabhu mithilesākisorī.",
        "translation": "'If the two steadfast brothers do not return — Raghurai being firm in His vow of truth —\nthen entreat the Lord with folded hands: at least send back the daughter of Mithila's king.'"
    },
    "ay-82-c2": {
        "transliteration": "jaba siya kānana dekhi ḍerāī, kahehu mori sikha avasaru pāī.\nsāsu sasura asa kaheu saṁdesū, putri phiria bana bahuta kalesū.",
        "translation": "'When Sita is frightened seeing the forest, seize the opportunity and relay my counsel to her:\nYour father-in-law and mother-in-law have sent this message — come back, daughter, the forest holds much suffering.'"
    },
    "ay-82-c3": {
        "transliteration": "pitṛgṛha kabahūṁ kabahūṁ sasurārī, rahehu jahāṁ ruci hoi tumhārī.\nehi bidhi karehu upāya kadaṁbā, phirai ta hoi prāna avalaṁbā.",
        "translation": "'Stay sometimes at your father's house and sometimes at your in-laws; live wherever you please.\nTry every possible means in this way; if she returns, it will be the sustenance of my life.'"
    },
    "ay-82-c4": {
        "transliteration": "nāhiṁ ta mora maranu parināmā, kachu na basāi bhaēṁ bidhi bāmā.\nasa kahi muruchi parā mahī rāū, rāmu lakhanu siya āni dekhāū.",
        "translation": "'Otherwise, death will be my ultimate fate; nothing can be done when destiny turns hostile.'\nSaying this, the king fainted and fell to the ground — 'Bring Rama, Lakshmana and Sita, let me see them!'"
    },
    "ay-82-d": {
        "transliteration": "pāi rajāyasu nāi siru rathu ati bega banāi.\ngayau jahāṁ bāhera nagara sīya sahita dou bhāi. 82.",
        "translation": "Receiving the king's command and bowing his head, Sumantra readied the chariot with utmost speed.\nHe drove to where, outside the city, the two brothers were with Sita."
    },

    # ===== DOHA GROUP 83 =====
    "ay-83-c1": {
        "transliteration": "taba sumaṁtra nṛpa bacana sunāe, kari binatī ratha rāmu caḍhāe.\ncaḍhi ratha sīya sahita dou bhāī, cale hṛdayaṁ avadhahi siru nāī.",
        "translation": "Then Sumantra conveyed the king's words and, making earnest entreaties, got Rama to mount the chariot.\nMounting the chariot with Sita and His brother, they departed, bowing their heads to Ayodhya in their hearts."
    },
    "ay-83-c2": {
        "transliteration": "calata rāmu lakhi avadha anāthā, bikala loga saba lāge sāthā.\nkṛpāsiṁdhu bahubidhi samujhāvahiṁ, phirahiṁ prema basa puni phiri āvahiṁ.",
        "translation": "Seeing Rama depart, the people of now-desolate Ayodhya, all distraught, followed Him.\nThe ocean of compassion tried in many ways to persuade them to turn back, but overcome by love, they kept returning."
    },
    "ay-83-c3": {
        "transliteration": "lāgati avadha bhayāvani bhārī, mānahuṁ kālarāti aṁdhiārī.\nghora jaṁtu sama pura nara nārī, ḍarapahiṁ ekahi eka nihārī.",
        "translation": "Ayodhya seemed dreadfully fearsome, as though it were the dark night of cosmic dissolution.\nThe men and women of the city were like frightened creatures, terrified at the very sight of one another."
    },
    "ay-83-c4": {
        "transliteration": "ghara masāna parijana janu bhūtā, suta hita mīta manahuṁ jamadūtā.\nbāganha biṭapa beli kumhilāhīṁ, sarita sarovara dekhi na jāhīṁ.",
        "translation": "Homes seemed like cremation grounds, relatives like ghosts; sons, friends and dear ones seemed like messengers of death.\nIn the gardens, trees and creepers were wilting; the rivers and lakes were a sight too pitiful to behold."
    },
    "ay-83-d": {
        "transliteration": "haya gaya koṭinha kelimṛga purapasu cātaka mora.\npika rathaṁga suka sārikā sārasa haṁsa cakora. 83.",
        "translation": "Horses, elephants, countless pet deer, domestic animals, cuckoos, peacocks,\nkoels, ruddy geese, parrots, mynas, cranes, swans and partridges —"
    },

    # ===== DOHA GROUP 84 =====
    "ay-84-c1": {
        "transliteration": "rāma biyoga bikala saba ṭhāḍhe, jahaṁ tahaṁ manahuṁ citra likhi kāḍhe.\nnagaru saphala banu gahbara bhārī, khaga mṛga bipula sakala nara nārī.",
        "translation": "All stood motionless in their grief of separation from Rama, like painted pictures everywhere.\nThe city had become like a dense, pathless forest, and all the men and women like multitudes of birds and beasts."
    },
    "ay-84-c2": {
        "transliteration": "bidhi kaikeyī kirātinī kīnhī, jēṁhi dava dusaha dasahuṁ disi dīnhī.\nsahi na sake raghubara birahāgī, cale loga saba byākula bhāgī.",
        "translation": "Fate had made Kaikeyi into a tribal huntress who had set an unbearable wildfire blazing in all ten directions.\nUnable to endure the fire of separation from Raghubara, all the people fled in agitation."
    },
    "ay-84-c3": {
        "transliteration": "sabahi bicāra kīnha mana māhīṁ, rāma lakhana siya binu sukhu nāhīṁ.\njahāṁ rāmu tahaṁ sabui samājū, binu raghubīra avadha nahiṁ kājū.",
        "translation": "Everyone resolved in their hearts: 'Without Rama, Lakshmana and Sita, there is no happiness.\nWherever Rama is, there is the whole community; without Raghubira, we have nothing to do in Ayodhya.'"
    },
    "ay-84-c4": {
        "transliteration": "cale sātha asa maṁtru dṛḍhāī, sura durlabha sukha sadana bihāī.\nrāma carana paṁkaja priya jinhahī, biṣaya bhoga basa karahiṁ ki tinhahī.",
        "translation": "With this firm resolve they followed, abandoning homes of comfort that even gods would envy.\nThose to whom Rama's lotus feet are dear — can sense pleasures ever hold them captive?"
    },
    "ay-84-d": {
        "transliteration": "bālaka bṛddha bihāi gṛhaṁ lage loga saba sātha.\ntamasā tīra nivāsu kiya prathama divasa raghunātha. 84.",
        "translation": "Leaving behind only children and the aged at home, all the people followed along.\nOn the first day, the Lord of the Raghus halted on the bank of the Tamasa river."
    },

    # ===== DOHA GROUP 85 =====
    "ay-85-c1": {
        "transliteration": "raghupati prajā premabasa dekhī, sadaya hṛdayaṁ dukhu bhayau biseṣī.\nkarunāmaya raghunātha gosāṁī, begi pāiahiṁ pīra parāī.",
        "translation": "Seeing the people overcome with love, the tender-hearted Lord felt great sorrow.\nThe compassionate Lord Raghunath quickly feels the pain of others."
    },
    "ay-85-c2": {
        "transliteration": "kahi saprema mṛdu bacana suhāe, bahubidhi rāma loga samujhāe.\nkie dharama upadesa ghanere, loga prema basa phirahiṁ na phere.",
        "translation": "Speaking affectionate, gentle and pleasant words, Rama counseled the people in many ways.\nHe gave them abundant teachings on dharma, but overcome by love, they could not be turned back."
    },
    "ay-85-c3": {
        "transliteration": "sīlu sanehu chāḍi nahiṁ jāī, asamaṁjasa basa bhe raghurāī.\nloga soga śrama basa gae soī, kachuka devamāyāṁ mati moī.",
        "translation": "His gracious nature and love for them would not let Him abandon them; the Lord of the Raghus was caught in a dilemma.\nThe people, exhausted from grief and fatigue, fell asleep, their minds also dulled somewhat by divine illusion."
    },
    "ay-85-c4": {
        "transliteration": "jabahiṁ jāma juga jāminī bītī, rāmu saciva sana kaheu saprītī.\nkhoja māri rathu hāṁkahu tātā, āna upāyaṁ banihi nahiṁ bātā.",
        "translation": "When two watches of the night had passed, Rama affectionately said to the minister:\n'Erase the tracks and drive the chariot away, my friend; there is no other way to manage this.'"
    },
    "ay-85-d": {
        "transliteration": "rāma lakhana siya jāna caḍhi saṁbhu carana siru nāi.\nsacivaṁ calāyau turata rathu ita uta khoja durāi. 85.",
        "translation": "Rama, Lakshmana and Sita mounted the chariot, bowing their heads to Lord Shiva.\nThe minister drove the chariot at once, concealing the tracks this way and that."
    },

    # ===== DOHA GROUP 86 =====
    "ay-86-c1": {
        "transliteration": "jāge sakala loga bhaēṁ bhorū, ge raghunātha bhayau ati sorū.\nratha kara khoja katahūṁ nahiṁ pāvahiṁ, rāma rāma kahi cahu disi dhāvahiṁ.",
        "translation": "When all the people awoke at dawn, Raghunath was gone and there was a great uproar.\nThey could find no trace of the chariot anywhere; crying 'Rama! Rama!' they ran in all four directions."
    },
    "ay-86-c2": {
        "transliteration": "manahuṁ bārinidhi būḍa jahājū, bhayau bikala baḍa banika samājū.\nekahi eka dēṁhi upadesū, taje rāma hama jāni kalesū.",
        "translation": "As though a ship had sunk in the ocean, the great company of merchants was distraught.\nThey advised one another: 'Rama has abandoned us, knowing we would cause Him distress.'"
    },
    "ay-86-c3": {
        "transliteration": "niṁdahi āpu sarāhahi mīnā, dhiga jīvanu raghubīra bihīnā.\njau pai priya biyogu bidhi kīnhā, tau kasa maranu na māgēṁ dīnhā.",
        "translation": "They blamed themselves and praised the fish: 'Cursed is life without Raghubira!\nIf God has decreed separation from our beloved, why did He not grant us death when we asked for it?'"
    },
    "ay-86-c4": {
        "transliteration": "ehi bidhi karata pralāpa kalāpā, āe avadha bhare paritāpā.\nbiṣama biyogu na jāi bakhānā, avadhi āsa saba rākhahi prānā.",
        "translation": "Making such piteous laments, they returned to Ayodhya filled with anguish.\nThe terrible separation is beyond description; only hope of the exile's end kept their lives going."
    },
    "ay-86-d": {
        "transliteration": "rāma darasa hita nema brata lage karana nara nāri.\nmanahuṁ koka kokī kamala dīna bihīna tamāri. 86.",
        "translation": "Men and women began observing vows and fasts for the sake of seeing Rama again,\npitiful like chakwa birds, chakwi birds and lotuses deprived of sunlight."
    },

    # ===== DOHA GROUP 87 =====
    "ay-87-c1": {
        "transliteration": "sītā saciva sahita dou bhāī, sṛṁgaberapura pahūṁce jāī.\nutare rāma devasari dekhī, kīnha daṁḍavata haraṣu biseṣī.",
        "translation": "Sita, along with the minister and the two brothers, arrived at Shringaverapur.\nSeeing the divine river Ganga, Rama alighted and prostrated Himself with great delight."
    },
    "ay-87-c2": {
        "transliteration": "lakhana sacivaṁ siyaṁ kie pranāmā, sabahi sahita sukhu pāyau rāmā.\ngaṁga sakala muda maṁgala mūlā, saba sukha karani harani saba sūlā.",
        "translation": "Lakshmana, the minister and Sita also offered their salutations; together with all, Rama felt joy.\nThe Ganga is the source of all delight and blessings — she bestows all happiness and removes all pain."
    },
    "ay-87-c3": {
        "transliteration": "kahi kahi koṭika kathā prasaṁgā, rāmu bilokahiṁ gaṁga taraṁgā.\nsacivahi anujahi priyahi sunāī, bibudha nadī mahimā adhikāī.",
        "translation": "Narrating millions of stories and legends, Rama gazed at the waves of the Ganga.\nHe described to the minister, His younger brother and His beloved the supreme glory of the divine river."
    },
    "ay-87-c4": {
        "transliteration": "majjanu kīnha paṁtha śrama gayaū, suci jalu piata mudita mana bhayaū.\nsumirata jāhi miṭai śrama bhārū, tehi śrama yaha laukika byavahārū.",
        "translation": "They bathed; the fatigue of the journey vanished; drinking the pure water, their hearts were gladdened.\nThis worldly behaviour of showing fatigue is merely a human act for Him whose mere remembrance removes the greatest burdens."
    },
    "ay-87-d": {
        "transliteration": "suddha sacidānaṁdamaya kaṁda bhānukula ketu.\ncarita karata nara anuharata saṁsṛti sāgara setu. 87.",
        "translation": "He who is pure Existence-Consciousness-Bliss embodied, the banner of the Solar dynasty,\nacts in human semblance, building a bridge across the ocean of worldly existence."
    },

    # ===== DOHA GROUP 88 =====
    "ay-88-c1": {
        "transliteration": "yaha sudhi guhaṁ niṣāda jaba pāī, mudita lie priya baṁdhu bolāī.\nlie phala mūla bheṁṭa bhari bhārā, milana caleu hiyaṁ haraṣu apārā.",
        "translation": "When the Nishad chief Guha received this news, he joyfully summoned his dear kinsmen.\nLoading baskets full of fruits and roots as offerings, he set out to meet them with boundless joy in his heart."
    },
    "ay-88-c2": {
        "transliteration": "kari daṁḍavata bheṁṭa dhari āgēṁ, prabhuhi bilokatu ati anurāgēṁ.\nsahaja saneha bibasa raghurāī, pūṁchī kusala nikaṭa baiṭhāī.",
        "translation": "Prostrating himself and placing the offerings before the Lord, he gazed at Him with deep devotion.\nThe Lord of the Raghus, spontaneously moved by his love, asked after his welfare and seated him nearby."
    },
    "ay-88-c3": {
        "transliteration": "nātha kusala pada paṁkaja dekhēṁ, bhayauṁ bhāgabhājana jana lekhēṁ.\ndeva dharani dhanu dhāmu tumhārā, maiṁ janu nīcu sahita parivārā.",
        "translation": "'Lord, all is well now that I have seen Your lotus feet; I am counted among the most fortunate of servants.\nThe earth, wealth and home are all Yours, my Lord; I am but a lowly servant along with my family.'"
    },
    "ay-88-c4": {
        "transliteration": "kṛpā karia pura dhāria pāū, thāpia janu sabu logu sihāū.\nkahehu satya sabu sakhā sujānā, mohi dīnha pitu āyasu ānā.",
        "translation": "'Be gracious and set foot in my town; install Your servant and let all the people rejoice.'\n'You speak truly, O wise friend, but my father has given me a different command.'"
    },
    "ay-88-d": {
        "transliteration": "baraṣa cāridasa bāsu bana muni brata beṣu ahāru.\ngrāma bāsu nahiṁ ucita suni guhahi bhayau dukhu bhāru. 88.",
        "translation": "'For fourteen years I must dwell in the forest, observing a sage's vows, garb and diet.\nIt is not proper for me to stay in a village.' Hearing this, Guha was deeply grieved."
    },

    # ===== DOHA GROUP 89 =====
    "ay-89-c1": {
        "transliteration": "rāma lakhana siya rūpa nihārī, kahahiṁ saprema grāma nara nārī.\nte pitu mātu kahahu sakhi kaise, jinha paṭhae bana bālaka aise.",
        "translation": "Gazing at the beauty of Rama, Lakshmana and Sita, the men and women of the village spoke lovingly:\n'Tell us, friend, what kind of parents are they who sent such young ones to the forest?'"
    },
    "ay-89-c2": {
        "transliteration": "eka kahahiṁ bhala bhūpati kīnhā, loyana lāhu hamahi bidhi dīnhā.\ntaba niṣādapati ura anumānā, taru siṁsupā manohara jānā.",
        "translation": "Some said: 'The king did well — God has granted us the reward of our eyes!'\nThen the Nishad king deliberated in his mind and selected a beautiful shinsupa tree."
    },
    "ay-89-c3": {
        "transliteration": "lai raghunāthahi ṭhāuṁ dekhāvā, kaheu rāma saba bhāṁti suhāvā.\npurajana kari johāru ghara āe, raghubara saṁdhyā karana sidhāe.",
        "translation": "He took Raghunath and showed Him the spot; Rama said it was pleasant in every way.\nThe townspeople paid their respects and went home; Raghubara went to perform His evening worship."
    },
    "ay-89-c4": {
        "transliteration": "guhaṁ saṁvāri sāṁtharī ḍasāī, kusa kisalayamaya mṛdula suhāī.\nsuci phala mūla madhura mṛdu jānī, donā bhari bhari rākhe si pānī.",
        "translation": "Guha prepared and spread a lovely, soft bed of kusha grass and tender leaves.\nKnowing them to be pure and sweet, he arranged soft fruits and roots, and filled leaf-cups brimming with water."
    },
    "ay-89-d": {
        "transliteration": "siya sumaṁtra bhrātā sahita kaṁda mūla phala khāi.\nsayana kīnha raghubaṁsamani pāya paloṭata bhāi. 89.",
        "translation": "Eating roots, tubers and fruits together with Sita, Sumantra and His brother,\nthe jewel of the Raghu dynasty retired to sleep while His brother pressed His feet."
    },

    # ===== DOHA GROUP 90 =====
    "ay-90-c1": {
        "transliteration": "uṭhe lakhanu prabhu sovata jānī, kahi sacivahi sovana mṛdu bānī.\nkachuka dūra saji bāna sarāsana, jāgana lage baiṭhi bīrāsana.",
        "translation": "Lakshmana rose when he knew the Lord was asleep; he gently told the minister to go to sleep.\nSitting a little distance away with bow and arrows ready, he began his vigil seated in a warrior's posture."
    },
    "ay-90-c2": {
        "transliteration": "guhaṁ bolāi pāharū pratītī, ṭhāvaṁ ṭhāṁva rākhe ati prītī.\nāpu lakhana pahiṁ baiṭheu jāī, kaṭi bhāthī sara cāpa caḍhāī.",
        "translation": "Guha called his trusted guards and posted them lovingly at various stations.\nThen he himself went and sat near Lakshmana, with quiver at his waist and bow strung."
    },
    "ay-90-c3": {
        "transliteration": "sovata prabhuhi nihāri niṣādū, bhayau prema basa hṛdayaṁ biṣādū.\ntanu pulakita jalu locana bahaī, bacana saprema lakhana sana kahaī.",
        "translation": "Gazing at the sleeping Lord, the Nishad chief's heart filled with loving sorrow.\nHis body thrilled, tears flowed from his eyes, and he spoke loving words to Lakshmana."
    },
    "ay-90-c4": {
        "transliteration": "bhūpati bhavana subhāyaṁ suhāvā, surapati sadanu na paṭatara pāvā.\nmaṇimaya racita cāru caubāre, janu ratipati nija hātha saṁvāre.",
        "translation": "'The king's palace is naturally so beautiful that even the abode of Indra cannot compare.\nIts lovely upper chambers are inlaid with gems, as if the god of love himself had fashioned them with his own hands.'"
    },
    "ay-90-d": {
        "transliteration": "suci subicitra subhogamaya sumana sugaṁdha subāsa.\npalaṁga mañju manidīpa jahaṁ saba bidhi sakala supāsa. 90.",
        "translation": "'Pure, wondrously decorated and full of luxuries, fragrant with flowers and sweet perfumes,\nwith beautiful beds and jeweled lamps — where every comfort is available in every way.'"
    },

    # ===== DOHA GROUP 91 =====
    "ay-91-c1": {
        "transliteration": "bibidha basana upadhāna turāī, chīra phena mṛdu bisada suhāī.\ntahaṁ siya rāmu sayana nisi karahīṁ, nija chabi rati manoja madu harahīṁ.",
        "translation": "'There, on beds with various garments, pillows and coverlets soft, white and beautiful as the foam of milk,\nSita and Rama would rest at night, Their beauty putting to shame the pride of Rati and Kamadeva.'"
    },
    "ay-91-c2": {
        "transliteration": "te siya rāmu sātharīṁ soe, śramita basana binu jāhi na joe.\nmātu pitā parijana purabāsī, sakhā susīla dāsa aru dāsī.",
        "translation": "'Those same Sita and Rama now sleep on a bed of grass, weary and without proper garments — one cannot bear to look.\nParents, relatives, townspeople, virtuous friends, male and female servants —'"
    },
    "ay-91-c3": {
        "transliteration": "jogavahiṁ jinhahi prāna kī nāīṁ, mahī sovata tei rāma gosāīṁ.\npitā janaka jaga bidita prabhāū, sasura suresa sakhā raghurāū.",
        "translation": "'All who would tend Them as dearly as their own lives — those same Lord Rama sleeps now on the ground.\nHer father is Janaka, famed throughout the world; Her father-in-law is the king of kings, and Her husband's friend is Raghurao.'"
    },
    "ay-91-c4": {
        "transliteration": "rāmacaṁdu pati so baidehī, sovata mahī bidhi bāma na kehī.\nsiya raghubīra ki kānana jogū, karamu pradhāna satya kaha logū.",
        "translation": "'Ramachandra is her husband — that Vaidehi now sleeps on the ground! Against whom is fate not hostile?\nAre Sita and Raghubira suited for the forest? Fate is supreme — truly do people say so.'"
    },
    "ay-91-d": {
        "transliteration": "kaikayanṁdinī maṁdamati kaṭhina kuṭilapanu kīnha.\njehī raghunṁdana jānakihi sukha avasara dukhu dīnha. 91.",
        "translation": "The dull-witted daughter of Kekaya has done a deed of extreme cruelty and wickedness.\nShe has given sorrow to Raghunandana and Janaki at a time when they should have been enjoying happiness."
    },

    # ===== DOHA GROUP 92 =====
    "ay-92-c1": {
        "transliteration": "bhai dinakara kula biṭapa kuṭhārī, kumati kīnha saba bisva dukhārī.\nbhayau biṣādu niṣādahi bhārī, rāma sīya mahī sayana nihārī.",
        "translation": "'She has become an axe to the tree of the Solar dynasty; her evil counsel has brought sorrow to the whole world.'\nSeeing Rama and Sita sleeping on the ground, the Nishad was overwhelmed with grief."
    },
    "ay-92-c2": {
        "transliteration": "bole lakhana madhura mṛdu bānī, gyāna birāga bhagati rasa sānī.\nkāhu na kou sukha dukha kara dātā, nija kṛta karama bhoga sabu bhrātā.",
        "translation": "Lakshmana spoke in a sweet, gentle voice steeped in wisdom, dispassion and devotion:\n'No one gives happiness or sorrow to another, brother; everyone experiences the fruits of their own actions.'"
    },
    "ay-92-c3": {
        "transliteration": "joga biyoga bhoga bhala maṁdā, hita anahita madhyama bhrama phaṁdā.\njanamu maranu jahaṁ lagi jaga jālū, saṁpatī bipati karamu aru kālū.",
        "translation": "'Union and separation, good and bad fortune, friend, foe and neutral — all are snares of delusion.\nBirth and death, the whole web of worldly existence, prosperity and adversity, karma and time —'"
    },
    "ay-92-c4": {
        "transliteration": "dharani dhāmu dhanu pura parivārū, saragu naraku jahaṁ lagi byavahārū.\ndekhia sunia gunia mana māhīṁ, moha mūla paramārathu nāhīṁ.",
        "translation": "'Earth, home, wealth, city, family, heaven, hell — all that constitutes worldly dealings;\nwhatever is seen, heard or contemplated in the mind — all is rooted in delusion and has no ultimate reality.'"
    },
    "ay-92-d": {
        "transliteration": "sapanēṁ hoi bhikhāri nṛpa raṁku nākapati hoi.\njāgēṁ lābhu na hāni kachu timi prapaṁca jiyaṁ joi. 92.",
        "translation": "'A king becomes a beggar in a dream; a pauper becomes the lord of heaven.\nOn waking, there is neither gain nor loss — so should one regard this worldly illusion.'"
    },

    # ===== DOHA GROUP 93 =====
    "ay-93-c1": {
        "transliteration": "asa bicāri nahiṁ kīja rosū, kāhuhi bādi na deia dosū.\nmoha nisāṁ sabu sovanihārā, dekhia sapana aneka prakārā.",
        "translation": "'Reflecting thus, do not be angry; it is useless to blame anyone.\nIn the night of delusion, everyone sleeps and sees dreams of many kinds.'"
    },
    "ay-93-c2": {
        "transliteration": "ehi jaga jāminī jāgahi jogī, paramārathī prapaṁca biyogī.\njānia tabahiṁ jīva jaga jāgā, jaba saba biṣaya bilāsa birāgā.",
        "translation": "'In this night of worldly existence, only yogis remain awake — those devoted to the Supreme Reality and detached from the world.\nKnow that a soul has truly awakened in this world only when it has become completely detached from sensual pleasures.'"
    },
    "ay-93-c3": {
        "transliteration": "hoi bibeku moha bhrama bhāgā, taba raghunātha carana anurāgā.\nsakhā parama paramārathu ehū, mana krama bacana rāma pada nehū.",
        "translation": "'When discrimination arises and the delusion of ignorance flees, then comes devotion to the feet of Raghunath.\nFriend, this is the highest spiritual truth: love for Rama's feet in thought, word and deed.'"
    },
    "ay-93-c4": {
        "transliteration": "rāma brahma paramāratha rūpā, abigata alakha anādi anūpā.\nsakala bikāra rahita gatbhedā, kahi nita neti nirūpahi bedā.",
        "translation": "'Rama is Brahman — the embodiment of the Supreme Reality — unseen, imperceptible, beginningless and incomparable.\nFree from all modifications and beyond all distinctions, the Vedas describe Him only through negation — saying always, not this, not this.'"
    },
    "ay-93-d": {
        "transliteration": "bhagata bhūmi bhūsura surabhī sura hita lāgi kṛpāla.\nkarata carita dhari manuja tanu sunata miṭahi jaga jāla. 93.",
        "translation": "'For the sake of devotees, the earth, Brahmins, cows and gods, the merciful Lord\nassumes a human body and performs divine deeds — hearing which, the bonds of worldly existence are destroyed.'"
    },

    # ===== DOHA GROUP 94 =====
    "ay-94-c1": {
        "transliteration": "sakhā samujhi asa parihari mohū, siya raghubīra carana rata hohū.\nkahata rāma guna bhā bhinusārā, jāge jaga maṁgala sukhadārā.",
        "translation": "'Friend, understanding this, abandon delusion and become devoted to the feet of Sita and Raghubira.'\nAs they were speaking of Rama's virtues, dawn broke; the source of the world's auspiciousness and joy awoke."
    },
    "ay-94-c2": {
        "transliteration": "sakala soca kari rāma nahāvā, suci sujāna baṭa chīra magāvā.\nanuja sahita sira jaṭā banāe, dekhi sumaṁtra nayana jala chāe.",
        "translation": "Completing His morning rituals, Rama bathed; the pure and wise Lord asked for the milk of a banyan tree.\nTogether with His brother, He matted His hair into ascetic locks; seeing this, Sumantra's eyes brimmed with tears."
    },
    "ay-94-c3": {
        "transliteration": "hṛdayaṁ dāhu ati badana malīnā, kaha kara jori bacana ati dīnā.\nnātha kaheu asa kosalanāthā, lai rathu jāhu rāma kēṁ sāthā.",
        "translation": "With a burning heart and a pallid face, he spoke with joined hands in the most piteous words:\n'Lord, the king of Kosala told me thus: take the chariot and go with Rama.'"
    },
    "ay-94-c4": {
        "transliteration": "banu dekhāi surasari anhavāī, ānehu pheri begi dou bhāī.\nlakhanu rāmu siya ānehu pherī, saṁsaya sakala saṁkoca niberī.",
        "translation": "'Show them the forest, bathe them in the Ganga, and bring back both brothers quickly.\nBring Lakshmana, Rama and Sita back, resolving all their doubts and hesitations.'"
    },
    "ay-94-d": {
        "transliteration": "nṛpa asa kaheu gosāīṁ jasa kahai karauṁ bali soi.\nkari binatī pāyanha pareu dīnha bāla jimi roi. 94.",
        "translation": "'The king said this, my Lord — whatever You command, I shall do, I swear.'\nMaking this entreaty, he fell at Rama's feet and wept like a child."
    },

    # ===== DOHA GROUP 95 =====
    "ay-95-c1": {
        "transliteration": "tāta kṛpā kari kījia soī, jātēṁ avadha anātha na hoī.\nmaṁtrahi rāma uṭhāi prabodhā, tāta dharama matu tumha sabu sodhā.",
        "translation": "'Be gracious, father, and do that which will not leave Ayodhya desolate.'\nRama raised the minister up and consoled him: 'Father, you have studied the entire doctrine of dharma.'"
    },
    "ay-95-c2": {
        "transliteration": "sibi dadhīci haricaṁda naresā, sahe dharama hita koṭi kalesā.\nraṁtideva bali bhūpa sujānā, dharamu dhareu sahi saṁkaṭa nānā.",
        "translation": "'Kings like Shibi, Dadhichi and Harishchandra endured millions of afflictions for the sake of dharma.\nThe wise kings Rantideva and Bali upheld dharma by bearing various calamities.'"
    },
    "ay-95-c3": {
        "transliteration": "dharamu na dūsara satya samānā, āgama nigama purāna bakhānā.\nmaiṁ soi dharamu sulabha kari pāvā, tajēṁ tihūṁ pura apajasu chāvā.",
        "translation": "'There is no dharma greater than truth — so declare the Agamas, Vedas and Puranas.\nI have easily obtained this dharma of truthfulness; if I forsake it, infamy will spread across all three worlds.'"
    },
    "ay-95-c4": {
        "transliteration": "saṁbhāvita kahuṁ apajasa lāhū, marana koṭi sama dāruna dāhū.\ntumha sana tāta bahuta kā kahūṁ, diēṁ utaru phiri pātaku lahūṁ.",
        "translation": "'For a person of honor, the acquisition of infamy is as agonizing as ten million deaths.\nWhat more can I say to you, father? If I give a different answer and turn back, I would incur sin.'"
    },
    "ay-95-d": {
        "transliteration": "pitu pada gahi kahi koṭi nati binaya karaba kara jori.\nciṁtā kavanihu bāta kai tāta karia jani mori. 95.",
        "translation": "'Clasp my father's feet and, offering millions of salutations with folded hands, entreat him:\nDo not worry about me on any account whatsoever, dear father.'"
    },

    # ===== DOHA GROUP 96 =====
    "ay-96-c1": {
        "transliteration": "tumha puni pitu sama ati hita morēṁ, binatī karauṁ tāta kara jorēṁ.\nsaba bidhi soi karatabya tumhārēṁ, dukha na pāva pitu soca hamārēṁ.",
        "translation": "'You too are like a father to me, most caring; I entreat you with folded hands, dear sir.\nDo everything in your power so that my father does not suffer sorrow on our account.'"
    },
    "ay-96-c2": {
        "transliteration": "suni raghunātha saciva saṁbādū, bhayau saparijana bikala niṣādū.\npuni kachu lakhana kahī kaṭu bānī, prabhu barajhe baḍa anucita jānī.",
        "translation": "Hearing the exchange between Raghunath and the minister, the Nishad and his family became distraught.\nThen Lakshmana spoke some harsh words, but the Lord stopped him, considering it most improper."
    },
    "ay-96-c3": {
        "transliteration": "sakuci rāma nija sapatha devāī, lakhana saṁdesū kahia jani jāī.\nkaha sumaṁtru puni bhūpa saṁdesū, sahi na sakihi siya bipina kalesū.",
        "translation": "Rama, feeling embarrassed, made Lakshmana swear an oath: 'Do not repeat Lakshmana's message.'\nSumantra then relayed the king's message: 'Sita will not be able to endure the hardships of the forest.'"
    },
    "ay-96-c4": {
        "transliteration": "jehi bidhi avadha āva phiri sīyā, soi raghubarahi tumhahi karanīyā.\nnataru nipaṭa avalaṁba bihīnā, maiṁ na jiaba jimi jala binu mīnā.",
        "translation": "'By whatever means Sita may be brought back to Ayodhya — that is what you and Raghubara must do.\nOtherwise, utterly bereft of support, I shall not live, just as a fish cannot survive without water.'"
    },
    "ay-96-d": {
        "transliteration": "maikēṁ sasarēṁ sakala sukha jabahiṁ jahāṁ manu māna.\ntahaṁ taba rahihi sukhena siya jaba lagi bipati bihāna. 96.",
        "translation": "'At her father's home or her in-laws' — wherever she may be happy, with every comfort,\nSita should stay there contentedly until this time of adversity passes.'"
    },

    # ===== DOHA GROUP 97 =====
    "ay-97-c1": {
        "transliteration": "binatī bhūpa kīnha jehi bhāṁtī, ārati prīti na so kahi jātī.\npitu saṁdesū suni kṛpānidhānā, siyahi dīnha sikha koṭi bidhānā.",
        "translation": "The manner in which the king made his entreaty — that distress and love are beyond words.\nHearing the father's message, the treasury of mercy counseled Sita in millions of ways."
    },
    "ay-97-c2": {
        "transliteration": "sāsu sasura guru priya parivārū, phiratu ta saba kara miṭai khabhārū.\nsuni pati bacana kahati baidehī, sunahu prānapati parama sanehī.",
        "translation": "'If you return, the anxiety of your parents-in-law, guru, and dear family will be removed.'\nHearing her husband's words, Vaidehi replied: 'Listen, O lord of my life, my dearest beloved.'"
    },
    "ay-97-c3": {
        "transliteration": "prabhu karunāmaya parama bibekī, tanu taji rahati chāṁha kimi chēṁkī.\nprabhā jāi kahaṁ bhānu bihāī, kahaṁ caṁdrikā caṁdu taji jāī.",
        "translation": "'You are compassionate and supremely wise, Lord — but can a shadow exist apart from the body it follows?\nWhere can radiance go leaving the sun? Where can moonlight go abandoning the moon?'"
    },
    "ay-97-c4": {
        "transliteration": "patihi premamaya binaya sunāī, kahati saciva sana girā suhāī.\ntumha pitu sasura sarisa hitakārī, utaru deuṁ phiri anucita bhārī.",
        "translation": "Having addressed her husband with a love-filled plea, she spoke pleasant words to the minister:\n'You are as caring as my father and father-in-law; it would be most improper for me to give a contrary reply.'"
    },
    "ay-97-d": {
        "transliteration": "ārati basa sanamukha bhaiuṁ bilagu na mānaba tāta.\nārajasuta pada kamala binu bādi jahāṁ lagi nāta. 97.",
        "translation": "'Compelled by distress I speak face to face; do not take offence, dear sir.\nWithout the lotus feet of the son of the Solar dynasty, all ties are meaningless.'"
    },

    # ===== DOHA GROUP 98 =====
    "ay-98-c1": {
        "transliteration": "pitu baibhava bilāsa maiṁ ḍīṭhā, nṛpa mani mukuṭa milita pada pīṭhā.\nsukhanidāna asa pitu gṛha morēṁ, piya bihīna mana bhāva na bhorēṁ.",
        "translation": "'I have seen my father's splendor and luxury — the crowns of jeweled kings touching his footstool.\nSuch is my father's home, an abode of happiness; yet without my beloved, it does not appeal to my heart even for a moment.'"
    },
    "ay-98-c2": {
        "transliteration": "sasura cakkavaī kosalarāū, bhuvana cāridasa pragaṭa prabhāū.\nāgēṁ hoi jehi surapati leī, aradha siṁghāsana āsanu deī.",
        "translation": "'My father-in-law, the king of Kosala, is a universal emperor whose fame pervades the fourteen worlds.\nBefore whom the king of gods himself comes and offers half his throne as a seat.'"
    },
    "ay-98-c3": {
        "transliteration": "sasuru etādṛsa avadha nivāsū, priya parivāru mātu sama sāsū.\nbinu raghupati pada paduma parāgā, mohi keu sapanēhuṁ sukhada na lāgā.",
        "translation": "'Such is my father-in-law, and Ayodhya is my home; my dear family and mother-in-law is like my own mother.\nYet without the dust of Raghupati's lotus feet, none of this seems pleasant to me even in a dream.'"
    },
    "ay-98-c4": {
        "transliteration": "agama paṁtha banabhūmi pahārā, kari kehari sara sarita apārā.\nkola kirāta kuraṁga bihaṁgā, mohi saba sukhada prānapati saṁgā.",
        "translation": "'Impassable paths, forest lands and mountains, elephants, lions, lakes and boundless rivers,\ntribal people, deer and birds — all are delightful to me in the company of my Lord.'"
    },
    "ay-98-d": {
        "transliteration": "sāsu sasura sana mori huṁti binaya karabi pari pāyaṁ.\nmora socu jani karia kachu maiṁ bana sukhī subhāyaṁ. 98.",
        "translation": "'Please convey my entreaty to my parents-in-law, falling at their feet on my behalf:\nDo not worry about me at all — I am naturally happy in the forest.'"
    },

    # ===== DOHA GROUP 99 =====
    "ay-99-c1": {
        "transliteration": "prānanātha priya devara sāthā, bīra dhurīna dharēṁ dhanu bhāthā.\nnahiṁ maga śramu bhramu dukha mana morēṁ, mohi lagi socu karia jani bhorēṁ.",
        "translation": "'With the lord of my life and my dear brother-in-law, foremost of heroes bearing bow and quiver,\nI feel no fatigue, confusion or sorrow on the path; do not worry about me even for a moment.'"
    },
    "ay-99-c2": {
        "transliteration": "suni sumaṁtru siya sītalī bānī, bhayau bikala janu phani mani hānī.\nnayana sūjha nahiṁ sunai na kānā, kahi na sakai kachu ati akulānā.",
        "translation": "Hearing Sita's cool and composed words, Sumantra became distraught like a serpent that has lost its jewel.\nHis eyes could not see, his ears could not hear, he could not speak — he was utterly overcome with anguish."
    },
    "ay-99-c3": {
        "transliteration": "rāma prabodhu kīnha bahu bhāṁtī, tadapi hotī nahiṁ sītalī chātī.\njatana aneka sātha hita kīnhe, ucita utara raghunṁdana dīnhe.",
        "translation": "Rama consoled him in many ways, yet his heart would not be soothed.\nSumantra made many efforts to persuade them to come along, but Raghunandana gave appropriate responses to each."
    },
    "ay-99-c4": {
        "transliteration": "meṭi jāi nahiṁ rāma rajāī, kaṭhina karama gati kachu na basāī.\nrāma lakhana siya pada siru nāī, phereu banika jimi mūra gavāṁī.",
        "translation": "Rama's will cannot be overturned; the course of fate is harsh and nothing can be done.\nBowing his head at the feet of Rama, Lakshmana and Sita, he turned back like a merchant who has lost his capital."
    },
    "ay-99-d": {
        "transliteration": "ratha hāṁkeu haya rāma tana heri heri hihinahiṁ.\ndekhi niṣāda biṣādabasa dhunahi sīsa pachitāhiṁ. 99.",
        "translation": "He drove the chariot away; the horses kept looking back toward Rama's form and neighing.\nSeeing this, the Nishad people, overcome with sorrow, struck their heads and lamented."
    },

    # ===== DOHA GROUP 100 =====
    "ay-100-c1": {
        "transliteration": "jāsu biyoga bikala pasu aise, prajā mātu pitu jiihahi kaisēṁ.\nbarabasa rāma sumaṁtru paṭhāe, surasari tīra āpu taba āe.",
        "translation": "'When even animals are so distraught at His separation, how will the subjects, mothers and father survive?'\nForcibly Rama sent Sumantra away; then He Himself came to the bank of the Ganga."
    },
    "ay-100-c2": {
        "transliteration": "māgī nāva na kevaṭu ānā, kahai tumhāra maramu maiṁ jānā.\ncarana kamala raja kahuṁ sabu kahaī, mānuṣa karani mūri kachu ahaī.",
        "translation": "He asked for a boat, but the boatman would not bring one. He said: 'I know Your secret.\nEveryone says that the dust of Your lotus feet has some kind of power to transform humans.'"
    },
    "ay-100-c3": {
        "transliteration": "chuata silā bhai nāri suhāī, pāhana tēṁ na kāṭha kaṭhināī.\ntaraniu muni gharini hoi jāī, bāṭa parai morī nāva uḍāī.",
        "translation": "'At the touch of Your feet, a stone became a beautiful woman; wood is not harder than stone.\nMy boat too will turn into a sage's wife and fly away — and my livelihood will be ruined.'"
    },
    "ay-100-c4": {
        "transliteration": "ehi pratipālauṁ sabu parivārū, nahiṁ jānauṁ kachu aura kabārū.\njau prabhu pāra avasi gā cahahū, mohi pada paduma pakhārana kahahū.",
        "translation": "'With this boat I support my entire family; I know no other trade.\nIf You absolutely must cross over, my Lord, then let me wash Your lotus feet first.'"
    },

    # ===== DOHA GROUP 101 =====
    "ay-101-c1": {
        "transliteration": "kṛpāsiṁdhu bole musukāī, soi karu jēṁhi tava nāva na jāī.\nbegi ānu jala pāya pakhārū, hota bilaṁbu utārahi pārū.",
        "translation": "The ocean of mercy smiled and said: 'Do whatever will protect your boat from ruin.\nQuickly bring water and wash My feet; it is getting late — ferry us across.'"
    },
    "ay-101-c2": {
        "transliteration": "jāsu nāma sumirata eka bārā, utarahi nara bhavasiṁdhu apārā.\nsoi kṛpālu kevaṭahi nihorā, jehi jagu kiya tihu pagahu te thorā.",
        "translation": "He whose name, remembered but once, enables mortals to cross the boundless ocean of worldly existence —\nthat same gracious Lord made a humble request to a boatman — He for whom even three steps were too few to span the universe."
    },
    "ay-101-c3": {
        "transliteration": "pada nakha nirakhi devasari haraṣī, suni prabhu bacana mohaṁ mati karaṣī.\nkevaṭa rāma rajāyasu pāvā, pāni kaṭhavatā bhari lei āvā.",
        "translation": "The divine river Ganga rejoiced at the sight of His toenails; hearing the Lord's words, even her wisdom was overpowered by love.\nThe boatman received Rama's command and brought a wooden basin filled with water."
    },
    "ay-101-c4": {
        "transliteration": "ati ānaṁda umagi anurāgā, carana saroja pakhārana lāgā.\nbaraṣi sumana sura sakala sihāhīṁ, ehi sama punyapuṁja kou nāhīṁ.",
        "translation": "Overflowing with supreme delight and love, he began washing the Lord's lotus feet.\nThe gods rained down flowers and envied him: 'There is no one as richly endowed with merit as he.'"
    },
    "ay-101-d": {
        "transliteration": "pada pakhāri jalu pāna kari āpu sahita parivāra.\npitara pāru kari prabhuhi puni mudita gayau lei pāra. 101.",
        "translation": "Washing the Lord's feet, he drank the water himself along with his family,\nthereby liberating his ancestors; then, joyfully, he ferried the Lord across."
    },

    # ===== DOHA GROUP 102 =====
    "ay-102-c1": {
        "transliteration": "utari ṭhāḍa bhae surasari retā, sīyarāmu guha lakhana sametā.\nkevaṭa utari daṁḍavata kīnhā, prabhuhi sakuca ehi nahiṁ kachu dīnhā.",
        "translation": "They alighted and stood on the sandy bank of the Ganga — Sita, Rama, Guha and Lakshmana together.\nThe boatman disembarked and prostrated himself; the Lord felt uneasy that He had nothing to give him."
    },
    "ay-102-c2": {
        "transliteration": "piya hiya kī siya jānanihārī, mani mudarī mana mudita utārī.\nkaheu kṛpāla lehi utarāī, kevaṭa carana gahe akulāī.",
        "translation": "Sita, who knew her beloved's heart, joyfully removed her jeweled ring.\nThe gracious Lord said: 'Take this as your fare.' But the boatman, overwhelmed, clasped His feet."
    },
    "ay-102-c3": {
        "transliteration": "nātha āju maiṁ kāha na pāvā, miṭe doṣa dukha dārida dāvā.\nbahuta kāla maiṁ kīnhi majūrī, āju dīnha bidhi bani bhali bhūrī.",
        "translation": "'Lord, what have I not received today! My sins, sorrows, and the fire of poverty are all extinguished.\nFor a long time I labored as a boatman; today God has given me abundant good fortune.'"
    },
    "ay-102-c4": {
        "transliteration": "aba kachu nātha na cāhia morēṁ, dīnadayāla anugraha torēṁ.\nphiratī bāra mohi je debā, so prasādu maiṁ sira dhari lebā.",
        "translation": "'Now I need nothing more, O Lord, by the grace of You who are kind to the humble.\nWhatever You give me on Your return journey — that blessed gift I shall accept upon my head.'"
    },
    "ay-102-d": {
        "transliteration": "bahuta kīnha prabhu lakhana siyaṁ nahiṁ kachu kevaṭu lei.\nbidā kīnha karunāyatana bhagati bimala baru dei. 102.",
        "translation": "The Lord, Lakshmana and Sita tried much, but the boatman would accept nothing.\nThe abode of compassion bade him farewell, granting him the boon of pure devotion."
    },

    # ===== DOHA GROUP 103 =====
    "ay-103-c1": {
        "transliteration": "taba majjanu kari raghukulanāthā, pūji pārathiva nāyau māthā.\nsiyaṁ surasarihi kaheu kara jorī, mātu manoratha purubi morī.",
        "translation": "Then the Lord of the Raghu dynasty bathed, worshipped a Shiva linga of earth and bowed His head.\nSita, with folded hands, addressed the Ganga: 'O Mother, fulfill my heart's desire.'"
    },
    "ay-103-c2": {
        "transliteration": "pati devara saṁga kusala bahorī, āi karauṁ jehiṁ pūjā torī.\nsuni siya binaya prema rasa sānī, bhai taba bimala bāri bara bānī.",
        "translation": "'When I return safely with my husband and brother-in-law, I shall come and worship you.'\nHearing Sita's plea steeped in the nectar of love, then came a beautiful voice from the pure waters."
    },
    "ay-103-c3": {
        "transliteration": "sunu raghubīra priyā baidehī, tava prabhāu jaga bidita na kehī.\nlokapa hohi bilokatu torēṁ, tohi sevahi saba sidhi kara jorēṁ.",
        "translation": "'Listen, O Vaidehi, beloved of Raghubira — who does not know your glory in the world?\nBy your mere glance one becomes a guardian of the spheres; all supernatural powers serve you with folded hands.'"
    },
    "ay-103-c4": {
        "transliteration": "tumha jo hamahi baḍi binaya sunāī, kṛpā kīnhi mohi dīnhi baḍāī.\ntadapi debī maiṁ debī asīsā, saphala hopana hita nija bāgīsā.",
        "translation": "'That you have addressed me with such a grand entreaty — you have shown me grace and bestowed honor upon me.\nNevertheless, O goddess, I shall give my blessing — to make it fruitful, I employ my own power of speech.'"
    },
    "ay-103-d": {
        "transliteration": "prānanātha devara sahita kusala kosalā āi.\npūjahi saba manakāmanā sujasu rahihi jaga chāi. 103.",
        "translation": "'You shall return safely to Kosala with your lord and brother-in-law.\nYou shall worship me, all your desires shall be fulfilled, and your fair fame shall pervade the world.'"
    },

    # ===== DOHA GROUP 104 =====
    "ay-104-c1": {
        "transliteration": "gaṁga bacana suni maṁgala mūlā, mudita sīya surasari anukūlā.\ntaba prabhu guhahi kaheu ghara jāhū, sunata sūkha mukhu bhā ura dāhū.",
        "translation": "Hearing the Ganga's auspicious words, Sita was delighted that the holy river was favorable to her.\nThen the Lord told Guha: 'Go home now.' Hearing this, Guha's face dried up and his heart burned."
    },
    "ay-104-c2": {
        "transliteration": "dīna bacana guha kaha kara jorī, binaya sunahu raghukulamani morī.\nnātha sātha rahi paṁthu dekhāī, kari dina cāri carana sevakāī.",
        "translation": "In pitiful words, with folded hands, Guha spoke: 'Listen to my entreaty, O jewel of the Raghu dynasty.\nLet me remain with You, show You the way, and serve at Your feet for just four days.'"
    },
    "ay-104-c3": {
        "transliteration": "jehi bana jāi rahaba raghurāī, paranakuṭī maiṁ karabi suhāī.\ntaba mohi kahaṁ jasī deba rajāī, soi karihauṁ raghubīra dohāī.",
        "translation": "'In whichever forest the Lord of the Raghus will stay, I shall build a beautiful leaf-hut.\nThen whatever command You give me, I shall carry it out — I swear by Raghubira.'"
    },
    "ay-104-c4": {
        "transliteration": "sahaja saneha rāma lakhi tāsu, saṁga līnha guha hṛdaya hulāsū.\npuni guhaṁ gyāti boli saba līnhe, kari paritoṣu bidā taba kīnhe.",
        "translation": "Seeing Guha's natural and sincere love, Rama took him along, filling Guha's heart with joy.\nThen Guha called all his kinsmen, satisfied them, and bade them farewell."
    },
    "ay-104-d": {
        "transliteration": "taba ganapati siva sumiri prabhu nāi surasarihi mātha.\nsakhā anuja siyā sahita bana gavanu kīnha raghunātha. 104.",
        "translation": "Then, remembering Ganesh and Shiva and bowing His head to the Ganga,\nthe Lord of the Raghus set out for the forest with His friend, brother and Sita."
    },

    # ===== DOHA GROUP 105 =====
    "ay-105-c1": {
        "transliteration": "tehi dina bhayau biṭapa tara bāsū, lakhana sakhāṁ saba kīnha supāsū.\nprāta prātakṛta kari raghusāī, tīratharāju dīkha prabhu jāī.",
        "translation": "That day they halted under a tree; Lakshmana and the friend (Guha) made all comfortable arrangements.\nAt dawn, after completing His morning rituals, the Lord went and beheld Prayag, the king of pilgrimage sites."
    },
    "ay-105-c2": {
        "transliteration": "saciva satya śraddhā priya nārī, mādhava sarisa mītu hitakārī.\ncāri padāratha bharā bhaṁḍārū, punya pradesa desa ati cāru.",
        "translation": "Truth is Prayag's minister, faith is his beloved wife, and Lord Vishnu is his benevolent friend.\nHis treasury is filled with the four goals of life; he is a region of merit, an exceedingly beautiful land."
    },
    "ay-105-c3": {
        "transliteration": "chetra agama gaḍhu gāḍha suhāvā, sapanēhuṁ nahiṁ pratipacchinha pāvā.\nsenā sakala tīratha bara bīrā, kaluṣa anīka dalana ranadhīrā.",
        "translation": "His territory is inaccessible, his fort formidable and beautiful; not even in dreams have enemies reached it.\nHis army consists of all the finest pilgrimage sites — valiant warriors who are steadfast in crushing the forces of sin."
    },
    "ay-105-c4": {
        "transliteration": "saṁgamu siṁhāsanu suṭhi sohā, chatru akhayabaṭu muni manu mohā.\ncavara jamuna aru gaṁga taraṁgā, dekhi hohi dukha dārida bhaṁgā.",
        "translation": "The Sangam (confluence) serves as his magnificent throne; the immortal banyan tree is his canopy that enchants sages' hearts.\nThe waves of the Yamuna and Ganga are his fly-whisks; beholding them, sorrow and poverty are destroyed."
    },
    "ay-105-d": {
        "transliteration": "sevahi sukṛti sādhu suci pāvahi saba manakāma.\nbaṁdī beda purāna gana kahahi bimala guna grāma. 105.",
        "translation": "The virtuous, saints and the pure-hearted serve him and attain all their desires.\nThe Vedas and Puranas are his bards, proclaiming his spotless host of virtues."
    },

    # ===== DOHA GROUP 106 =====
    "ay-106-c1": {
        "transliteration": "ko kahi sakai prayāga prabhāū, kaluṣa puṁja kuṁjara mṛgarāū.\nasa tīrathapati dekhi suhāvā, sukha sāgara raghubara sukhu pāvā.",
        "translation": "Who can describe the glory of Prayag? He is a lion to the elephant-herd of accumulated sins.\nBeholding such a beautiful lord of pilgrimage sites, the ocean of bliss Raghubara was delighted."
    },
    "ay-106-c2": {
        "transliteration": "kahi siya lakhanahi sakhahi sunāī, śrīmukha tīratharāja baḍāī.\nkari praṇāmu dekhata bana bāgā, kahata mahātamu ati anurāgā.",
        "translation": "Describing the greatness of the king of pilgrimage sites from His own blessed lips, He told Sita, Lakshmana and His friend.\nOffering salutations and viewing the forests and gardens, He spoke of its glories with deep devotion."
    },
    "ay-106-c3": {
        "transliteration": "ehi bidhi āi bilokī benī, sumirata sakala sumaṁgala denī.\nmudita nahāi kīnhi siva sevā, puji jathābidhi tīratha devā.",
        "translation": "In this manner He came and beheld the Triveni confluence, whose very remembrance bestows all auspiciousness.\nBathing joyfully, He worshipped Lord Shiva, and duly honored the deity of the pilgrimage site."
    },
    "ay-106-c4": {
        "transliteration": "taba prabhu bharadvāja pahiṁ āe, karata daṁḍavata muni ura lāe.\nmuni mana moda na kachu kahi jāi, brahmānaṁda rāsi janu pāī.",
        "translation": "Then the Lord went to sage Bharadwaj; as He prostrated Himself, the sage embraced Him.\nThe joy in the sage's heart was beyond description, as though he had obtained a treasure of divine bliss."
    },
    "ay-106-d": {
        "transliteration": "dīnhi asīsa munīsa ura ati anaṁdu asa jāni.\nlocana gocara sukṛta phala manahuṁ kie bidhi āni. 106.",
        "translation": "The great sage gave his blessings, with immense joy in his heart, knowing that\nthe fruits of his good deeds had been brought before his very eyes by the Creator."
    },

    # ===== DOHA GROUP 107 =====
    "ay-107-c1": {
        "transliteration": "kusala prasna kari āsana dīnhe, pūji prema paripūrana kīnhe.\nkanda mūla phala aṁkura nīke, die ānī muni manahuṁ amī ke.",
        "translation": "Asking after their welfare and offering them seats, the sage worshipped them and treated them with complete love.\nHe brought and offered fine roots, tubers, fruits and sprouts — as if they were nectar itself."
    },
    "ay-107-c2": {
        "transliteration": "sīya lakhana jana sahita suhāe, ati ruci rāma mūla phala khāe.\nbhae bigatśrama rāmu sukhāre, bharvdāja mṛdu bacana ucāre.",
        "translation": "Sita, Lakshmana and the attendant (Guha) looked lovely; Rama partook of the roots and fruits with great relish.\nRama's fatigue vanished and He was refreshed; then sage Bharadwaj spoke in gentle words."
    },
    "ay-107-c3": {
        "transliteration": "āju suphala tapu tīratha tyāgū, āju suphala japa joga birāgū.\nsaphala sakala subha sādhana sājū, rāma tumhahi avalokatu ājū.",
        "translation": "'Today my penance, pilgrimages and renunciation have borne fruit; today my chanting, yoga and detachment are rewarded.\nAll my auspicious spiritual practices are fulfilled today — beholding You, O Rama!'"
    },
    "ay-107-c4": {
        "transliteration": "lābha avadhi sukha avadhi na dūjī, tumhārēṁ darasa āsa saba pūjī.\naba kari kṛpā dehu bara ehū, nija pada sarasija sahaja sanehū.",
        "translation": "'The limit of gain and the limit of happiness is nothing else — by Your sight all my hopes are fulfilled.\nNow, be gracious and grant me this boon: spontaneous and natural love for Your lotus feet.'"
    },
    "ay-107-d": {
        "transliteration": "karama bacana mana chāḍi chalu jaba lagi janu na tumhāra.\ntaba lagi sukhu sapanēhuṁ nahīṁ kiēṁ koṭi upacāra.",
        "translation": "'Until one becomes Your servant in thought, word and deed, abandoning all guile,\nthere is no happiness even in dreams, though one may try ten million remedies.'"
    },

    # ===== DOHA GROUP 108 =====
    "ay-108-c1": {
        "transliteration": "suni muni bacana rāmu sakucāne, bhāva bhagati ānaṁda aghāne.\ntaba raghubara muni sujasu suhāvā, koṭi bhāṁti kahi sabahi sunāvā.",
        "translation": "Hearing the sage's words, Rama felt abashed, yet He was satiated with the emotion of devotion and bliss.\nThen Raghubara praised the sage's beautiful fame, extolling it in millions of ways for all to hear."
    },
    "ay-108-c2": {
        "transliteration": "so baḍa so saba guna gana gehū, jehi munīsa tumha ādara dehū.\nmuni raghubīra parasapara navahīṁ, bacana agocara sukhu anubhavahīṁ.",
        "translation": "'He alone is great, he alone is the abode of all virtues, whom you, O great sage, honor.'\nThe sage and Raghubira bowed to each other and experienced a happiness beyond the reach of words."
    },
    "ay-108-c3": {
        "transliteration": "yaha sudhi pāi prayāga nivāsī, baṭu tāpasa muni siddha udāsī.\nbharadvāja āśrama saba āe, dekhana dasaratha suana suhāe.",
        "translation": "Hearing this news, the residents of Prayag — students, ascetics, sages, perfected beings and recluses —\nall came to Bharadwaj's ashram to see the handsome sons of Dasharatha."
    },
    "ay-108-c4": {
        "transliteration": "rāma pranāma kīnha saba kāhū, mudita bhae lahi loyana lāhū.\ndehi asīsa parama sukhu pāī, phire sarāhata suṁdaratāī.",
        "translation": "Rama bowed to every one of them; they were all delighted, having reaped the reward of their eyes.\nReceiving supreme happiness, they gave their blessings and returned, praising His beauty."
    },
    "ay-108-d": {
        "transliteration": "rāma kīnha biśrāma nisī prāta prayāga nahāi.\ncale sahita siya lakhana jana muddita munihi siru nāi. 108.",
        "translation": "Rama rested for the night, bathed at Prayag at dawn,\nand departed with Sita, Lakshmana and the attendant, joyfully bowing His head to the sage."
    },

    # ===== DOHA GROUP 109 =====
    "ay-109-c1": {
        "transliteration": "rāma saprema kaheu muni pāhīṁ, nātha kahia hama kehi maga jāhīṁ.\nmuni mana bihasi rāma sana kahahīṁ, sugama sakala maga tumha kahuṁ ahahīṁ.",
        "translation": "Rama lovingly asked the sage: 'Lord, please tell us which path we should take.'\nThe sage smiled inwardly and said to Rama: 'All paths are easy for You.'"
    },
    "ay-109-c2": {
        "transliteration": "sātha lāgi muni siṣya bolāe, suni mana mudita pacāsaka āe.\nsabanhi rāma para prema apārā, sakala kahahi magu dīkha hamārā.",
        "translation": "To accompany them, the sage summoned his disciples; hearing the call, about fifty came joyfully.\nAll had boundless love for Rama and said: 'This is our path — we have seen the way.'"
    },
    "ay-109-c3": {
        "transliteration": "muni baṭu cāri saṁga taba dīnhe, jinha bahu janama sukṛta saba kīnhe.\nkari pranāmu riṣi āyasu pāī, pramudita hṛdayaṁ cale raghurāī.",
        "translation": "The sage then sent four young students as guides — those who had accumulated great merit over many lifetimes.\nOffering salutations and receiving the sage's permission, the Lord of the Raghus departed with a joyful heart."
    },
    "ay-109-c4": {
        "transliteration": "grāma nikaṭa jaba nikasahi jāī, dekhahi darasu nāri nara dhāī.\nhohi sanātha janama phalu pāī, phirahi dukhita manu saṁga paṭhāī.",
        "translation": "Whenever they passed near a village, men and women would run out to behold them.\nThey felt blessed, having reaped the reward of their birth; then they would return sorrowfully, sending their hearts along with Him."
    },
    "ay-109-d": {
        "transliteration": "bidā kie baṭu binaya kari phire pāi mana kāma.\nutari nahāe jamuna jala jo sarīra sama syāma. 109.",
        "translation": "Bidding farewell to the students with humble words, they returned having fulfilled their heart's desire.\nDescending to the Yamuna, they bathed in its waters, dark as the Lord's own body."
    },

    # ===== DOHA GROUP 110 =====
    "ay-110-c1": {
        "transliteration": "sunata tīravāsī nara nārī, dhāe nija nija kāja bisārī.\nlakhana rāma siya suṁdaratāī, dekhi karahi nija bhāgya baḍāī.",
        "translation": "Hearing the news, the men and women dwelling along the banks ran out, forgetting their own tasks.\nBeholding the beauty of Lakshmana, Rama and Sita, they praised their own good fortune."
    },
    "ay-110-c2": {
        "transliteration": "ati lālasā basahi mana māhīṁ, nāuṁ gāuṁ būjhata sakucāhīṁ.\nje tinha mahuṁ bayabiridha sayāne, tinha kari juguti rāmu pahicāne.",
        "translation": "Great longing dwelt in their hearts, but they hesitated shyly to ask their names and village.\nAmong them, those who were elderly and wise recognized Rama through their discernment."
    },
    "ay-110-c3": {
        "transliteration": "sakala kathā tinha sabahi sunāī, banahi cale pitu āyasu pāī.\nsuni sabiṣāda sakala pachitāhīṁ, rānī rāyaṁ kīnha bhala nāhīṁ.",
        "translation": "They told the whole story to everyone: He has gone to the forest on His father's command.\nHearing this, all lamented with great sorrow: 'The queen and the king have not done well.'"
    },
    "ay-110-c4": {
        "transliteration": "tehi avasara eka tāpasu āvā, tejapuṁja laghubayasa suhāvā.\nkavi alakhita gati beṣu birāgī, mana krama bacana rāma anurāgī.",
        "translation": "At that time, a young ascetic arrived — a mass of spiritual radiance, of tender age and handsome appearance.\nHis movements were unnoticed and his garb was that of a renunciant; in thought, word and deed he was devoted to Rama."
    },
    "ay-110-d": {
        "transliteration": "sajala nayana tana pulaki nija iṣṭadeu pahicāni.\npareu daṁḍa jimi dharanitala dasā na jāi bakhāni. 110.",
        "translation": "His eyes filled with tears, his body thrilled as he recognized his beloved deity.\nHe fell flat on the ground like a staff — his condition is beyond description."
    },

    # ===== DOHA GROUP 111 =====
    "ay-111-c1": {
        "transliteration": "rāma saprema pulaki ura lāvā, parama raṁka janu pārasu pāvā.\nmanahuṁ premu paramārathu doū, milata dhare tana kaha sabu koū.",
        "translation": "Rama lovingly embraced him to His bosom, His body thrilling — as if an utterly destitute man had found the philosopher's stone.\nIt was as though Love and the Supreme Truth had both taken bodily form and were meeting, everyone said."
    },
    "ay-111-c2": {
        "transliteration": "bahuri lakhana pāyanha soi lāgā, līnha uṭhāi umagi anurāgā.\npuni siya carana dhūri dhari sīsā, jananī jāni sisu dīnhi asīsā.",
        "translation": "Then the ascetic fell at Lakshmana's feet; Lakshmana raised him, overflowing with love.\nThen he placed the dust of Sita's feet on his head; knowing him as a child, she blessed him like a mother."
    },
    "ay-111-c3": {
        "transliteration": "kīnha niṣāda daṁḍavata tehī, mileu mudita lakhi rāma sanehī.\npiata nayana puṭa rūpu piyūṣā, mudita suasanu pāi jimi bhūkhā.",
        "translation": "The Nishad chief also prostrated before him; the ascetic met him gladly, seeing him as a lover of Rama.\nDrinking in the nectar of Rama's beauty with his eyes, he was as delighted as a hungry man who receives delicious food."
    },
    "ay-111-c4": {
        "transliteration": "te pitu mātu kahahu sakhi kaise, jinha paṭhae bana bālaka aise.\nrāma lakhana siya rūpu nihārī, hohi saneha bikala nara nārī.",
        "translation": "'Tell us, friend, what kind of parents are they who sent such young ones to the forest?'\nGazing at the beauty of Rama, Lakshmana and Sita, the men and women were overwhelmed with tender emotion."
    },
    "ay-111-d": {
        "transliteration": "taba raghubīra aneka bidhi sakhahi sikhāvanu dīnha.\nrāma rajāyasu sīsa dhari bhavana gavanu tēṁiṁ kīnha. 111.",
        "translation": "Then Raghubira gave many kinds of counsel to His friend (the ascetic).\nPlacing Rama's command upon his head, the friend departed for his home."
    },

    # ===== DOHA GROUP 112 =====
    "ay-112-c1": {
        "transliteration": "puni siyaṁ rāma lakhana kara jorī, jamunahi kīnha pranāmu bahorī.\ncale sasīya mudita dou bhāī, rabitanujā kai karata baḍāī.",
        "translation": "Then Sita, Rama and Lakshmana, with folded hands, offered their salutations to the Yamuna.\nThe two brothers proceeded joyfully with Sita, praising the daughter of the Sun (Yamuna)."
    },
    "ay-112-c2": {
        "transliteration": "pathika aneka milahi maga jātā, kahahi saprema dekhi dou bhrātā.\nrāja lakhana saba aṁga tumhārēṁ, dekhi socu ati hṛdaya hamārēṁ.",
        "translation": "Many travelers met them on the way and spoke with affection upon seeing the two brothers:\n'Every feature of Yours speaks of royalty, O Lakshmana; seeing You, our hearts are filled with great anxiety.'"
    },
    "ay-112-c3": {
        "transliteration": "māraga calahu payādehi pāēṁ, jyotiṣu jhūṭha hamārēṁ bhāēṁ.\nagamu paṁtha giri kānana bhārī, tehi mahaṁ sātha nāri sukumārī.",
        "translation": "'You walk along the road barefoot; astrology is false, it seems to us.\nThe path ahead is impassable — with great mountains and dense forests — and with You is a delicate woman.'"
    },
    "ay-112-c4": {
        "transliteration": "kari kehari bana jāi na joī, hama saṁga calahi jo āyasu hoī.\njāba jahaṁ lagi tahaṁ pahūṁcāī, phiraba bahori tumhahi siru nāī.",
        "translation": "'The forest is filled with elephants and lions — one cannot even look at it. Let us go with You, if You permit.\nWe will escort You as far as You go, and then return, bowing our heads to You.'"
    },
    "ay-112-d": {
        "transliteration": "ehi bidhi pūṁchahi prema basa pulaka gāta jalu naina.\nkṛpāsiṁdhu pherahi tinhahi kahi binīta mṛdu baina. 112.",
        "translation": "In this way they inquired, overcome by love, with thrilling limbs and tearful eyes.\nThe ocean of mercy sent them back, speaking humble and gentle words."
    },

    # ===== DOHA GROUP 113 =====
    "ay-113-c1": {
        "transliteration": "je pura gāṁva basahi maga māhīṁ, tinhahi nāga sura nagara sihāhīṁ.\nkehi sukṛtīṁ kehi gharīṁ basāe, dhanya punyamaya parama suhāe.",
        "translation": "The cities and villages that lay along their path — even the serpent-world and celestial cities envied them.\n'By what meritorious one and at what auspicious hour were these blessed, holy and supremely beautiful places founded?'"
    },
    "ay-113-c2": {
        "transliteration": "jahaṁ jahaṁ rāma carana cali jāhīṁ, tinha samāna amarāvati nāhīṁ.\npunyapuṁja maga nikaṭa nivāsī, tinhahi sarāhahi surapuravāsī.",
        "translation": "'Wherever Rama's feet tread, even Amaravati (Indra's city) cannot compare with those places.\nThose supremely meritorious souls who dwell along the path — the residents of heaven themselves praise them.'"
    },
    "ay-113-c3": {
        "transliteration": "je bhari nayana bilokahi rāmahi, sītā lakhana sahita ghanaśyāmahi.\nje sara sarita rāma avagāhahi, tinhahi deva sara sarita sarāhahi.",
        "translation": "'Those who gaze at Rama with eyes full of love — at the dark-complexioned Lord with Sita and Lakshmana —\nthe lakes and rivers in which Rama bathes — the celestial lakes and rivers praise them.'"
    },
    "ay-113-c4": {
        "transliteration": "jehi taru tara prabhu baiṭhahi jāī, karahi kalpataru tāsu baḍāī.\nparasi rāma pada paduma parāgā, mānati bhūmi bhūri nija bhāgā.",
        "translation": "'Whatever tree the Lord sits under — even the wish-fulfilling tree sings its praises.\nTouching the pollen of Rama's lotus feet, the earth considers her fortune immense.'"
    },
    "ay-113-d": {
        "transliteration": "chāṁha karahi ghana bibudhagana baraṣahi sumana sihāhi.\ndekhata giri bana bihaga mṛga rāmu cale maga jāhi. 113.",
        "translation": "The gods form clouds to provide shade, rain down flowers and look on with envy,\nas Rama walks along the path, beholding mountains, forests, birds and deer."
    },

    # ===== DOHA GROUP 114 =====
    "ay-114-c1": {
        "transliteration": "sītā lakhana sahita raghurāī, gāṁva nikaṭa jaba nikasahi jāī.\nsuni saba bāla bṛddha nara nārī, calahi turata gṛhakāju bisārī.",
        "translation": "Whenever the Lord of the Raghus, with Sita and Lakshmana, passed near a village,\nall — children, the old, men and women — would rush out at once, forgetting their household tasks."
    },
    "ay-114-c2": {
        "transliteration": "rāma lakhana siya rūpa nihārī, pāi nayanaphalu hohi sukhārī.\nsajala bilocana pulaka sarīrā, saba bhae magana dekhi dou bīrā.",
        "translation": "Beholding the beauty of Rama, Lakshmana and Sita, they gained the reward of their eyes and were overjoyed.\nWith tearful eyes and thrilling bodies, all were enraptured at the sight of the two heroes."
    },
    "ay-114-c3": {
        "transliteration": "barani na jāi dasā tinha kerī, lahi janu raṁkanha suramani ḍherī.\nekanhi eka boli sikha dehīṁ, locana lāhu lehu chana ehīṁ.",
        "translation": "Their condition cannot be described — as if paupers had found heaps of celestial gems.\nThey called to one another and gave counsel: 'Seize this moment — take the reward of your eyes right now!'"
    },
    "ay-114-c4": {
        "transliteration": "rāmahi dekhi eka anurāge, citavata cale jāhi saṁga lāge.\neka nayana maga chabi ura ānī, hohi sithila tana mana bara bānī.",
        "translation": "Some, enamored upon seeing Rama, walked along staring, following Him.\nOthers stored His beauty in their hearts through the path of their eyes, and became motionless in body, mind and speech."
    },
    "ay-114-d": {
        "transliteration": "eka dekhiṁ baṭa chāṁha bhalī ḍāsi mṛdula tṛna pāta.\nkahahi gavāṁia chinuku śramu gavanaba abahiṁ ki prāta. 114.",
        "translation": "Some, seeing the good shade of a banyan tree, spread soft grass and leaves beneath it.\nThey said: 'Rest here a moment and relieve Your fatigue — will You proceed now or wait till morning?'"
    },

    # ===== DOHA GROUP 115 =====
    "ay-115-c1": {
        "transliteration": "eka kalasa bhari ānahi pānī, aṁcaia nātha kahahi mṛdu bānī.\nsuni priya bacana prīti ati dekhī, rāma kṛpāla susīla biseṣī.",
        "translation": "Some brought a full pitcher of water, saying in gentle words: 'Please drink, Lord.'\nHearing their loving words and seeing their intense affection, the gracious and supremely virtuous Rama was moved."
    },
    "ay-115-c2": {
        "transliteration": "jānī śramita sīya mana māhīṁ, gharika bilaṁbu kīnha baṭa chāhīṁ.\nmudita nāri nara dekhahi sobhā, rūpa anūpa nayana manu lobhā.",
        "translation": "Knowing in His heart that Sita was tired, He paused briefly under the shade of a banyan tree.\nThe delighted men and women gazed at His splendor — His incomparable beauty captivated their eyes and minds."
    },
    "ay-115-c3": {
        "transliteration": "ekaṭaka saba sohahi cahuṁ orā, rāmacaṁdra mukha caṁda cakorā.\ntaruna tamāla barana tanu sohā, dekhata koṭi madana manu mohā.",
        "translation": "All sat gazing unblinkingly in every direction — like partridges fixed upon the moon of Ramachandra's face.\nHis body shone with the complexion of a young tamala tree; His sight could enchant the hearts of ten million Cupids."
    },
    "ay-115-c4": {
        "transliteration": "dāmini barana lakhana suṭhi nīke, nakha sikha subhaga bhāvate jī ke.\nmunipata kaṭinha kasēṁ tūnīrā, sohahi kara kamalinī dhanu tīrā.",
        "translation": "Lakshmana, fair as lightning, looked extremely handsome — lovely from head to toe and dear to everyone's heart.\nClad in hermit garb with quivers fastened at the waist, their lotus hands holding bows and arrows looked resplendent."
    },
    "ay-115-d": {
        "transliteration": "jaṭā mukuṭa sīsani subhaga ura bhuja nayana bisāla.\nsarada paraba bidhu badana bara lasata sveda kana jāla. 115.",
        "translation": "With beautiful crowns of matted locks upon Their heads, broad chests, mighty arms and large eyes,\nTheir lovely faces shone like the full autumn moon, glistening with a network of tiny beads of perspiration."
    },

    # ===== DOHA GROUP 116 =====
    "ay-116-c1": {
        "transliteration": "barani na jāi manohara jorī, sobhā bahuta thorī mati morī.\nrāma lakhana siya suṁdaratāī, saba citavahi cita mana mati lāī.",
        "translation": "The enchanting pair is beyond description; Their beauty is vast and my wit is small.\nAll gazed at the loveliness of Rama, Lakshmana and Sita, their hearts, minds and intellects fully absorbed."
    },
    "ay-116-c2": {
        "transliteration": "thake nāri nara prema piāse, manahuṁ mṛgī mṛga dekhi diā se.\nsīya samīpa grāmatiya jāhīṁ, pūṁchata ati sanēhaṁ sakucāhīṁ.",
        "translation": "The men and women were weary yet thirsting for love, like deer and does drawn to a light.\nThe village women approached Sita, but hesitated shyly even as they asked their questions."
    },
    "ay-116-c3": {
        "transliteration": "bāra bāra saba lāgahi pāēṁ, kahahi bacana mṛdu sarala subhāēṁ.\nrājakumāri binaya hama karahīṁ, tiya subhāyaṁ kachu pūṁchata ḍarahīṁ.",
        "translation": "Again and again they all touched her feet, speaking words that were soft, simple and sweet-natured.\n'O princess, we make this humble request, but being women, we are afraid to ask anything.'"
    },
    "ay-116-c4": {
        "transliteration": "svāminī abinaya chamabi hamārī, bilagu na mānaba jāni gavāṁrī.\nrājakuaṁra dou sahaja salone, inha tēṁ lahī duti marakata sone.",
        "translation": "'O mistress, forgive our impertinence; do not be offended, knowing us to be rustic women.\nBoth these princes are naturally handsome — from Them comes the radiance of emerald and gold.'"
    },
    "ay-116-d": {
        "transliteration": "syāmala gaura kisora bara suṁdara suṣamā aina.\nsarada sarbarīnātha mukhu sarada saroruha naina. 116.",
        "translation": "'The dark and fair youths are supremely handsome, the very embodiment of beauty.\nTheir faces are like the autumn full moon, and Their eyes are like autumnal lotus flowers.'"
    },

    # ===== DOHA GROUP 117 =====
    "ay-117-c1": {
        "transliteration": "koṭi manoja lajāvanihāre, sumukhi kahahu ko āhi tumhāre.\nsuni sanehamaya mañjula bānī, sakucī siya mana mahuṁ musukānī.",
        "translation": "'They can put tens of millions of Cupids to shame — tell us, O beautiful one, who are They to you?'\nHearing their affectionate and charming words, Sita felt shy and smiled within her heart."
    },
    "ay-117-c2": {
        "transliteration": "tinhahi biloki bilokati dharanī, duhuṁ sakoca sakucita barabaranī.\nsakuci saprema bāla mṛga nayanī, bolī madhura bacana pikabanaī.",
        "translation": "Looking at them and then looking at the ground, embarrassed by both kinds of shyness, the beautiful lady hesitated.\nThen the modest, loving, doe-eyed one spoke in sweet words with a cuckoo's voice."
    },
    "ay-117-c3": {
        "transliteration": "sahaja subhāya subhaga tana gore, nāmu lakhanu laghu devara more.\nbahuri badanu bidhu aṁcala ḍhāṁkī, piya tana citai bhauṁha kari bāṁkī.",
        "translation": "'The one who is naturally fair and handsome in form — his name is Lakshmana, my younger brother-in-law.'\nThen she veiled her moonlike face with her garment and glanced toward her beloved's form with arched eyebrows."
    },
    "ay-117-c4": {
        "transliteration": "khañjana mañju tirīche nayanani, nija pati kaheu tinhahi siyaṁ sayanani.\nbhai mudita saba grāmabadhūṭīṁ, raṁkanha rāya rāsi janu lūṭīṁ.",
        "translation": "With beautiful, sidelong, wagtail-like glances, Sita indicated to them that He was her husband.\nAll the village women were overjoyed, as if paupers had plundered a king's treasure."
    },
    "ay-117-d": {
        "transliteration": "ati saprema siya pāyaṁ pari bahubidhi dehi asīsa.\nsadā sohāgini hohu tumha jaba lagi mahī ahi sīsa. 117.",
        "translation": "With deep love they fell at Sita's feet and gave many blessings:\n'May you forever be a happily married woman, as long as the earth rests upon the serpent's head.'"
    },

    # ===== DOHA GROUP 118 =====
    "ay-118-c1": {
        "transliteration": "pārabatī sama patipriya hohū, debī na hama para chāḍaba chohū.\npuni puni binaya karia kara jorī, jauṁ ehi māraga phiria bahorī.",
        "translation": "'May you be as dear to your husband as Parvati; O goddess, do not withdraw your grace from us.\nWe entreat you again and again with folded hands: if you pass this way again on your return,'"
    },
    "ay-118-c2": {
        "transliteration": "darasanu deba jāni nija dāsī, lakhīṁ sīyaṁ saba prema piāsī.\nmadhura bacana kahi kahi paritoṣīṁ, janu kumudīnīṁ kaumudīṁ poṣīṁ.",
        "translation": "'grant us your sight, knowing us as your servants.' Sita saw that all were thirsting for love.\nShe consoled them by speaking sweet words, like moonlight nurturing night-lilies."
    },
    "ay-118-c3": {
        "transliteration": "tabahiṁ lakhana raghubara rukha jānī, pūṁcheu magu loganha mṛdu bānī.\nsunata nāri nara bhae dukhārī, pulakita gāta bilocana bārī.",
        "translation": "Just then Lakshmana, understanding Raghubara's wish, asked the people for directions in a gentle voice.\nHearing this, the men and women became sorrowful, with thrilling bodies and tearful eyes."
    },
    "ay-118-c4": {
        "transliteration": "miṭā modu mana bhae malīne, bidhi nidhi dīnha leta janu chīne.\nsamujhi karama gati dhīraju kīnhā, sodhi sugama magu tinha kahi dīnhā.",
        "translation": "Their joy vanished; their hearts became heavy — as if God had given a treasure and was now snatching it away.\nResigning themselves to the course of fate, they gathered courage and, having found an easy route, described it to them."
    },
    "ay-118-d": {
        "transliteration": "lakhana jānakī sahita taba gavanu kīnha raghunātha.\npheré saba priya bacana kahi lie lāi mana sātha. 118.",
        "translation": "Then Raghunath proceeded with Lakshmana and Janaki.\nHe sent everyone back with loving words, taking their hearts along with Him."
    },

    # ===== DOHA GROUP 119 =====
    "ay-119-c1": {
        "transliteration": "phirata nāri nara ati pachitāhīṁ, deahi doṣu dehi mana māhīṁ.\nsahita biṣāda parasapara kahahīṁ, bidhi karataba ulaṭe saba ahahīṁ.",
        "translation": "As the men and women turned back, they deeply regretted it, blaming fate in their hearts.\nWith great sorrow they said to one another: 'All the works of the Creator are upside down.'"
    },
    "ay-119-c2": {
        "transliteration": "nipaṭa niraṁkusu niṭhura nisaṁkū, jehi sasi kīnha saruja sakalaṁkū.\nrūkha kalpataru sāgaru khārā, tehi paṭhae bana rājakumārā.",
        "translation": "'He is utterly unbridled, merciless and fearless — He who made the moon diseased and blemished.\nHe made the wish-fulfilling tree fruitless and the ocean salty — that same Creator has sent these princes to the forest.'"
    },
    "ay-119-c3": {
        "transliteration": "jauṁ pe inhahi dīnha banabāsū, kīnha bādi bidhi bhoga bilāsū.\ne bicarahi maga binu padatrānā, race bādi bidhi bāhana nānā.",
        "translation": "'If He has given Them forest exile, then the Creator made all luxuries and pleasures in vain.\nThey walk the road without footwear — the Creator made various vehicles for nothing.'"
    },
    "ay-119-c4": {
        "transliteration": "e mahī parahi ḍāsi kusa pātā, subhaga seja kata sṛjata bidhātā.\ntarubara bāsa inhahi bidhi dīnhā, dhavala dhāma raci raci śramu kīnhā.",
        "translation": "'They lie on the ground on a spread of kusha grass and leaves — why then did the Creator fashion lovely beds?\nThe Creator has given Them a dwelling under trees — He labored in vain building grand white mansions.'"
    },

    # ===== DOHA GROUP 120 =====
    "ay-120-c1": {
        "transliteration": "jauṁ e kaṁda mūla phala khāhīṁ, bādi sudhādi asana jaga māhīṁ.\neka kahahi e sahaja suhāe, āpu pragaṭa bhae bidhi na banāe.",
        "translation": "'If They eat roots, tubers and fruits, then ambrosia and all other foods in the world are useless.'\nSome said: 'They are naturally beautiful — They have manifested on Their own; the Creator did not fashion Them.'"
    },
    "ay-120-c2": {
        "transliteration": "jahaṁ lagi beda kahī bidhi karanī, śravana nayana mana gocara baranī.\ndekhahu khoji bhuaṁna dasa cārī, kahaṁ asa puruṣa kahāṁ asi nārī.",
        "translation": "'All of the Creator's work described in the Vedas, all that can be perceived by ears, eyes and mind —\nsearch throughout the fourteen worlds and see: where is such a man, and where is such a woman?'"
    },
    "ay-120-c3": {
        "transliteration": "inhahi dekhi bidhi manu anurāgā, paṭatara joga banāvai lāgā.\nkīnha bahuta śrama aika na āe, tehi iriṣā bana āni durāe.",
        "translation": "'Seeing Them, the Creator's heart was smitten with love, and he tried to make someone comparable.\nDespite great effort, not one matched Them — so out of jealousy he brought Them and hid Them in the forest.'"
    },
    "ay-120-c4": {
        "transliteration": "eka kahahi hama bahuta na jānahiṁ, āpuhi parama dhanya kari mānahiṁ.\nte puni punyapuṁja hama lekhe, je dekahiṁ dekhihahi jinha dekhe.",
        "translation": "Some said: 'We do not know much; we consider ourselves supremely blessed.\nAnd we reckon those too as great stores of merit who have seen Them, who will see Them, and who have already seen Them.'"
    },
    "ay-120-d": {
        "transliteration": "ehi bidhi kahi kahi bacana priya lehi nayana bhari nīra.\nimi calihahi māraga agama suṭhi sukumāra sarīra. 120.",
        "translation": "Speaking such loving words, their eyes brimming with tears, they would say:\n'How will They walk on this impassable path with such exceedingly delicate bodies?'"
    },

    # ===== DOHA GROUP 121 =====
    "ay-121-c1": {
        "transliteration": "nāri saneha bikala basa hohīṁ, cakaī sāṁjha samaya janu sohīṁ.\nmṛdu pada kamala kaṭhina magu jānī, gahbari hṛdayaṁ kahahi bara bānī.",
        "translation": "The women, overcome by affection, became distraught — like chakwi birds at eventide.\nKnowing the lotus feet to be soft and the path to be hard, they said with anxious hearts in choice words:"
    },
    "ay-121-c2": {
        "transliteration": "parasata mṛdula carana arunāre, sakucati mahī jimi hṛdaya hamāre.\njauṁ jagadīsa inhahi banu dīnhā, kasa na sumanamaya māragu kīnhā.",
        "translation": "'At the touch of those soft, reddish feet, the earth herself shrinks back, just as our hearts do.\nIf the Lord of the universe has given Them forest exile, why did He not make the path of flowers?'"
    },
    "ay-121-c3": {
        "transliteration": "jauṁ māgā pāia bidhi pāhīṁ, e rakhiahiṁ sakhi āṁkhinha māhīṁ.\nje nara nāri na avasara āe, tinha siya rāmu na dekhana pāe.",
        "translation": "'If one could get what one asks from the Creator, we would keep Them, my friend, enshrined in our eyes forever.'\nThose men and women who did not come in time could not see Sita and Rama."
    },
    "ay-121-c4": {
        "transliteration": "suni surūpa būjhahi akulāī, aba lagi gae kahāṁ lagi bhāī.\nsamaratha dhāi bilokahi jāī, pramudita phirahi janamaphalu pāī.",
        "translation": "Hearing of Their beauty, they would inquire anxiously: 'How far have They gone by now, brother?'\nThose who were able would run and go see Them, and return delighted, having reaped the fruit of their birth."
    },
    "ay-121-d": {
        "transliteration": "abalā bālaka bṛddha jana kara mījahi pachitāhi.\nhohi premabasa loga imi rāmu jahāṁ jahaṁ jāhi. 121.",
        "translation": "Women, children and the elderly wrung their hands in regret.\nWherever Rama went, the people were thus overcome with love."
    },

    # ===== DOHA GROUP 122 =====
    "ay-122-c1": {
        "transliteration": "gāṁva gāṁva asa hoi anaṁdū, dekhi bhānukula kairava caṁdū.\nje kachu samācāra suni pāvahi, te nṛpa rānihi dosu lagāvahi.",
        "translation": "In village after village there was such bliss at beholding the moon of the Solar dynasty, who is like moonlight to the lily.\nThose who heard any news would blame the king and queen."
    },
    "ay-122-c2": {
        "transliteration": "kahahi eka ati bhala naranāhū, dīnha hamahi joi locana lāhū.\nkahahi paraspara loga logāīṁ, bātēṁ sarala saneha suhāīṁ.",
        "translation": "Some would say: 'The king has done very well — he has given us the reward of our eyes.'\nThe men and women said to one another in simple, affectionate and delightful words:"
    },
    "ay-122-c3": {
        "transliteration": "te pitu mātu dhanya jinha jāe, dhanya so nagaru jahāṁ tēṁ āe.\ndhanya so desu sailu bana gāūṁ, jahaṁ jahaṁ jāhi dhanya soi ṭhāūṁ.",
        "translation": "'Blessed are the parents who gave Them birth; blessed is the city from which They come.\nBlessed is that country, that mountain, that forest and that village; wherever They go, blessed is that place.'"
    },
    "ay-122-c4": {
        "transliteration": "sukha pāyau biraṁci raci tehī, e jehi ke saba bhāṁti snehī.\nrāma lakhana pathi kathā suhāī, rahī sakala maga kānana chāī.",
        "translation": "'The Creator attained bliss by creating the one who is beloved to Them in every way.'\nThe charming tale of Rama and Lakshmana's journey spread throughout all the roads and forests."
    },
    "ay-122-d": {
        "transliteration": "ehi bidhi raghukula kamala rabi maga loganha sukha deta.\njāhi cale dekhata bipina siya saumitri sameta. 122.",
        "translation": "In this way, the sun to the lotus of the Raghu dynasty, giving happiness to people along the way,\nproceeded onward, viewing the forests, with Sita and Lakshmana."
    },

    # ===== DOHA GROUP 123 =====
    "ay-123-c1": {
        "transliteration": "āge rāmu lakhanu bane pāchēṁ, tāpasa beṣa birājata kāchēṁ.\nubhaya bīca siya sohati kaise, brahma jīva bica māyā jaise.",
        "translation": "Rama walked in front and Lakshmana behind, both resplendent in their ascetic garb.\nBetween them Sita shone — just as Maya (the divine illusion) stands between Brahman and the individual soul."
    },
    "ay-123-c2": {
        "transliteration": "bahuri kahauṁ chabi jasī mana basaī, janu madhu madana madhya rati lasaī.\nupamā bahuri kahauṁ jiyaṁ johī, janu budha bidhu bica rohinī sohī.",
        "translation": "Let me describe Their beauty as it dwells in my heart: as if Rati shines between Spring and the god of Love.\nAnother comparison that comes to my mind: as if Rohini is adorned between Mercury and the Moon."
    },
    "ay-123-c3": {
        "transliteration": "prabhu pada rekha bīca bica sītā, dharati carana maga calatī sabhītā.\nsīya rāma pada aṁka barāēṁ, lakhana calahi magu dāhina lāēṁ.",
        "translation": "Sita walked in between the Lord's footprints, timidly placing her feet on the path.\nSita walked measuring her steps within Rama's footprints, while Lakshmana walked keeping to the right side of the path."
    },
    "ay-123-c4": {
        "transliteration": "rāma lakhana siya prīti suhāī, bacana agocara kimi kahi jāī.\nkhaga mṛga magana dekhi chabi hohīṁ, lie corī cita rāma baṭohīṁ.",
        "translation": "The beautiful love between Rama, Lakshmana and Sita is beyond words — how can it be described?\nBirds and beasts became enraptured seeing Their beauty; Rama as a wayfarer stole everyone's heart."
    },
    "ay-123-d": {
        "transliteration": "jinha jinha dekhe pathika priya siya sameta dou bhāi.\nbhava magu agamu anaṁdu tei binu śrama rahe sirāi. 123.",
        "translation": "All those dear travelers who beheld Sita with the two brothers —\nfor them the impassable path of worldly existence was effortlessly traversed to its end."
    },

    # ===== DOHA GROUP 124 =====
    "ay-124-c1": {
        "transliteration": "ajahuṁ jāsu ura sapanēhuṁ kāū, basahuṁ lakhanu siya rāmu baṭāū.\nrāma dhāma patha pāihi soī, jo patha pāva kabahūṁ muni koī.",
        "translation": "Even now, in whose heart Lakshmana, Sita and Rama as wanderers dwell, even in a dream,\nthat person shall find the path to Rama's abode — a path that some rare sage may attain."
    },
    "ay-124-c2": {
        "transliteration": "taba raghubīra śramita siya jānī, dekhi nikaṭa baṭu sītala pānī.\ntahaṁ basi kaṁda mūla phala khāī, prāta nahāi cale raghurāī.",
        "translation": "Then Raghubira, knowing Sita was tired, spotted a banyan tree nearby with cool water.\nThey rested there, ate roots, tubers and fruits, and the Lord of the Raghus departed at dawn after bathing."
    },
    "ay-124-c3": {
        "transliteration": "dekhata bana sara saila suhāe, bālamīki āśrama prabhu āe.\nrāma dīkha muni bāsu suhāvana, suṁdara giri kānanu jalu pāvana.",
        "translation": "Beholding the beautiful forests, lakes and mountains, the Lord arrived at Valmiki's ashram.\nRama beheld the sage's pleasant abode — lovely hills, forests and pure water."
    },
    "ay-124-c4": {
        "transliteration": "sarani saroja biṭapa bana phūle, guṁjata mañju madhupa rasa bhūle.\nkhaga mṛga bipula kolāhala karahīṁ, birahita baira mudita mana carahīṁ.",
        "translation": "Rows of lotuses and trees in the forest were in bloom; beautiful bees hummed, intoxicated with nectar.\nCountless birds and beasts made a joyful clamor, roaming happily with hearts free from enmity."
    },
    "ay-124-d": {
        "transliteration": "suci suṁdara āśramu nirakhi haraṣe rājivanena.\nsuni raghubara āgamanu muni āgēṁ āyau lena. 124.",
        "translation": "Beholding the pure and beautiful ashram, the lotus-eyed Lord was delighted.\nHearing of Raghubara's arrival, the sage came forward to receive Him."
    },

    # ===== DOHA GROUP 125 =====
    "ay-125-c1": {
        "transliteration": "muni kahuṁ rāma daṁḍavata kīnhā, āsirabādu biprabara dīnhā.\ndekhi rāma chabi nayana juḍāne, kari sanamānu āśramahi āne.",
        "translation": "Rama prostrated before the sage; the great Brahmin gave his blessings.\nSeeing Rama's beauty, his eyes were soothed; honoring them, he brought them to the ashram."
    },
    "ay-125-c2": {
        "transliteration": "munibara atithi prānapriya pāe, kaṁda mūla phala madhura magāe.\nsiya saumitri rāma phala khāe, taba muni āśrama die suhāe.",
        "translation": "The great sage received these guests who were dearer than life and had sweet roots, tubers and fruits brought.\nSita, Lakshmana and Rama ate the fruits; then the sage assigned them pleasant quarters in the ashram."
    },
    "ay-125-c3": {
        "transliteration": "bālamīki mana ānaṁdu bhārī, maṁgala mūrati nayana nihārī.\ntaba kara kamala jori raghurāī, bole bacana śravana sukhadāī.",
        "translation": "Valmiki's heart was full of immense joy, beholding the auspicious form with his own eyes.\nThen the Lord of the Raghus, joining His lotus hands, spoke words that were a delight to the ears."
    },
    "ay-125-c4": {
        "transliteration": "tumha trikāla darasī munināthā, bisva badara jimi tumharēṁ hāthā.\nasa kahi prabhu saba kathā bakhānī, jehi jehi bhāṁti dīnha banu rānī.",
        "translation": "'You are a seer of the three times (past, present and future), O lord of sages; the universe rests in your palm like a jujube fruit.'\nSaying this, the Lord narrated the whole story — how the queen had arranged for the exile to the forest."
    },
    "ay-125-d": {
        "transliteration": "tāta bacana puni mātu hita bhāi bharata asa rāu.\nmo kahuṁ darasa tumhāra prabhu sabu mama punya prabhāu. 125.",
        "translation": "'My father's command, my mother's welfare, my brother Bharata's nobility and such is the king.\nThat I behold You, O sage, is all the effect of my accumulated merit.'"
    },

    # ===== DOHA GROUP 126 =====
    "ay-126-c1": {
        "transliteration": "dekhi pāya munirāya tumhāre, bhae sukṛta saba suphala hamāre.\naba jahaṁ rāura āyasu hoī, muni udabegu na pāvai koī.",
        "translation": "'Seeing your feet, O king of sages, all our good deeds have borne their fruit.\nNow, wherever you command, may no sage be disturbed by our presence.'"
    },
    "ay-126-c2": {
        "transliteration": "muni tāpasa jinha tēṁ dukhu lahahīṁ, te naresa binu pāvaka dahahīṁ.\nmaṁgala mūla bipra paritoṣū, dahai koṭi kula bhūsura roṣū.",
        "translation": "'Kings who cause suffering to sages and ascetics burn without fire.\nThe satisfaction of Brahmins is the root of all blessings; the wrath of a Brahmin can destroy ten million families.'"
    },
    "ay-126-c3": {
        "transliteration": "asa jiyaṁ jāni kahia soi ṭhāūṁ, siya saumitri sahita jahaṁ jāūṁ.\ntahaṁ raci rucira parana tṛna sālā, bāsu karauṁ kachu kāla kṛpālā.",
        "translation": "'Knowing this in my heart, please tell me a place where I may go with Sita and Lakshmana.\nI shall build a beautiful hut of leaves and grass there and dwell for some time, O gracious one.'"
    },
    "ay-126-c4": {
        "transliteration": "sahaja sarala suni raghubara bānī, sādhu sādhu bole muni gyānī.\nkasa na kahahu asa raghukulaketū, tumha pālaka saṁtata śruti setū.",
        "translation": "Hearing Raghubara's naturally simple and sincere words, the wise sage exclaimed: 'Excellent! Excellent!\nHow could You speak otherwise, O banner of the Raghu dynasty? You are forever the protector and upholder of Vedic law.'"
    },

    # ===== DOHA GROUP 127 =====
    "ay-127-c1": {
        "transliteration": "jagu pekhana tumha dekhanihāre, bidhi hari saṁbhu nacāvanihāre.\nteu na jānahi maramu tumhārā, auru tumhahi ko jānanihārā.",
        "translation": "'The world is the spectacle and You are the spectator; Brahma, Vishnu and Shiva are those You cause to dance.\nEven They do not know Your secret — who else then can know You?'"
    },
    "ay-127-c2": {
        "transliteration": "soi jānai jehi dehu janāī, jānata tumhahi tumhai hoi jāī.\ntumharihi kṛpāṁ tumhahi raghunṁdana, jānahi bhagata bhagata ura caṁdana.",
        "translation": "'Only he knows You to whom You reveal Yourself; and knowing You, he becomes one with You.\nBy Your grace alone, O Raghunandana, devotees come to know You — You who are sandalwood to the devotee's heart.'"
    },
    "ay-127-c3": {
        "transliteration": "cidānaṁdamaya deha tumhārī, bigata bikāra jāna adhikārī.\nnara tanu dharehu saṁta sura kājā, kahahu karahu jasa prākṛta rājā.",
        "translation": "'Your body is made of pure consciousness and bliss; the qualified alone know it to be free from all modifications.\nYou have assumed a human form for the sake of saints and gods; You speak and act like an ordinary king.'"
    },
    "ay-127-c4": {
        "transliteration": "rāma dekhi suni carita tumhāre, jaḍa mohahi budha hohi sukhāre.\ntumha jo kahahu karahu sabu sāṁcā, jasa kāchia tasa cāhia nācā.",
        "translation": "'O Rama, seeing and hearing Your deeds, the ignorant are deluded while the wise are delighted.\nWhatever You say and do is all genuine — one must dance according to the costume one wears.'"
    },
    "ay-127-d": {
        "transliteration": "pūṁchehu mohi ki rahauṁ kahaṁ maiṁ pūṁchata sakucāuṁ.\njahaṁ na hohu tahaṁ dehu kahi tumhahi dekhāvauṁ ṭhāuṁ. 127.",
        "translation": "'You ask me where You should stay — I feel shy to answer.\nTell me where You are not present, and then I shall show You a place!'"
    },

    # ===== DOHA GROUP 128 =====
    "ay-128-c1": {
        "transliteration": "suni muni bacana prema rasa sāne, sakuci rāma mana mahuṁ musukāne.\nbālamīki haṁsi kahahi bahorī, bānī madhura amia rasa borī.",
        "translation": "Hearing the sage's words steeped in the nectar of love, Rama felt abashed and smiled inwardly.\nValmiki laughed and spoke again, his voice sweet and drenched in ambrosia."
    },
    "ay-128-c2": {
        "transliteration": "sunahu rāma aba kahauṁ niketā, jahāṁ basahu siya lakhana sametā.\njinha ke śravana samudra samānā, kathā tumhāri subhaga sari nānā.",
        "translation": "'Listen, O Rama, now I shall describe the dwellings where You should live with Sita and Lakshmana.\nThose whose ears are like the ocean — into which the many beautiful rivers of Your stories flow —'"
    },
    "ay-128-c3": {
        "transliteration": "bharahi niraṁtara hohi na pūre, tinha ke hiya tumha kahuṁ gṛha rūre.\nlocana cātaka jinha kari rākhe, rahahi darasa jaladhara abhilāṣe.",
        "translation": "'which fill ceaselessly yet never overflow — their hearts are fine homes for You.\nThose who have made their eyes like chataka birds, ever longing for the rain-cloud of Your sight,'"
    },
    "ay-128-c4": {
        "transliteration": "nidarahi sarita siṁdhu sara bhārī, rūpa biṁdu jala hohi sukhārī.\ntinha ke hṛdaya sadana sukhadāyaka, basahu baṁdhu siya saha raghunāyaka.",
        "translation": "'who disdain rivers, oceans and great lakes, and are gladdened by a single drop of Your beauty-rain —\nin their bliss-giving hearts, O Lord of the Raghus, dwell with Your brother and Sita.'"
    },
    "ay-128-d": {
        "transliteration": "jasu tumhāra mānasa bimala haṁsinī jīhā jāsu.\nmuktāhala guna gana cunai rāma basahu hiyaṁ tāsu. 128.",
        "translation": "'Your fame is a spotless Manasa lake, and one whose tongue is a swan upon it,\npicking up the pearls of Your virtues — O Rama, dwell in the heart of such a one.'"
    },

    # ===== DOHA GROUP 129 =====
    "ay-129-c1": {
        "transliteration": "prabhu prasāda suci subhaga subāsā, sādara jāsu lahai nita nāsā.\ntumhahi nibedita bhojana karahīṁ, prabhu prasāda paṭa bhūṣana dharahīṁ.",
        "translation": "'Those whose nostrils reverently inhale the pure, beautiful and fragrant offerings of the Lord every day;\nwho eat food only after offering it to You, and wear garments and ornaments as Your blessed gifts —'"
    },
    "ay-129-c2": {
        "transliteration": "sīsa navahi sura guru dvija dekhī, prīti sahita kari binaya biseṣī.\nkara nita karahi rāma pada pūjā, rāma bharosa hṛdayaṁ nahi dūjā.",
        "translation": "'Who bow their heads upon seeing gods, the guru and Brahmins, with love and special humility;\nwhose hands daily worship Rama's feet, with trust in Rama alone and no other in their hearts —'"
    },
    "ay-129-c3": {
        "transliteration": "carana rāma tīratha calī jāhīṁ, rāma basahu tinha ke mana māhīṁ.\nmaṁtrarāju nita japahi tumhārā, pūjahi tumhahi sahita parivārā.",
        "translation": "'Whose feet walk to pilgrimage places sacred to Rama — O Rama, dwell in the minds of such devotees.\nWho daily chant Your supreme mantra and worship You along with Your entire divine family —'"
    },
    "ay-129-c4": {
        "transliteration": "tarapana homa karahi bidhi nānā, bipra jevāṁi dehi bahu dānā.\ntumha tēṁ adhika gurahi jiyaṁ jānī, sakala bhāyaṁ sevahi sanamānī.",
        "translation": "'Who perform oblations and fire-rituals of many kinds, who feed Brahmins and give abundant charity;\nwho regard the guru as even greater than You in their hearts and serve him with honor in every way —'"
    },

    # ===== DOHA GROUP 130 =====
    "ay-130-c1": {
        "transliteration": "kāma koha mada māna na mohā, lobha na chobha na rāga na drohā.\njinha kēṁ kapaṭa daṁbha nahiṁ māyā, tinha kēṁ hṛdaya basahu raghurāyā.",
        "translation": "'Those who have no lust, anger, pride, arrogance or delusion; no greed, agitation, attachment or malice;\nin whose hearts there is no deceit, hypocrisy or guile — O Lord of the Raghus, dwell in their hearts.'"
    },
    "ay-130-c2": {
        "transliteration": "saba ke priya saba ke hitakārī, dukha sukha sarisa prasaṁsā gārī.\nkahahi satya priya bacana bicārī, jāgata sovata sarana tumhārī.",
        "translation": "'Dear to all and benefactors of all, to whom sorrow and joy, praise and abuse are the same;\nwho speak truth, pleasant and considered words, and who, waking or sleeping, are in Your refuge —'"
    },
    "ay-130-c3": {
        "transliteration": "tumhahi chāḍi gati dūsarī nāhīṁ, rāma basahu tinha ke mana māhīṁ.\njananī sama jānahi paranārī, dhanu parāva biṣa tēṁ biṣa bhārī.",
        "translation": "'Who have no other refuge than You — O Rama, dwell in their minds.\nWho regard another's wife as a mother, and another's wealth as more deadly than poison —'"
    },
    "ay-130-c4": {
        "transliteration": "je haraṣahi para saṁpati dekhī, dukhita hohi para bipati biseṣī.\njinhahi rāma tumha prānapiāre, tinha ke mana subha sadana tumhāre.",
        "translation": "'Who rejoice at seeing others' prosperity and are deeply grieved by others' adversity;\nto whom You, O Rama, are dearer than life — their pure hearts are Your abode.'"
    },
    "ay-130-d": {
        "transliteration": "svāmī sakhā pitu mātu guru jinha ke saba tumha tāta.\nmana maṁdira tinha kēṁ basahu sīya sahita dou bhrāta. 130.",
        "translation": "'Those for whom You alone are master, friend, father, mother and guru, O Lord —\nin the temple of their hearts, dwell with Sita and both brothers.'"
    },
}

# Apply updates
count = 0
for group in data["dohaGroups"]:
    if 66 <= group["dohaNumber"] <= 130:
        for verse in group["verses"]:
            vid = verse["id"]
            if vid in updates:
                verse["transliteration"] = updates[vid]["transliteration"]
                verse["translation"] = updates[vid]["translation"]
                count += 1

print(f"Updated {count} verses")

with open(INPUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("File written successfully")
