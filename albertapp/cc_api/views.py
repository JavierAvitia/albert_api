from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

#
# Helper Dicts
#
major_industry_dict = {
	1:'Airlines (Diners Club enRoute)',
	2:'Airlines (Diners Club enRoute)',
	3:"Travel & Entertainment (non-banks such as American Express, Diner's Club, JCB, and Carte Blanche)",
	4:'Banking & Financial (Visa, Switch, and Electron)',
	5:'Banking & Financial (Mastercard and Bankcard)',
	6:'Merchandising & Finance (Discover Card, Laser, Solo, Switch, and China UnionPay)',
	7:'Petroleum',
	8:'Telecommunications',
	9:'National Assignment',
}

#
# Defaults
#
def albert_home(request):
    return HttpResponse("Hello! Welcome to the Albert Credit Card API.")

def redirect_404(request,exception):
	return HttpResponse("Sorry! Your request was invalid. Please try again.")

def redirect_500(request):
	return HttpResponse("Zoinks! It appears the server timed out. Please check your internet connection or try again.")

#
# Helper Functions
#
def validate_cc_len(cc,return_string=False):

	# Check for string flag & construct CC# comparison list
	cc_list =  [d for d in str(cc)]

	# Verify CC# length
	if len(cc_list) < 6 or len(cc_list) > 19:
		return []
	else:
		return cc_list

#
# Views
#
@csrf_exempt
def validate_cc(request,function_flag=False):

	# Parse POST request
	valid_flag = True
	met = request.method
	cc_num = request.POST.get('cc_num',None)

	# Check variables
	num_list = validate_cc_len(cc_num)

	# Confirm valid credit card #
	if met != 'POST':
		valid_flag = False

	elif not cc_num:
		valid_flag = False

	elif not num_list:
		valid_flag = False

	else:

		# Luhn Mod-10 validation variables
		slice_idx = len(num_list) - 1
		check_digit = num_list[slice_idx:][0]
		num_slice = num_list[:slice_idx]
		num_slice.reverse()
		cc_even = []
		cc_odd = []

		# Calculate comparison sum
		for idx,num in enumerate(num_slice):

			# Convert to integer
			num = int(num)

			# Check position
			if idx % 2 == 0:
				n = num * 2
				tmp_list = [int(d) for d in str(n)]

				if len(tmp_list) > 1:
					n = sum(tmp_list)

				cc_even.append(n)

			else:
				cc_odd.append(num)
		cc_sum = sum(cc_even + cc_odd)

		# Verify Luhn Algorithm
		test_digit = 10 - (( cc_sum % 10 ) % 10)

		# Compare to Check Digit
		if int(test_digit) != int(check_digit):
			valid_flag = False

	# Return response
	if not valid_flag:
		res_dict = {'valid_cc':'false'}
	else:
		res_dict = {'valid_cc':'true'}

	# Check for function flag & return response
	if function_flag:
		return num_list, res_dict
	else:
		return JsonResponse(res_dict)

@csrf_exempt
def get_mii(request):

	# Check variables
	valid_flag = True
	num_list, valid_check_dict = validate_cc(request, function_flag=True)

	# Confirm valid credit card #
	if valid_check_dict['valid_cc'] != 'true':
		valid_flag = False
	elif not num_list:
		valid_flag = False
	else:
		mii = num_list[:1][0]

	# Return response
	if not valid_flag:
		return JsonResponse(valid_check_dict)
	else:
		return JsonResponse({'mii':mii,'major_industry':major_industry_dict[int(mii)]})

@csrf_exempt
def get_iin(request):

	# Check variables
	valid_flag = True
	num_list, valid_check_dict = validate_cc(request, function_flag=True)

	# Confirm valid credit card
	if valid_check_dict['valid_cc'] != 'true':
		valid_flag = False
	elif not num_list:
		valid_flag = False
	else:
		iin = ''.join(num_list[:6])

	# Return response
	if not valid_flag:
		return JsonResponse(valid_check_dict)
	else:
		return JsonResponse({'iin':iin})

@csrf_exempt
def get_account_number(request):

	# Check variables
	valid_flag = True
	num_list, valid_check_dict = validate_cc(request, function_flag=True)

	# Confirm valid credit card #
	if valid_check_dict['valid_cc'] != 'true':
		valid_flag = False
	elif not num_list:
		valid_flag = False
	else:
		slice_idx = len(num_list) - 1
		account_number = ''.join(num_list[6:slice_idx])

	# Return response
	if not valid_flag:
		return JsonResponse(valid_check_dict)
	else:
		return JsonResponse({'account_number':account_number})

@csrf_exempt
def get_check_digit(request):

	# Check variables
	valid_flag = True
	num_list, valid_check_dict = validate_cc(request, function_flag=True)

	# Confirm valid credit card #
	if valid_check_dict['valid_cc'] != 'true':
		valid_flag = False
	elif not num_list:
		valid_flag = False
	else:
		slice_idx = len(num_list) - 1
		check_digit = num_list[slice_idx:][0]

	# Return response
	if not valid_flag:
		return JsonResponse(valid_check_dict)
	else:
		return JsonResponse({'check_digit':check_digit})