# Conspiracy RELAX NG

First

```
Find:&
Replace with:&amp;
```
```
Find:<
Replace with:&lt;
```
```
Find:>
Replace with:&gt;
```

Fixing Format (dot matches all on)
```
Find:^\s+
Replace with:
```
```
Find:\s+$
Replace with: 
```
```
Find: {2,}
Replace with: 
```

Delete unnecessary dividers:
Dot Matches All On:
```
Find:#{4,}
Replace with:<div>
```
```
Find:\*{4,}
Replace with:<div>
```
```
Find:={4,}
Replace with:<div>
```
```
Find:-{4,}
Replace with:<div>
```
```
Find:_{3,}
Replace with:<div>
```
```
Find:~{3,}
Replace with:<div>
```
```
Find:\+{3,}
Replace with:<div>
```
```
Find:\| ?
Replace with:
```

Put tag around whole file:
```
Find:.+
Replace with:<conspiracyFile>\0</conspiracyFile>
```

Finding Phone Numbers:
```
Find:\(?\d{3}-?\)? ?\d{3}-?\d{4}
Replace with:<data type="phoneNumber">\0</digit>
```

Fixing number format:
Find: `(\d+?) 1/2`
Replace with: `\1.5`

Find: `(\d+?) 1/8`
Replace with: `\1.125`

Find: `(\d+?) 3/4`
Replace with: `\1.75`

Finding percentages:
```
Find:\d*-*\d*\.?\d+%
Replace with: <data type="percent" unit="%">\0</data>
```

Changing Digit Format

Millions:
```
Find:(\d+)\.(\d+)\s+?million
Replace with: \1\200000
```
```
Find:(\d+)\s+?million
Replace with: \1000000
```
```
Find:(\d+)(-\d000000)
Replace with: \1000000\2
```

Billions:
```
Find:(\d+)\.(\d+)\s+?billion
Replace with:\1\200000000
```
```
Find:(\d+)\,(\d+)\s+?billion
Replace with:\1\2000000000
```
```
Find:(\d+)\s+?billion
Replace with:\1000000000
```
```
Find:(\d+)(-\d000000000)
Replace with:\1000000000\2
```

Trillions:
```
Find:(\d+)\.(\d+)\strillion
Replace with:\1\200000000000
```
```
Find:(\d+)?,?(\d+)\s?trillion
Replace with:\1\2000000000000
```

Delete commas in digits:
```
Find:(\d{1,3}),(\d{3}),?(\d{3})?,?(\d{3})?
Replace with:\1\2\3
```

Find ISBN:
```
Find:\d+-\d+-\d+-\d+
Replace with:<data type="ISBN">\0</data>
```

Finding Time:
```
Find:(\d+:\d{2,}:\d{2,})\s+([A-Z]{3})
Replace with:<data type="time" timezone="\2">\1</data>
```
```
Find:(\d{2}:\d{2}:\d{2})\s+
Replace with:<data type="time">\1</data>
```


Finding different conspiracy groups

Illuminati
New World Order
C&amp;SL
NASA
UFO
Unidentified Flying Object
CNN
TAX
AIDS
HIV
CAIB
CIA
US
USA
WHO
World Health Organization
POW
Prisoner(s( of War
WWIII
World War III
WWII
World War II
WWI
World War I
FBI
IBM
NCR
BCD
Mafia
UN
Drug
USSR
NCI
FDC
FAO
Food and Agriculture Organization
IDA
IMF
International Monetary Fund
