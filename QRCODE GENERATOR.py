import qrcode
upi_id = input("Enter your UPI ID=")
phnpe_url = f'upi://pay?pa={upi_id}&pn= Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
gpay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

phnpe_qr = qrcode.make(phnpe_url)
paytm_qr = qrcode.make(paytm_url)
gpay_qr = qrcode.make(gpay_url) 

phnpe_qr.save('phnpe_qr.png')
paytm_qr.save('paytm_qr.png')
gpay_qr.save('gpay_qr.png') 

phnpe_qr.show() 
paytm_qr.show()
gpay_qr.show()  