# Receipts_ExtractionFromImageService
## วิธีใช้
1. ติดตั้งโปรแกรม tesseract ocr 
- Microsoft Windows ---> https://linuxhint.com/install-tesseract-windows/
- Mac OS ---> https://www.oreilly.com/library/view/building-computer-vision/9781838644673/95de5b35-436b-4668-8ca2-44970a6e2924.xhtml
- Ubuntu ---> https://techviewleo.com/how-to-install-tesseract-ocr-on-ubuntu/
2. ติดตั้ง python3 (แนะนำให้เป็น version 3.8)
3. รันคำสั่ง pip install -r library_list.txt
4. รันคำสั่ง uvicorn app:app --workers 8 --host 0.0.0.0 --port 8081
5. ทดสอบการใช้ด้วย localhost:8081/docs (ใช้ใน browser)