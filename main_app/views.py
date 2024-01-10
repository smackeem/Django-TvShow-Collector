from django.shortcuts import render

# Create your views here.

# shows = [
#     {title='Game of Thrones', network='HBO', run='2011-19', genre='Drama', seasons=8},
#    {title="Grey's Anatomy", network='ABC', run='2005-present', genre='Drama', seasons=20},
#     {title='Scandal', network='ABC', run='2012-18', genre='Drama', seasons=7},
#     {title='How To Get Away With Murder', network='ABC', run='2014-20', genre='Drama', seasons=6},
#     {title='Billions', network='SHOWTIME', run='2016-2023', genre='Drama', seasons=7},
#     {title='True Blood', network='HBO', run='2008-14', genre='Drama', seasons=7},
#     {title='The Big Bang Theory', network='CBS', run='2007-19', genre='Sitcom', seasons=12},
#     {title='Insecure', network='HBO', run='2016-21', genre='Drama', seasons=5},
#     {title='Watchmen', network='HBO', run='2019', genre='Drama', seasons=1},
#     {title='Succession', network='HBO', run='2018-present', genre='Drama', seasons=4},
#     {title='Mad Men', network='AMC', run='2007-15', genre='Drama', seasons=7},
#     {title='Breaking Bad', network='AMC', run='2008-13', genre='Drama', seasons=5},
#     {title='The Good Fight', network='CBS', run='2017-present', genre='Drama', seasons=6},
#     {title='The Crown', network='NETFLIX', run='2016-present', genre='Drama', seasons=6},
# ]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shows_index(request):
    return render(request, 'shows/index.html', {'shows': shows})
