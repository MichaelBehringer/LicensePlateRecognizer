# LicensePlateRecognizer
## Installation Windows (local Recognition)

 1. git clone https://github.com/MichaelBehringer/LicensePlateRecognizer.git
 2. pip install opencv-python
 3. pip install imutils
 4. pip install pytesseract
 5. install https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.2.0.20220708.exe
 6. add the tesseract installation path (C:\Program Files\Tesseract-OCR) to your PATH-Variable
 7. cd pi
 8. python recognizer.py
(tested with python 3.9.x)
## Installation (API Recognition)
 1. pip install requests
 2. cd pi
 3. python apiRecognizer.py
(tested with python 3.9.x)
## Api:
URL: https://platerecognizer.com/
Token: (FÜNF)e52f71a0abd5e1c22900d2882effd115a058ab(ACHT)
Pricing: Free
Calls: 2500/month (max: 1/second)
Doc: https://docs.platerecognizer.com/
