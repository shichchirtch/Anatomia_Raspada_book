from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



one_one_button = InlineKeyboardButton(text='1. Правовая норма как метрика.', url='https://telegra.ph/1-Pravovaya-norma-kak-metrika-Pravovye-razlomy-07-24')

one_two_button = InlineKeyboardButton(text='2. От руин к "взбесившемуся принтеру"', callback_data='От руин')
one_three_button = InlineKeyboardButton(text='3. Как в современной России менялись нормы Уголовного кодекса ', callback_data='Как в современной')
one_four_button = InlineKeyboardButton(text='4. Институты и субъекты:', callback_data='Институты')

one_zero_kb = InlineKeyboardMarkup(inline_keyboard=
                                   [[one_one_button],[one_two_button],[one_three_button],[one_four_button]])
#######################################################################################################################
one_two_1 = InlineKeyboardButton(text='Борьба вокруг смертной казни', url='https://telegra.ph/Prava-cheloveka-Borba-vokrug-smertnoj-kazni-07-24')
one_two_2 = InlineKeyboardButton(text='Становление репрессивного законодательства', url='https://telegra.ph/Stanovlenie-repressivnogo-zakonodatelstva-07-25')

one_two_kb = InlineKeyboardMarkup(inline_keyboard=[[one_two_1], [one_two_2]])

#№§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§

one_three_1 = InlineKeyboardButton(text='Уголовный кодекс 1996 года', url='https://telegra.ph/Kak-v-sovremennoj-Rossii-menyalis-normy-Ugolovnogo-kodeksa-i-pri-chyom-tut-pravo-na-zhizn-07-25')
one_three_2 = InlineKeyboardButton(text='Первый постсоветский Уголовный кодекс', url='https://telegra.ph/Pervyj-postsovetskij-Ugolovnyj-kodeks-07-25')
one_three_3 = InlineKeyboardButton(text=' Поправки начала 2000-х', url='https://telegra.ph/Popravki-nachala-2000-h-07-25')
one_three_4 = InlineKeyboardButton(text='Начало 2010-х: фиксация на протестах', url='https://telegra.ph/Nachalo-2010-h-fiksaciya-na-protestah-07-25')
one_three_5 = InlineKeyboardButton(text='Борьба за пытки', url='https://telegra.ph/Borba-za-pytki-07-25')
one_three_6 = InlineKeyboardButton(text='Четверть века развития: итоги', url='https://telegra.ph/CHetvert-veka-razvitiya-itogi-Za-chto-chashche-vsego-rugayut-rossijskij-UK-07-25')

one_three_kb = InlineKeyboardMarkup(inline_keyboard=[[one_three_1], [one_three_2],[one_three_3],
                                                     [one_three_4], [one_three_5], [one_three_6]])
#####################################################################################################################

one_four_1 = InlineKeyboardButton(text='Становление российского уголовного процесса', url='https://telegra.ph/4-Instituty-i-subekty-kak-111-menyalis-normy-ot-kotoryh-zavisit-ugolovnyj-process-07-26')
one_four_2 = InlineKeyboardButton(text='Состояние перманентной реформы', url='https://telegra.ph/Sostoyanie-permanentnoj-reformy-07-26')
one_four_3 = InlineKeyboardButton(text='Дисбалансы уголовного процесса', url='https://telegra.ph/Disbalansy-ugolovnogo-processa-07-26')
one_four_4 = InlineKeyboardButton(text='Распад правовой системы', url='https://telegra.ph/Raspad-pravovoj-sistemy-07-26')

one_four_kb = InlineKeyboardMarkup(inline_keyboard=[[one_four_1], [one_four_2],[one_four_3], [one_four_4]])

################################################################################################################################

II_1_button = InlineKeyboardButton(text='1. Путь одного дела', url='https://telegra.ph/1-Put-odnogo-dela-07-26')
II_2_button = InlineKeyboardButton(text='2. Кто принимает решения', callback_data='Кто принимает')
II_3_button = InlineKeyboardButton(text='3. Принципы и парадоксы функционирования правоохранительной системы: ', callback_data='Принципы и парадоксы')
II_4_button = InlineKeyboardButton(text='4. Эволюция жестокости', callback_data='Эволюция')

II_zero_kb = InlineKeyboardMarkup(inline_keyboard=[[II_1_button], [II_2_button], [II_3_button], [II_4_button]])

#####################################################################################################################

II_2_1_button = InlineKeyboardButton(text='Штрихи к портрету российского правоохранителя', url='https://telegra.ph/SHtrihi-k-portretu-rossijskogo-pravoohranitelya-07-26')
II_2_2_button = InlineKeyboardButton(text='Образование правоохранителей', url='https://telegra.ph/Obrazovanie-pravoohranitelej-07-26')
II_2_3_button = InlineKeyboardButton(text="Трансляция профессиональных практик", url='https://telegra.ph/Translyaciya-professionalnyh-praktik-07-26')
II_2_4_button = InlineKeyboardButton(text='НКО и программы Совета Европы', url='https://telegra.ph/Dopolnitelnoe-obuchenie-NKO-i-programmy-Soveta-Evropy-07-26')
II_2_5_button = InlineKeyboardButton(text='Уголовная бюрократия', url='https://telegra.ph/Ugolovnaya-byurokratiya-07-26')
II_2_6_button = InlineKeyboardButton(text='Проблемы правоохранителей', url='https://telegra.ph/Problemy-pravoohranitelej-obezlichivanie-otchyotnost-peregruzki-07-26')

II_two_kb = InlineKeyboardMarkup(inline_keyboard=[[II_2_1_button], [II_2_2_button], [II_2_3_button],
                                                  [II_2_4_button], [II_2_5_button], [II_2_6_button]])


#############################################################################################################################

II_3_1_button = InlineKeyboardButton(text='Почему институты не меняются', url='https://telegra.ph/3-Principy-i-paradoksy-funkcionirovaniya-pravoohranitelnoj-sistemy-pochemu-instituty-ne-menyayutsya-07-27')
II_3_2_button = InlineKeyboardButton(text='Парадокс скованной самостоятельности', url='https://telegra.ph/Paradoks-skovannoj-samostoyatelnosti-kak-rassoglasovannost-pravil-vedyot-k-bezzakoniyu-07-27')
II_3_3_button = InlineKeyboardButton(text='Парадокс бесконтрольного контроля', url='https://telegra.ph/Paradoks-beskontrolnogo-kontrolya-07-27')
II_3_4_button = InlineKeyboardButton(text='Принцип широко закрытых глаз', url='https://telegra.ph/Princip-shiroko-zakrytyh-glaz-07-27')
II_3_5_button = InlineKeyboardButton(text='Группы, состоящие из одиночек', url='https://telegra.ph/Gruppy-sostoyashchie-iz-odinochek-07-27')
II_3_6_button = InlineKeyboardButton(text='Сохранить лицо', url='https://telegra.ph/Sohranit-lico-07-27')
II_3_7_button = InlineKeyboardButton(text='Принцип пружинящей дистанции', url='https://telegra.ph/Princip-pruzhinyashchej-distancii-07-27')
II_3_8_button = InlineKeyboardButton(text='Парадокс мнимой открытости', url='https://telegra.ph/Paradoks-mnimoj-otkrytosti-07-27')
II_3_9_button = InlineKeyboardButton(text='Самовоспроизводство институтов', url='https://telegra.ph/Samovosproizvodstvo-institutov-blokirovanie-izmenenij-07-27')


II_three_kb = InlineKeyboardMarkup(inline_keyboard=[[II_3_1_button], [II_3_2_button], [II_3_3_button],
                                                  [II_3_4_button], [II_3_5_button], [II_3_6_button],
                                                    [II_3_7_button], [II_3_8_button], [II_3_9_button]])

###################################################################################################################

II_4_1_button = InlineKeyboardButton(text='Эволюция жестокости', url='https://telegra.ph/4-EHvolyuciya-zhestokosti-07-27')
II_4_2_button = InlineKeyboardButton(text='Между писаными нормами и неформальными правилами', url='https://telegra.ph/Mezhdu-pisanymi-normami-i-neformalnymi-pravilami-07-27')

II_four_kb = InlineKeyboardMarkup(inline_keyboard=[[II_4_1_button], [II_4_2_button]])

######################################################################################################

III_1_button = InlineKeyboardButton(text='Как общество и государство говорят о правах человека', url='https://telegra.ph/Kak-obshchestvo-i-gosudarstvo-govoryat-o-pravah-cheloveka-07-27')
III_2_button = InlineKeyboardButton(text='1. Сдержки и противовесы', url='https://telegra.ph/1-Sderzhki-i-protivovesy-pochemu-otsutstvie-nastoyashchego-razdeleniya-vlastej-kritichno-dlya-sistemy-zashchity-prav-cheloveka-07-27')
III_3_button = InlineKeyboardButton(text='2. От декларации к декорации', url='https://telegra.ph/2-Ot-deklaracii-k-dekoracii-Prava-cheloveka-v-diskurse-gosudarstva-07-28')
III_4_button = InlineKeyboardButton(text='3. «Западное» — значит вражеское', url='https://telegra.ph/3-Zapadnoe--znachit-vrazheskoe-07-28')
III_5_button = InlineKeyboardButton(text='4. А есть ли противодействие?', url='https://telegra.ph/4-A-est-li-protivodejstvie-Rabota-SPCH-kak-svyazuyushchego-organa-mezhdu-grazhdanskim-obshchestvom-i-gosudarstvom-07-29')
III_6_button = InlineKeyboardButton(text='5. Права человека в общественном дискурсе', callback_data='Права')
III_7_button = InlineKeyboardButton(text='6. Синдром вины: что было сделано не так', callback_data='Синдром')


III_zero_kb = InlineKeyboardMarkup(inline_keyboard=[[III_1_button], [III_2_button], [III_3_button],
                                                    [III_4_button] , [III_5_button] , [III_6_button], [III_7_button]])

#########################################################################################################

III_6_1_button = InlineKeyboardButton(text='Права человека в общественном дискурсе', url="https://telegra.ph/5-Prava-cheloveka-v-obshchestvennom-diskurse-07-29")
III_6_2_button = InlineKeyboardButton(text='Поп-культура', url="https://telegra.ph/Pop-kultura-07-29")

III_6_kb = InlineKeyboardMarkup(inline_keyboard=[[III_6_1_button], [III_6_2_button]])

########################################################################################################


III_7_1_button = InlineKeyboardButton(text='Синдром вины', url="https://telegra.ph/6-Sindrom-viny-chto-bylo-sdelano-ne-tak-07-29")
III_7_2_button = InlineKeyboardButton(text='Вещь в себе', url="https://telegra.ph/Veshch-v-sebe-07-29")
III_7_3_button = InlineKeyboardButton(text='Короткая память', url="https://telegra.ph/Korotkaya-pamyat-07-29")
III_7_4_button = InlineKeyboardButton(text='Реклама страхов', url="https://telegra.ph/Reklama-strahov-07-29")
III_7_5_button = InlineKeyboardButton(text='Права человека оказались лишними', url="https://telegra.ph/Prava-cheloveka-okazalis-lishnimi-07-29")

III_7_kb = InlineKeyboardMarkup(inline_keyboard=[[III_7_1_button], [III_7_2_button] , [III_7_3_button] , [III_7_4_button] , [III_7_5_button]])

####################################################################################################################

