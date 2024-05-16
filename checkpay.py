import requests

#https://www.zarinpal.com/pg/StartPay/A00000000000000000000000000536494960

def check_pay(authority,amount):
# مقادیر مورد نیاز شما
    merchant_id = '7aa08ed2-ff34-44d4-867b-d918676f856f'
    # authority = 'A00000000000000000000000000536494960'

    # URL آدرس API زرین پال
    url = 'https://api.zarinpal.com/pg/v4/payment/verify.json'

    # پارامتر‌های ارسالی به زرین پال
    payload = {
        'merchant_id': merchant_id,
        'authority': authority,
        'amount': amount  # مبلغ به ریال
    }

    # درخواست بررسی وضعیت پرداخت
    response = requests.post(url,json=payload)

    if response.status_code == 200:
        # اگر درخواست با موفقیت انجام شد
        response_data = response.json()
        print(response_data)
        if response_data['data']['code'] == 100:
            # پرداخت موفق بوده است
            print('Payment is verified.')
            return {"data":"yes","card_pan":response_data['data']['card_pan']}


        elif response_data['data']['code'] == 101:
            return {"data":"againcheck"}
        
        else:
            
            # پرداخت ناموفق بوده است
            print('Payment verification failed.')
            return {"data":"nopay"}
    else:
        # در صورت خطا
        print('Request failed with status code:', response.status_code)
        return {"data":"nopay"}


"""
PS D:\work\translate2> & d:/work/translate2/myy/Scripts/python.exe d:/work/translate2/checkpay.py
{'data': {'code': 100, 'message': 'Paid', 'card_hash': 'E025B7BF8C848C3D1AA62E21A1D61E455B5E337B4819BC61BFA5CA6D8301BDAF', 'card_pan': '603799******1670', 'ref_id': 53649496001, 'fee_type': 'Merchant', 'fee': 3500, 'order_id': None}, 'errors': []}
Payment is verified.
PS D:\work\translate2> & d:/work/translate2/myy/Scripts/python.exe d:/work/translate2/checkpay.py
{'data': {'code': 101, 'message': 'Verified', 'card_hash': 'E025B7BF8C848C3D1AA62E21A1D61E455B5E337B4819BC61BFA5CA6D8301BDAF', 'card_pan': '603799******1670', 'ref_id': 53649496001, 'fee_type': 'Merchant', 'fee': 3500, 'order_id': None}, 'errors': []}
Payment verification failed.
PS D:\work\translate2> 

"""


"""
def is_powerful(n):
	list_number=[]
	if n%2==0:
		list_number.append(2)
	for i in range(3,10,2):
		if n%i==0:
			list_number.append(i)
	for i n list_number:
		if n%(i**2)==0:
			
"""
