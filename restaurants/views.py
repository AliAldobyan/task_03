from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {"my_list": [
            {

                "restaurant_name":'McDonald\'s',
                "food_type":'american food'
            },
            {
                "restaurant_name" : 'Roma Restaurant',
                "food_type": 'italian food'

            }

        ],

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {"my_object":
        {
            "restaurant_name": 'Roma Restaurant' ,
            "food_type" : 'Italian food',
            "Best dish": 'margarita pizza',
            "address": '2699 Shubah Ibn Al Hajjaj, Al Olaya, Riyadh 12241 6726',
            "phone number" : '+966114641133',
            "opening hours" : '1:30-11PM'
        }
    }
    return render(request, 'detail.html', context)
