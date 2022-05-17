from collections import defaultdict
from django.shortcuts import render
from django.http import JsonResponse
from decimal import Decimal
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

from ressources.models import Salary , Category ,Depency 
from .serializers import DepencySerializer2, SalarySerializer ,CategorySerializer,DepencySerializer

from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer
from api import serializers

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import logout
import datetime
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

# Create your views here.

# Login Api
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'token': 'notFound'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
	

    return Response({'token': token.key, 'user': serializer.data },
                    status=HTTP_200_OK)

# Register API


@permission_classes((AllowAny,))
class RegisterAPI(generics.GenericAPIView):
	serializer_class = RegisterSerializer
	
	@csrf_exempt
	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		
		user = serializer.save()
		token, _ = Token.objects.get_or_create(user=user)
		# return Response({"ms":user})
	# 	return Response({
    #     "user": UserSerializer(user, context=self.get_serializer_context()).data,
    #     "token": Token.objects.get_or_create(user=user)
    #    })
		return Response({'token': token.key},
                    status=HTTP_200_OK)

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
"api/": "api-overview",
# "_____________________":"_______Salary____________",
"api/salary-list/" : "salary-list",
"api/ salary-detail/pk/":"salary-detail",
"api/salary-create/": "salary-create",
"api/salary-update/pk/": "salary-update",
"api/salary-delete/pk/":"salary-delete",
# "_____________________":"_______category____________",
"api/ category-list/" : "category-list",
"api/ category-detail/pk/ ":"category-detail",
"api/ category-create/": "category-create",
"api/ category-update/pk/":"category-update",
"api/ category-delete/pk/ ":"category-delete",
#"_____________________":"________depency___________",
"api/ depency-list/ ":" depency-list",
"api/ depency-detail/pk/ ":" depency-detail",
"api/ depency-add/ ":" depency-add",
#"_____________________":"________register___________",
"api/ register/ ":"register",
#"_____________________":"________dashbord___________",
"api/ dashboard/ ":" dashbord.get"}
	return Response(api_urls)


@api_view(['GET'])
def salaryList(request):
	user=0
	if request.user.is_authenticated:
		user = request.user
	# checking for the parameters from the URL
	if request.query_params:
		salarys = Salary.objects.filter(**request.query_params.dict())
	else:
		print(user)
		salarys = Salary.objects.filter(user=user).order_by('-id')

	# if there is something in items else raise error
	if salarys:
		serializer = SalarySerializer(salarys, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

	
class SalaryUser(generics.ListAPIView):
    serializer_class = SalarySerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        # user = self.request.user
        return Salary.objects.filter(user_id=1)    
       
@api_view(['POST'])
def salaryCreate(request):
    salary = SalarySerializer(data=request.data)
  
    # validating for already existing data
    if Salary.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if salary.is_valid():
        salary.save()
        return Response(salary.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def salaryUpdate(request, pk):
	salary = Salary.objects.get(id=pk)
	serializer = SalarySerializer(instance=salary, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def salaryDelete(request, pk):
	salary = Salary.objects.get(id=pk)
	salary.delete()
	return Response('Item succsesfully delete!')

# Category Crud
@api_view(['GET'])
def categoryList(request):
	user=0
	if request.user.is_authenticated:
		user = request.user
	print(user)
	categorys = Category.objects.filter(user=user).order_by('-id')
	serializer = CategorySerializer(categorys, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def categoryDetail(request, pk):
	user=0
	if request.user.is_authenticated:
		user = request.user
	category = Category.objects.get(id=pk,user=user)
	serializer = CategorySerializer(category, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def categoryCreate(request):
	serializer = CategorySerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['POST'])
def categoryUpdate(request, pk):
	category = Category.objects.get(id=pk)
	serializer = CategorySerializer(instance=category, data=request.data)

	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['DELETE'])
def categoryDelete(request, pk):
	user=0
	if request.user.is_authenticated:
		user = request.user
	category = Category.objects.get(id=pk,user=user)
	category.delete()
	return Response('Item succsesfully delete!')

# Depency Add

@api_view(['GET'])
def depencyList(request):
	user=0
	if request.user.is_authenticated:
		user = request.user
	depency = Depency.objects.filter(user=user).order_by('-id')
	serializer = DepencySerializer2(depency, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def depencyDetail(request, pk):
	user=0
	if request.user.is_authenticated:
		user = request.user
	depency = Depency.objects.get(id=pk ,user=user)
	
	serializer = DepencySerializer(depency, many=False)
	# serializer = SalarySerializer(salary, many=False)
	return Response(serializer.data )

@api_view(['PUT'])
def depencyAdd(request):
	serializer = DepencySerializer(data=request.data)

	if serializer.is_valid():
		salary = Salary.objects.get(id=serializer.data['salary']).amount
		category = Category.objects.get(id=serializer.data['category'])
		# depance  toltal pour ce mois
		depency_month = sum(Depency.objects.values_list('amount' ,flat=True).filter(salary=serializer.data['salary']) ) +  Decimal(serializer.data['amount'])

		depency_month=sum(Depency.objects.values_list('amount' ,flat=True).filter(salary=serializer.data['salary'])) +  Decimal(serializer.data['amount'])
		
		# depance sur mois pour cette categori

		depency_month_category=sum(Depency.objects.values_list('amount' ,flat=True).filter(category=serializer.data['category'],salary=serializer.data['salary'])) +  Decimal(serializer.data['amount'])

        # si la depence total de ce mois dépasse le salaire
		if salary < depency_month :
			return Response({"salary_exceeds": depency_month-salary,"code":3 })


		# si la depence total sur categorie   dépasse le max fixe max amout
		
		# si la depence total sur categorie   dépasse le max fixe (max amout)
		elif depency_month_category  > category.max_amount :
			return Response({"category_exceeds": depency_month_category-category.max_amount,
			"code":2 })
		
		else:
			# si tout est ok
			category=serializer.validated_data.get('category')
			amount=serializer.validated_data.get('amount')
			salary=serializer.validated_data.get('salary')
            
			try:
				#verivier si la depeence sur ce categori exist (cas update)
				depency= Depency.objects.get(category=serializer.data['category'],salary=serializer.data['salary'])
				depency.amount = depency.amount +amount
				print("cas update")
				depency.date=datetime.datetime.now().strftime("%d-%m-%y %H:%M")  
				depency.save()
				return Response({'message':'saved',"code":1})
			except:
				print("cas create")
				#si la depeence sur ce categori ne  exist pas  (cas create)
				depency = Depency()
				depency.category=category
				depency.salary=salary
				depency.amount=amount
				depency.user=request.user
				depency.date=datetime.datetime.now().strftime("%d-%m-%y %H:%M")
				depency.save()
				return Response({'message':'saved',"code":1})

					
			
	else:

		return Response({"message":'not valide',"code":4})


# Dashbord
@api_view(['GET'])
def Dashboard(request):
	#user
	user=0
	if request.user.is_authenticated:
		user = request.user
		print(user)
	#recuperation du salaire actuel
	salary = Salary.objects.filter(user=user).latest('date')
	
	#mount pour ce mois
	amount=salary.amount
	
	#depace tatal pour ce mois
	depency_month=sum(Depency.objects.values_list('amount' ,flat=True).filter(salary=salary.id))
    
	#max amount
	max_amount_total=sum(Category.objects.values_list('max_amount' ,flat=True))

	resume = {'salary':amount, 'depence total':depency_month, 'max_amount_total':max_amount_total}

	#serializer = SalarySerializer(salary , many=False)
    
	#category with depence pour ce mois
	depencys = Depency.objects.filter(salary=salary).values('category' ,'amount')
	
    #category with max_amount ,label
	list_max_amount_category=[]
	for list_item in depencys:
		depency =Category.objects.filter(id=list_item['category']).values('id','max_amount','label')
		list_max_amount_category.append(depency)
	
	# converter la liste list_max_amout_category en liste de dictionnaire
	list_max_amount_category_serialise = []
	for i in list_max_amount_category:
		for j in i:
			list_max_amount_category_serialise.append(j)
    
	#covert id to 'category' pour la joiture
	for d in list_max_amount_category_serialise:
		d['category'] = d.pop('id')
	
	#JOITURE des list depence avec caegory
	d = defaultdict(dict)
	for l in (depencys, list_max_amount_category_serialise):
		for elem in l:
			d[elem['category']].update(elem)
	detailler = d.values()
	
	
	response={
		'resumer':resume,
		'detailler':detailler
	}

	
	return Response(response)
	#test unitaire
	#return Response(list_max_amount_category_serialise)
	#return Response(resume)
	#return Response(depencys)

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def logout(request):

	request.user.auth_token.delete()

	# logout(request)

	return Response({'message':'you are lougout'})
    