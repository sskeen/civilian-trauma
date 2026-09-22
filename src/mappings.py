"""
Ukraine administrative unit mappings for ULS pipeline.

ADMIN_UNIT_TO_OBLAST: Postal code prefix (2 digits) → Oblast name
RAION_UA_TO_EN: Ukrainian raion names → English translations

Sources:
- Ukrposhta postal code system: https://en.wikipedia.org/wiki/Postal_codes_in_Ukraine
- Raions of Ukraine (post-2020 reform): https://en.wikipedia.org/wiki/Raions_of_Ukraine
"""

# Postal code prefix → Oblast
# Source: https://en.wikipedia.org/wiki/Postal_codes_in_Ukraine

ADMIN_UNIT_TO_OBLAST = {
    # Kyiv city (01-06)
    '01': 'Kyiv', '02': 'Kyiv', '03': 'Kyiv',
    '04': 'Kyiv', '05': 'Kyiv', '06': 'Kyiv',
    # Kyiv Oblast (07-09)
    '07': 'Kyiv Oblast', '08': 'Kyiv Oblast', '09': 'Kyiv Oblast',
    # Zhytomyr Oblast (10-13)
    '10': 'Zhytomyr Oblast', '11': 'Zhytomyr Oblast',
    '12': 'Zhytomyr Oblast', '13': 'Zhytomyr Oblast',
    # Chernihiv Oblast (14-17)
    '14': 'Chernihiv Oblast', '15': 'Chernihiv Oblast',
    '16': 'Chernihiv Oblast', '17': 'Chernihiv Oblast',
    # Cherkasy Oblast (18-22)
    '18': 'Cherkasy Oblast', '19': 'Cherkasy Oblast', '20': 'Cherkasy Oblast',
    '21': 'Cherkasy Oblast', '22': 'Cherkasy Oblast',
    # Vinnytsia Oblast (23-24)
    '23': 'Vinnytsia Oblast', '24': 'Vinnytsia Oblast',
    # Kirovohrad Oblast (25-28)
    '25': 'Kirovohrad Oblast', '26': 'Kirovohrad Oblast',
    '27': 'Kirovohrad Oblast', '28': 'Kirovohrad Oblast',
    # Khmelnytskyi Oblast (29-32)
    '29': 'Khmelnytskyi Oblast', '30': 'Khmelnytskyi Oblast',
    '31': 'Khmelnytskyi Oblast', '32': 'Khmelnytskyi Oblast',
    # Rivne Oblast (33-35)
    '33': 'Rivne Oblast', '34': 'Rivne Oblast', '35': 'Rivne Oblast',
    # Poltava Oblast (36-39)
    '36': 'Poltava Oblast', '37': 'Poltava Oblast',
    '38': 'Poltava Oblast', '39': 'Poltava Oblast',
    # Sumy Oblast (40-42)
    '40': 'Sumy Oblast', '41': 'Sumy Oblast', '42': 'Sumy Oblast',
    # Volyn Oblast (43-45)
    '43': 'Volyn Oblast', '44': 'Volyn Oblast', '45': 'Volyn Oblast',
    # Ternopil Oblast (46-48)
    '46': 'Ternopil Oblast', '47': 'Ternopil Oblast', '48': 'Ternopil Oblast',
    # Dnipropetrovsk Oblast (49-53)
    '49': 'Dnipropetrovsk Oblast', '50': 'Dnipropetrovsk Oblast',
    '51': 'Dnipropetrovsk Oblast', '52': 'Dnipropetrovsk Oblast',
    '53': 'Dnipropetrovsk Oblast',
    # Mykolaiv Oblast (54-57)
    '54': 'Mykolaiv Oblast', '55': 'Mykolaiv Oblast',
    '56': 'Mykolaiv Oblast', '57': 'Mykolaiv Oblast',
    # Chernivtsi Oblast (58-60)
    '58': 'Chernivtsi Oblast', '59': 'Chernivtsi Oblast', '60': 'Chernivtsi Oblast',
    # Kharkiv Oblast (61-64)
    '61': 'Kharkiv Oblast', '62': 'Kharkiv Oblast',
    '63': 'Kharkiv Oblast', '64': 'Kharkiv Oblast',
    # Odesa Oblast (65-68)
    '65': 'Odesa Oblast', '66': 'Odesa Oblast',
    '67': 'Odesa Oblast', '68': 'Odesa Oblast',
    # Zaporizhzhia Oblast (69-72)
    '69': 'Zaporizhzhia Oblast', '70': 'Zaporizhzhia Oblast',
    '71': 'Zaporizhzhia Oblast', '72': 'Zaporizhzhia Oblast',
    # Kherson Oblast (73-75)
    '73': 'Kherson Oblast', '74': 'Kherson Oblast', '75': 'Kherson Oblast',
    # Ivano-Frankivsk Oblast (76-78)
    '76': 'Ivano-Frankivsk Oblast', '77': 'Ivano-Frankivsk Oblast',
    '78': 'Ivano-Frankivsk Oblast',
    # Lviv Oblast (79-82)
    '79': 'Lviv Oblast', '80': 'Lviv Oblast',
    '81': 'Lviv Oblast', '82': 'Lviv Oblast',
    # Donetsk Oblast (83-87)
    '83': 'Donetsk Oblast', '84': 'Donetsk Oblast', '85': 'Donetsk Oblast',
    '86': 'Donetsk Oblast', '87': 'Donetsk Oblast',
    # Zakarpattia Oblast (88-90)
    '88': 'Zakarpattia Oblast', '89': 'Zakarpattia Oblast', '90': 'Zakarpattia Oblast',
    # Luhansk Oblast (91-94)
    '91': 'Luhansk Oblast', '92': 'Luhansk Oblast',
    '93': 'Luhansk Oblast', '94': 'Luhansk Oblast',
    # AR Crimea (95-98) & Sevastopol (99)
    '95': 'AR Crimea', '96': 'AR Crimea', '97': 'AR Crimea', '98': 'AR Crimea',
    '99': 'Sevastopol',
}


# UCDP adm_1 → Standard oblast names
# Source: UCDP GED v26.1 unique adm_1 values for Ukraine
# Maps UCDP romanization variants to project-standard oblast names

UCDP_ADM1_TO_OBLAST = {
    # Standard matches (minor case/spelling normalization)
    'Donetsk oblast': 'Donetsk Oblast',
    'Kharkiv oblast': 'Kharkiv Oblast',
    'Luhansk oblast': 'Luhansk Oblast',
    'Kherson oblast': 'Kherson Oblast',
    'Sumy oblast': 'Sumy Oblast',
    'Dnipropetrovsk oblast': 'Dnipropetrovsk Oblast',
    'Chernihiv oblast': 'Chernihiv Oblast',
    'Kyiv oblast': 'Kyiv Oblast',
    'Zhytomyr oblast': 'Zhytomyr Oblast',
    'Poltava oblast': 'Poltava Oblast',
    'Lviv oblast': 'Lviv Oblast',
    'Cherkasy oblast': 'Cherkasy Oblast',
    'Rivne oblast': 'Rivne Oblast',
    'Khmelnytskyi oblast': 'Khmelnytskyi Oblast',
    'Kirovohrad oblast': 'Kirovohrad Oblast',
    'Volyn oblast': 'Volyn Oblast',
    'Ivano-Frankivsk oblast': 'Ivano-Frankivsk Oblast',
    'Ternopil oblast': 'Ternopil Oblast',
    'Zakarpattia oblast': 'Zakarpattia Oblast',
    'Chernivtsi oblast': 'Chernivtsi Oblast',
    # Romanization variants
    'Zaporizhzhya oblast': 'Zaporizhzhia Oblast',
    'Odessa oblast': 'Odesa Oblast',
    'Mykolayiv oblast': 'Mykolaiv Oblast',
    'Vinnytsya oblast': 'Vinnytsia Oblast',
    # Kyiv city variants
    'Kyiv Special Republican city': 'Kyiv',
    'Kiev Special Republican city': 'Kyiv',
    # Crimea & Sevastopol
    'Autonomous Republic of Crimea': 'AR Crimea',
    'Sevastopol City State Administration': 'Sevastopol',
}


# UCDP adm_2 → Standard raion_nominatim_en names
# Source: UCDP GED v26.1 unique adm_2 values for Ukraine
# Maps UCDP romanization variants to project-standard raion names (post-2020 reform)

UCDP_ADM2_TO_RAION_EN = {
    # === High-frequency raions (>100 events) ===
    'Pokrovsk raion': 'Pokrovsk Raion',
    'Bakhmut raion': 'Bakhmut Raion',
    'Kramatorsk raion': 'Kramatorsk Raion',
    'Volnovakha raion': 'Volnovakha Raion',
    'Polohy raion': 'Polohy Raion',
    'Kupiansk raion': 'Kupiansk Raion',
    'Kherson raion': 'Kherson Raion',
    'Severodonetsk raion': 'Sievierodonetsk Raion',
    'Svativskyi raion': 'Svatove Raion',
    'Chuhuiv raion': 'Chuhuiv Raion',
    'Donetsk raion': 'Donetsk Raion',
    'Kharkiv raion': 'Kharkiv Raion',
    'Beryslav raion': 'Beryslav Raion',
    'Sumy raion': 'Sumy Raion',
    'Vasylivka raion': 'Vasylivka Raion',
    'Izyum raion': 'Izium Raion',
    'Kakhovka raion': 'Kakhovka Raion',
    'Synelnykove raion': 'Synelnykove Raion',
    'Horlivka raion': 'Horlivka Raion',
    'Mariupol raion': 'Mariupol Raion',
    'Zaporizhzhia raion': 'Zaporizhzhia Raion',
    'Mykolayiv raion': 'Mykolaiv Raion',
    'Bucha raion': 'Bucha Raion',
    'Chernihiv raion': 'Chernihiv Raion',
    'Nikopol raion': 'Nikopol Raion',
    'Skadovsk raion': 'Skadovsk Raion',
    # === Medium-frequency raions (20-100 events) ===
    'Dnipro raion': 'Dnipro Raion',
    'Bohodukhiv raion': 'Bohodukhiv Raion',
    'Shostkynskyi raion': 'Shostka Raion',
    'Odessa raion': 'Odesa Raion',
    'Okhtyrska raion': 'Okhtyrka Raion',
    'Kryvyi Rih raion': 'Kryvyi Rih Raion',
    'Bashtanka raion': 'Bashtanka Raion',
    'Melitopol raion': 'Melitopol Raion',
    'Novhorod-Siverskyi raion': 'Novhorod-Siverskyi Raion',
    'Nizhyn raion': 'Nizhyn Raion',
    'Vyshhorod raion': 'Vyshhorod Raion',
    'Berdyansk raion': 'Berdiansk Raion',
    'Brovary raion': 'Brovary Raion',
    'Konotop raion': 'Konotop Raion',
    'Henichesk raion': 'Henichesk Raion',
    'Alchevsk raion': 'Alchevsk Raion',
    'Pavlohrad raion': 'Pavlohrad Raion',
    'Shchastia raion': 'Shchastia Raion',
    'Koriukivka raion': 'Koriukivka Raion',
    'Korosten raion': 'Korosten Raion',
    'Fastiv raion': 'Fastiv Raion',
    'Pryluky raion': 'Pryluky Raion',
    'Zhytomyr raion': 'Zhytomyr Raion',
    'Izmail raion': 'Izmail Raion',
    'Starobilsk raion': 'Starobilsk Raion',
    'Lozova raion': 'Lozova Raion',
    'Lviv raion': 'Lviv Raion',
    'Bilhorod-Dnistrovskyi raion': 'Bilhorod-Dnistrovskyi Raion',
    'Cherkasy raion': 'Cherkasy Raion',
    'Kamyanske raion': 'Kamianske Raion',
    'Poltava raion': 'Poltava Raion',
    'Myrhorod raion': 'Myrhorod Raion',
    'Kropyvnytskyi raion': 'Kropyvnytskyi Raion',
    'Khmelnytskyi raion': 'Khmelnytskyi Raion',
    'Rivne raion': 'Rivne Raion',
    # === Low-frequency raions (<20 events) ===
    'Obukhiv raion': 'Obukhiv Raion',
    'Lutsk raion': 'Lutsk Raion',
    'Romny raion': 'Romny Raion',
    'Boryspil raion': 'Boryspil Raion',
    'Svatove raion': 'Svatove Raion',
    'Sarnenskyi raion': 'Sarny Raion',
    'Ternopil raion': 'Ternopil Raion',
    'Kremenchuk raion': 'Kremenchuk Raion',
    'Oleksandriia raion': 'Oleksandriia Raion',
    'Uman raion': 'Uman Raion',
    'Vinnytsia raion': 'Vinnytsia Raion',
    'Voznesensk raion': 'Voznesensk Raion',
    'Rovenky raion': 'Rovenky Raion',
    'Kalush raion': 'Kalush Raion',
    'Dovzhansk raion': 'Dovzhansk Raion',
    'Volodymyr-Volynska raion': 'Volodymyr Raion',
    'Ivano-Frankivsk raion': 'Ivano-Frankivsk Raion',
    'Kolomyya raion': 'Kolomyia Raion',
    'Podilsk raion': 'Podilsk Raion',
    'Khmilnyk raion': 'Khmilnyk Raion',
    'Shepetivka raion': 'Shepetivka Raion',
    'Kamyanets-Podilskyy raion': 'Kamianets-Podilskyi Raion',
    'Chernivtsi raion': 'Chernivtsi Raion',
    'Chortkiv raion': 'Chortkiv Raion',
    'Zolotonosha raion': 'Zolotonosha Raion',
    'Haisyn raion': 'Haisyn Raion',
    'Stryi raion': 'Stryi Raion',
    'Sambir raion': 'Sambir Raion',
    'Kremenets raion': 'Kremenets Raion',
    'Mukachevo raion': 'Mukachevo Raion',
    'Zviahel raion': 'Zviaghel Raion',
    'Kovel raion': 'Kovel Raion',
    'Zhmerynka raion': 'Zhmerynka Raion',
    'Yavoriv raion': 'Yavoriv Raion',
    # === City municipalities (map to containing raion where applicable) ===
    'Donetsk City municipality': 'Donetsk Raion',
    'Horlivka City municipality': 'Horlivka Raion',
    'Avdiivka city municipality': 'Pokrovsk Raion',
    'Debaltseve City municipality': 'Horlivka Raion',
    'Luhansk City municipality': 'Luhansk Raion',
    'Makiivka City municipality': 'Donetsk Raion',
    'Mariupol City municipality': 'Mariupol Raion',
    'Dokuchaev City municipality': 'Volnovakha Raion',
    'Pervomaisk City municipality': 'Rovenky Raion',
    'Kadiivka City municipality': 'Alchevsk Raion',
    'Severodonetsk City municipality': 'Sievierodonetsk Raion',
    'Snizhne City municipality': 'Donetsk Raion',
    'Zhdanivka city municipality': 'Horlivka Raion',
    'Artemivsk city municipality': 'Bakhmut Raion',
    'Krasnyi Lyman City municipality': 'Kramatorsk Raion',
    'Yenakiieve City municipality': 'Horlivka Raion',
    'Kirovsk City municipality': 'Alchevsk Raion',
    'Selydove city municipality': 'Pokrovsk Raion',
    'Stakhaniv City municipality': 'Alchevsk Raion',
    'Druzhkivka City municipality': 'Kramatorsk Raion',
    'Dzhankoi city municipality': None,  # Crimea - no standard raion
    'Simferopol City municipality': None,  # Crimea
    'Rubizhne City municipality': 'Sievierodonetsk Raion',
    'Alchevsk city municipality': 'Alchevsk Raion',
    'Odessa City municipality': 'Odesa Raion',
    # === Pre-2020 raion names (map to post-2020 equivalents) ===
    'Yasynuvata raion': 'Donetsk Raion',
    'Popasna raion': 'Sievierodonetsk Raion',
    'Starobesheve raion': 'Donetsk Raion',
    'Amvrosiivka raion': 'Donetsk Raion',
    'Marinka raion': 'Pokrovsk Raion',
    'Novoaidar raion': 'Sievierodonetsk Raion',
    'Shaktarsk raion': 'Donetsk Raion',
    'Novoazovsk raion': 'Mariupol Raion',
    'Telmanove raion': 'Volnovakha Raion',
    'Stanychno-Luhansk raion': 'Luhansk Raion',
    'Slovianoserbsk raion': 'Sievierodonetsk Raion',
    'Lutuhynskyi raion': 'Luhansk Raion',
    "Lutuhyns'kyi raion": 'Luhansk Raion',
    'Krasnodon raion': 'Dovzhansk Raion',
    'Sloviansk raion': 'Kramatorsk Raion',
    'Perevalsk raion': 'Alchevsk Raion',
    'Toretsk raion': 'Bakhmut Raion',
    'Krasnoarmiiskyi raion': 'Pokrovsk Raion',
    'Antrasyt raion': 'Rovenky Raion',
    'Boykivskyi raion': None,  # Cannot map - unclear
    'Nikolske raion': 'Volnovakha Raion',
    'Kalmiuske raion': 'Kalmius Raion',
    'Kostiantynivka raion': 'Kramatorsk Raion',
    'Samar raion': None,  # Cannot map - unclear (may be Novomoskovsk)
    'Lysychanska raion': 'Sievierodonetsk Raion',
    'Bilovodsk raion': 'Starobilsk Raion',
    'Manhush raion': 'Mariupol Raion',
    'Dobropil raion': 'Pokrovsk Raion',
    'Shaktarsk City municipality': 'Donetsk Raion',
    'Berestyn raion': None,  # Cannot map - unclear
    'Kreminna raion': 'Sievierodonetsk Raion',
    'Sverdlovsk raion': 'Dovzhansk Raion',
    'Velyka Novosilka raion': 'Volnovakha Raion',
    'Torezka raion': 'Donetsk Raion',
    'Mezhova raion': 'Synelnykove Raion',
    'Briankivska raion': 'Alchevsk Raion',
    'Sheptytskyi raion': None,  # Cannot map - unclear
    'Bila Tserkva Raion': 'Bila Tserkva Raion',
    'Pervomaisk Raion': 'Pervomaisk Raion',
    'Vitovka Raion': 'Mykolaiv Raion',
    'Zhovtnevyi raion': 'Mykolaiv Raion',
    'Chaplynka raion': 'Kakhovka Raion',
    'Troitskiy raion': None,  # Cannot map - unclear
    # === Crimea raions (limited coverage, map where clear) ===
    'Yevpatoria raion': None,  # Crimea
    'Saky raion': None,  # Crimea
    'Yalta raion': None,  # Crimea
    'Feodosia raion': None,  # Crimea
    'Kirovske raion': None,  # Crimea
    'Simferopol Raion': None,  # Crimea
    'Nakhimov Raion': None,  # Sevastopol
    'Bakhchysarai raion': None,  # Crimea
    'Rozdolne raion': None,  # Crimea
    'Kerchenska raion': None,  # Crimea
    'Bilohirsk raion': None,  # Crimea
}


# Ukrainian raion names → English translations
# Source: https://en.wikipedia.org/wiki/Raions_of_Ukraine (post-2020 reform: 136 raions)

RAION_UA_TO_EN = {
    # Cherkasy Oblast
    'Звенигородський район': 'Zvenyhorodka Raion',
    'Золотоніський район': 'Zolotonosha Raion',
    'Уманський район': 'Uman Raion',
    'Черкаський район': 'Cherkasy Raion',
    # Chernihiv Oblast
    'Корюківський район': 'Koriukivka Raion',
    'Ніжинський район': 'Nizhyn Raion',
    'Новгород-Сіверський район': 'Novhorod-Siverskyi Raion',
    'Прилуцький район': 'Pryluky Raion',
    'Чернігівський район': 'Chernihiv Raion',
    # Chernivtsi Oblast
    'Вижницький район': 'Vyzhnytsia Raion',
    'Дністровський район': 'Dnistrovskyi Raion',
    'Чернівецький район': 'Chernivtsi Raion',
    # Dnipropetrovsk Oblast
    'Дніпровський район': 'Dnipro Raion',
    'Кам\'янський район': 'Kamianske Raion',
    'Криворізький район': 'Kryvyi Rih Raion',
    'Нікопольський район': 'Nikopol Raion',
    'Новомосковський район': 'Novomoskovsk Raion',
    'Павлоградський район': 'Pavlohrad Raion',
    'Синельниківський район': 'Synelnykove Raion',
    # Donetsk Oblast
    'Бахмутський район': 'Bakhmut Raion',
    'Волноваський район': 'Volnovakha Raion',
    'Горлівський район': 'Horlivka Raion',
    'Донецький район': 'Donetsk Raion',
    'Кальміуський район': 'Kalmius Raion',
    'Краматорський район': 'Kramatorsk Raion',
    'Маріупольський район': 'Mariupol Raion',
    'Покровський район': 'Pokrovsk Raion',
    # Ivano-Frankivsk Oblast
    'Верховинський район': 'Verkhovyna Raion',
    'Івано-Франківський район': 'Ivano-Frankivsk Raion',
    'Калуський район': 'Kalush Raion',
    'Коломийський район': 'Kolomyia Raion',
    'Косівський район': 'Kosiv Raion',
    'Надвірнянський район': 'Nadvirna Raion',
    # Kharkiv Oblast
    'Богодухівський район': 'Bohodukhiv Raion',
    'Ізюмський район': 'Izium Raion',
    'Красноградський район': 'Krasnohrad Raion',
    'Куп\'янський район': 'Kupiansk Raion',
    'Лозівський район': 'Lozova Raion',
    'Харківський район': 'Kharkiv Raion',
    'Чугуївський район': 'Chuhuiv Raion',
    # Kherson Oblast
    'Бериславський район': 'Beryslav Raion',
    'Генічеський район': 'Henichesk Raion',
    'Каховський район': 'Kakhovka Raion',
    'Скадовський район': 'Skadovsk Raion',
    'Херсонський район': 'Kherson Raion',
    # Khmelnytskyi Oblast
    'Кам\'янець-Подільський район': 'Kamianets-Podilskyi Raion',
    'Хмельницький район': 'Khmelnytskyi Raion',
    'Шепетівський район': 'Shepetivka Raion',
    # Kirovohrad Oblast
    'Голованівський район': 'Holovanivsk Raion',
    'Кропивницький район': 'Kropyvnytskyi Raion',
    'Новоукраїнський район': 'Novoukrainka Raion',
    'Олександрійський район': 'Oleksandriia Raion',
    # Kyiv Oblast
    'Білоцерківський район': 'Bila Tserkva Raion',
    'Бориспільський район': 'Boryspil Raion',
    'Броварський район': 'Brovary Raion',
    'Бучанський район': 'Bucha Raion',
    'Вишгородський район': 'Vyshhorod Raion',
    'Обухівський район': 'Obukhiv Raion',
    'Фастівський район': 'Fastiv Raion',
    # Luhansk Oblast
    'Алчевський район': 'Alchevsk Raion',
    'Довжанський район': 'Dovzhansk Raion',
    'Луганський район': 'Luhansk Raion',
    'Ровеньківський район': 'Rovenky Raion',
    'Сватівський район': 'Svatove Raion',
    'Сєвєродонецький район': 'Sievierodonetsk Raion',
    'Старобільський район': 'Starobilsk Raion',
    'Щастинський район': 'Shchastia Raion',
    # Lviv Oblast
    'Дрогобицький район': 'Drohobych Raion',
    'Золочівський район': 'Zolochiv Raion',
    'Львівський район': 'Lviv Raion',
    'Самбірський район': 'Sambir Raion',
    'Стрийський район': 'Stryi Raion',
    'Червоноградський район': 'Chervonohrad Raion',
    'Яворівський район': 'Yavoriv Raion',
    # Mykolaiv Oblast
    'Баштанський район': 'Bashtanka Raion',
    'Вознесенський район': 'Voznesensk Raion',
    'Миколаївський район': 'Mykolaiv Raion',
    'Первомайський район': 'Pervomaisk Raion',
    # Odesa Oblast
    'Білгород-Дністровський район': 'Bilhorod-Dnistrovskyi Raion',
    'Березівський район': 'Berezivka Raion',
    'Болградський район': 'Bolhrad Raion',
    'Ізмаїльський район': 'Izmail Raion',
    'Одеський район': 'Odesa Raion',
    'Подільський район': 'Podilsk Raion',
    'Роздільнянський район': 'Rozdilna Raion',
    # Poltava Oblast
    'Кременчуцький район': 'Kremenchuk Raion',
    'Лубенський район': 'Lubny Raion',
    'Миргородський район': 'Myrhorod Raion',
    'Полтавський район': 'Poltava Raion',
    # Rivne Oblast
    'Вараський район': 'Varash Raion',
    'Дубенський район': 'Dubno Raion',
    'Рівненський район': 'Rivne Raion',
    'Сарненський район': 'Sarny Raion',
    # Sumy Oblast
    'Конотопський район': 'Konotop Raion',
    'Охтирський район': 'Okhtyrka Raion',
    'Роменський район': 'Romny Raion',
    'Сумський район': 'Sumy Raion',
    'Шосткинський район': 'Shostka Raion',
    # Ternopil Oblast
    'Кременецький район': 'Kremenets Raion',
    'Тернопільський район': 'Ternopil Raion',
    'Чортківський район': 'Chortkiv Raion',
    # Vinnytsia Oblast
    'Вінницький район': 'Vinnytsia Raion',
    'Гайсинський район': 'Haisyn Raion',
    'Жмеринський район': 'Zhmerynka Raion',
    'Могилів-Подільський район': 'Mohyliv-Podilskyi Raion',
    'Тульчинський район': 'Tulchyn Raion',
    'Хмільницький район': 'Khmilnyk Raion',
    # Volyn Oblast
    'Володимирський район': 'Volodymyr Raion',
    'Камінь-Каширський район': 'Kamin-Kashyrskyi Raion',
    'Ковельський район': 'Kovel Raion',
    'Луцький район': 'Lutsk Raion',
    # Zakarpattia Oblast
    'Берегівський район': 'Berehove Raion',
    'Мукачівський район': 'Mukachevo Raion',
    'Рахівський район': 'Rakhiv Raion',
    'Тячівський район': 'Tiachiv Raion',
    'Ужгородський район': 'Uzhhorod Raion',
    'Хустський район': 'Khust Raion',
    # Zaporizhzhia Oblast
    'Бердянський район': 'Berdiansk Raion',
    'Василівський район': 'Vasylivka Raion',
    'Запорізький район': 'Zaporizhzhia Raion',
    'Мелітопольський район': 'Melitopol Raion',
    'Пологівський район': 'Polohy Raion',
    # Zhytomyr Oblast
    'Бердичівський район': 'Berdychiv Raion',
    'Житомирський район': 'Zhytomyr Raion',
    'Звягельський район': 'Zviaghel Raion',
    'Коростенський район': 'Korosten Raion',
}
