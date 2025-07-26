#pip install qrcode in terminal 
#pip install pillow in terminal
import qrcode
#Take UPI id as input
upi_id=input("Enter the UPI ID: \n")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE      -PAYMENT URL FORMAT
#Defining the payment url based on UPI ID and payment app(modification allowed)

phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'    #mc=Merchant Code
googlepay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create qr codes for each url
phonepe_qr=qrcode.make(phonepe_url)
googlepay_qr=qrcode.make(googlepay_url)
paytm_qr=qrcode.make(paytm_url)

#Save the qr code in image format
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm.png")
googlepay_qr.save("googlepay_qr.png")

#Display QR code
phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()