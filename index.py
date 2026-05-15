from weasyprint import HTML

html_content = """
<!DOCTYPE html>
<html lang="ta">
<head>
    <meta charset="UTF-8">
    <style>
        @page {
            size: A4;
            margin: 12mm;
            @bottom-center {
                content: counter(page);
                font-family: 'Arial', sans-serif;
                font-size: 11pt;
            }
        }
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.35;
            color: #000;
            margin: 0;
            padding: 0;
        }
        .header {
            text-align: center;
            margin-bottom: 8px;
        }
        .header-en { font-size: 13pt; margin: 0; font-weight: normal; }
        .header-ta { font-size: 17pt; margin: 1px 0; font-weight: bold; }
        .header-sub { font-size: 12pt; margin: 1px 0; }
        
        .info-container {
            width: 100%;
            margin-bottom: 12px;
        }
        .info-row {
            display: flex;
            justify-content: space-between;
            border: 1px solid #000;
            padding: 4px 10px;
        }
        .info-row div { width: 50%; }
        .name-row {
            border: 1px solid #000;
            border-top: none;
            padding: 4px 10px;
        }

        .section-header {
            font-weight: bold;
            margin-top: 12px;
            margin-bottom: 6px;
            font-size: 11.5pt;
        }
        .question-block {
            margin-left: 5px;
            margin-bottom: 10px;
            page-break-inside: avoid;
        }
        .q-text { display: block; margin-bottom: 3px; }
        .options-row {
            display: flex;
            justify-content: flex-start;
            gap: 35px;
            margin-left: 25px;
        }
        .write-space {
            border-bottom: 1px dotted #000;
            height: 22px;
            margin-top: 4px;
            width: 98%;
        }
        .passage-box {
            border: 1px solid #000;
            padding: 12px;
            margin: 8px 0;
            font-size: 11pt;
            text-align: justify;
            page-break-inside: avoid;
        }
        /* Prevents section headers from being alone at the bottom */
        .section-header { page-break-after: avoid; }
    </style>
</head>
<body>
    <div class="header">
        <p class="header-ta">அமெரிக்கத் தமிழ்க் கல்விக்கழகம்</p>
        <p class="header-en">American Tamil Academy</p>
        <p class="header-sub">மூன்றாம் பருவத் தேர்வு 2025-26</p>
        <p class="header-sub">நிலை - 7</p>
    </div>

    <div class="info-container">
        <div class="info-row">
            <div>மொத்த மதிப்பெண்-100</div>
            <div>காலம் -2.00 மணி</div>
        </div>
        <div class="info-row" style="border-top: none;">
            <div>எழுத்துத் தேர்வு-80</div>
            <div>வாய்மொழித்தேர்வு-20</div>
        </div>
        <div class="name-row">
            <div>பெயர் - _________________________________ &nbsp;&nbsp;&nbsp;&nbsp; பெற்ற மதிப்பெண்- ________</div>
        </div>
    </div>

    <div class="section-header">I. சரியான விடையைத் தேர்ந்தெடுத்து எழுதுக. (5)</div>
    <div class="question-block">
        <span class="q-text">1. சந்திரயான் - 1 செயற்கைக்கோள், நிலவில் ________ உள்ளதா என ஆய்வை மேற்கொண்டது?</span>
        <div class="options-row">
            <span>அ) நெருப்பு</span> <span>ஆ) தண்ணீர்</span> <span>இ) காற்று</span>
        </div>
    </div>
    <div class="question-block">
        <span class="q-text">2. இளைஞர்களின் அறிவியல் திசைகாட்டி யார்?</span>
        <div class="options-row">
            <span>அ) சி.வி.இராமன்</span> <span>ஆ) அப்துல் கலாம்</span> <span>இ) மயில்சாமி அண்ணாதுரை</span>
        </div>
    </div>
    <div class="question-block">
        <span class="q-text">3. மயில்சாமி அண்ணாதுரை எத்தனை முனைவர் பட்டம் பெற்றார்?</span>
        <div class="options-row">
            <span>அ) 7</span> <span>ஆ) 67</span> <span>இ) 5</span> <span>ஈ) 4</span>
        </div>
    </div>
    <div class="question-block">
        <span class="q-text">4. ஏ.ஆர். ரகுமானின் இயற்பெயர் என்ன?</span>
        <div class="options-row">
            <span>அ) சேகர்</span> <span>ஆ) ராஜகோபால்</span> <span>இ) திலீப்குமார்</span>
        </div>
    </div>
    <div class="question-block">
        <span class="q-text">5. சர் சி.வி. ராமன் எந்த துறையில் நோபல் பரிசு பெற்றார்?</span>
        <div class="options-row">
            <span>அ) இயற்பியல்</span> <span>ஆ) அறிவியல்</span> <span>இ) வேதியியல்</span>
        </div>
    </div>

    <div class="section-header">II. கோடிட்ட இடங்களை நிரப்புக. (5)</div>
    <div class="question-block">1. மயில்சாமி அண்ணாதுரை பிறந்த ஊர் ________________ ஆகும்.</div>
    <div class="question-block">2. பிப்ரவரி 28 - ஆம் நாள் உலக ________________ தினமாகக் கொண்டாடப்படுகிறது.</div>
    <div class="question-block">3. இசைப்புயல் என்று அனைவராலும் அழைக்கப்படுபவர் ________________.</div>
    <div class="question-block">4. இராமனுக்கு "சர்" பட்டம் வழங்கிய அரசு ________________.</div>
    <div class="question-block">5. சர் சி.வி. ராமன் ________________ குடும்பத்தில் பிறந்தார்.</div>

    <div class="section-header">III. சேர்த்து எழுதுக. (5)</div>
    <div class="question-block">1. நீச்சல் + அடி = ________________</div>
    <div class="question-block">2. வேற்றுமை + படு = ________________</div>
    <div class="question-block">3. தயார் + இரு = ________________</div>
    <div class="question-block">4. கட்டுப்பாடு + படு = ________________</div>
    <div class="question-block">5. கூச்சல் + இடு = ________________</div>

    <div class="section-header">IV. பிறமொழிச் சொற்களுக்கு இணையான தமிழ்ச் சொற்களை எழுதுக. (5)</div>
    <div class="question-block">1. Translate to English: நுண்செயலி: ________________</div>
    <div class="question-block">2. Translate to English: தொலையுணர்வு: ________________</div>
    <div class="question-block">3. Translate to Tamil: Space: ________________</div>
    <div class="question-block">4. Translate to Tamil: Achievement: ________________</div>
    <div class="question-block">5. Translate to Tamil: Research: ________________</div>

    <div class="section-header">V. கூட்டு வினையைப் பயன்படுத்தி தொடரமைக்க. (10)</div>
    <div class="question-block">1. கண்டுபிடி: <div class="write-space"></div></div>
    <div class="question-block">2. தந்தியடி: <div class="write-space"></div></div>
    <div class="question-block">3. ஆசைப்படு: <div class="write-space"></div></div>
    <div class="question-block">4. சரிபார்: <div class="write-space"></div></div>
    <div class="question-block">5. உருவாக்கு: <div class="write-space"></div></div>
    <div class="question-block">6. அடிபடு: <div class="write-space"></div></div>
    <div class="question-block">7. தெரியப்படுத்து: <div class="write-space"></div></div>
    <div class="question-block">8. வழிகாட்டு: <div class="write-space"></div></div>
    <div class="question-block">9. உதவிசெய்: <div class="write-space"></div></div>
    <div class="question-block">10. பாராட்டு: <div class="write-space"></div></div>

    <div class="section-header">VI. தொடரமைத்து எழுதுக. (5)</div>
    <p style="font-size: 9pt; margin-left: 5px;">(ஒவ்வொரு சொல்லுக்கும் 6 சொற்கள் கொண்ட வாக்கியம் அமைக்கவும்)</p>
    <div class="question-block">1. விண்வெளி: <div class="write-space"></div></div>
    <div class="question-block">2. முன்னேற்றம்: <div class="write-space"></div></div>
    <div class="question-block">3. ஆசிரியர்: <div class="write-space"></div></div>
    <div class="question-block">4. உலகம்: <div class="write-space"></div></div>
    <div class="question-block">5. சந்தோஷம்: <div class="write-space"></div></div>

    <div class="section-header">VII. கீழே உள்ள வாக்கியங்களை மொழிப்பெயர்க்கவும். (10)</div>
    <div class="question-block">1. The sun rises in the east. <div class="write-space"></div></div>
    <div class="question-block">2. I like to read books. <div class="write-space"></div></div>
    <div class="question-block">3. Science is a very interesting subject. <div class="write-space"></div></div>
    <div class="question-block">4. My school is near my house. <div class="write-space"></div></div>
    <div class="question-block">5. We must protect our nature. <div class="write-space"></div></div>

    <div class="section-header">VIII. ஒரு திருக்குறள் மற்றும் அதன் விளக்கம் எழுதவும். (5)</div>
    <div class="question-block">திருக்குறள்: <div class="write-space"></div><div class="write-space"></div></div>
    <div class="question-block">விளக்கம்: <div class="write-space"></div><div class="write-space"></div></div>

    <div class="section-header" style="page-break-before: always;">IX. மொழிப்பெயர்க்க. (10)</div>
    <div class="passage-box">
        தமிழகத்தில் பல அறிஞர்கள் பிறந்துள்ளனர். அவர்கள் தமிழுக்கும் அறிவியலுக்கும் பெரும் தொண்டு செய்துள்ளனர். கல்வி கற்பது ஒரு சிறந்த பண்பாகும். மாணவர்கள் விடாமுயற்சியுடன் படிக்க வேண்டும். அப்போதுதான் வாழ்வில் பெரிய சாதனைகளைச் செய்ய முடியும்.
    </div>
    <div class="write-space"></div><div class="write-space"></div><div class="write-space"></div><div class="write-space"></div>

    <div class="section-header">X. பத்தியைப் படித்து வினாக்களுக்கு விடையளி. (10)</div>
    <div class="passage-box">
        ஏ.ஆர். ரகுமான் உலகப் புகழ்பெற்ற இந்திய இசையமைப்பாளர். இவர் சென்னையில் பிறந்தார். சிறுவயதிலேயே இசை ஆர்வத்துடன் வளர்ந்தார். இவருக்குப் பியானோ, கிதார் போன்ற பல இசைக்கருவிகள் வாசிக்கத் தெரியும். இவரது முதல் படம் 'ரோஜா'. இந்தப் படத்திற்காக தேசிய விருது பெற்றார். ஆசியாவிலேயே சிறந்த தொழில்நுட்ப வசதிகள் கொண்ட ஏ.எம். ஸ்டுடியோவை இவர்தான் நிறுவினார். இவர் இரண்டு ஆஸ்கார் விருதுகளை வென்று இந்தியாவிற்குப் பெருமை சேர்த்தார். இவரது இசை இளையவர்களையும் முதியவர்களையும் கவரும் தன்மை கொண்டது. இந்தியத் திரையிசையில் பெரும் மாற்றத்தைக் கொண்டு வந்தார்.
    </div>
    <div class="question-block">1. ஏ.ஆர். ரகுமான் எங்கு பிறந்தார்? <div class="write-space"></div></div>
    <div class="question-block">2. ரகுமான் வாசிக்கத் தெரிந்த இசைக்கருவிகள் எவை? <div class="write-space"></div></div>
    <div class="question-block">3. ரகுமானின் முதல் படத்தின் பெயர் என்ன? <div class="write-space"></div></div>
    <div class="question-block">4. அவர் எத்தனை ஆஸ்கார் விருதுகளை வென்றார்? <div class="write-space"></div></div>
    <div class="question-block">5. ஏ.எம். ஸ்டுடியோவின் சிறப்பு என்ன? <div class="write-space"></div></div>

    <div class="section-header">XI. உனக்குப் பிடித்த தலைப்பில் கட்டுரை எழுதுக. (10)</div>
    <div class="question-block">
        கீழே உள்ள ஏதாவது ஒரு தலைப்பில் கட்டுரை வரைக:<br>
        1. ஏ.ஆர். ரகுமான் (A.R. Rahman) <br>
        2. இளையராஜா (Ilaiyaraaja) <br>
        3. சர். சி. வி. இராமன் (Sir. C. V. Raman) <br>
        4. ஏ.பி.ஜே. அப்துல் கலாம் (A.P.J. Abdul Kalam)
    </div>
    <div class="write-space"></div><div class="write-space"></div><div class="write-space"></div><div class="write-space"></div><div class="write-space"></div>
    <div class="write-space"></div><div class="write-space"></div><div class="write-space"></div><div class="write-space"></div><div class="write-space"></div>
    <div class="write-space"></div><div class="write-space"></div><div class="write-space"></div>

</body>
</html>
"""

HTML(string=html_content).write_pdf("Tamil_Test_Nilai7_Fixed.pdf")
