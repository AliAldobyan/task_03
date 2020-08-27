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
            "restaurant_name": 'McDonald\'s' ,
            "food_type" : 'american food'

        }
    }
    return render(request, 'detail.html', context)
